import streamlit as st
from steamship import Steamship
import webbrowser

    
def prompt(title,keywords,option_min,option_max,option_tone,option_sections,option_structure):
    ''' 
    This function uses Steamship to generate a response to the given 
    prompt using the ChatGPT-4 model
    '''
    # Use the OpenAI API to generate a response
    #client = Steamship(workspace="mipo-writer-ws")
    instance = Steamship.use("mipo-gpt-writer-pkg","mipo-gpt-writer-pkg-a4d")

    #prompt = WriterPackage(client)

    with st.spinner('Wait while AI generates the article. This might take a few minutes..'):
        resp = instance.invoke("generate",title=title,keywords=keywords,min_words=option_min,max_words=option_max,tone=option_tone,paragraphs=option_sections,structure=option_structure)
    st.success("Finished")
    return resp
    


def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    #get user inputs
    option_min = st.selectbox(
    'Minimum words?',
    ('1000', '1500', '2000','2500'),index=2)

    option_max = st.selectbox(
    'Maximum words?',
    ('1500', '2000', '2500','3000'),index=2)

    option_tone = st.selectbox(
    'Tone of the article?',
    ('Informative, engaging, convey emotion','Informative, convey emotion','Informative, engaging','Informative','Conversational','Conversational, 50% spartan'))

    option_structure = st.selectbox(
    'Article structure?',
    ('Explanatory structure','20% Creative structure and 80% Explanatory structure','Creative structure','Feature structure','Rundown Structure','Expert Opinion Structure','Persuasion structure','Story structure','Series structure'),index=1)

    option_sections = st.selectbox(
    'Paragraphs?',
    ('4','5','6','7','8'),index=2)
    
    
    title = st.text_input("Write article title here.")
    keywords = st.text_input("Keywords for the article. Use comma separated list.")

    if title and keywords:
        # Pass the query to the ChatGPT function
        response = prompt(title,keywords,option_min,option_max,option_tone,option_sections,option_structure)
        return st.write(f"\n\n {response}")
        
    
    





st.title("AI article generator")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you generate articles with 
    the ChatGPT-4.
    Enter article **title** and **keywords** in the **text boxes** and **press Enter** to receive 
    a human-like generated article.
    '''
    )

st.write("\n")   


with st.sidebar:
    url = 'https://app.mash.com/e/mpoikkilehto'
    st.write("\n")
    st.write("\n")
    if st.button('Donate BTC with Mash'):
        webbrowser.open_new_tab(url)

    st.write("\n")
    st.write("\n")

    st.write("Github: [streamlit app](https://github.com/MikPoik/streamlit-gpt-article-generator.git)")
    st.write("Github: [steamship api](https://github.com/MikPoik/steamship-gpt-article-generator.git)")
    st.write("\n")
    st.write("\n")

    st.write("Powered by [Steamship](https://steamship.com)")

main()