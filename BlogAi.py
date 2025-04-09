import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#function to get responce from LLAMA 2 model

def getLLAMAresponse(input_text,no_words,blog_style):
    ##llama 2 model
    llm=CTransformers(model='C:\\Users\\nijhi\\PycharmProjects\\Blog Generation with LLAMA 2 model\\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens' :256,
                              'temperature':0.01})

    #prompt tempelate

    template="""
    please write the blog on {input_text} Topic in a proper manner as a blogger for {blog_style}
    within {no_words} words.
    """

    prompt=PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                          template=template)

    #generate the response from the llama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)

    return response


st.set_page_config(page_title="Generate Blogs",
                   page_icon='*',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs with LLAMA 2 Model")

input_text=st.text_input("Enter the Blog Topic")

#more column for 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of words')
with col2:
    blog_style=st.text_input('Writing the blog for',placeholder='Optional')

#with col2:
#    blog_style=st.selectbox('Writing the blog for',('common people','Data Scientists','Sportsmen'),index=0)

submit=st.button("Generate")

#final responce

if submit:
    st.write(getLLAMAresponse(input_text,no_words,blog_style))


