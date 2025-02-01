# Import Libraries
import streamlit as st
from googletrans import Translator, LANGUAGES

# Set page title and configuration
st.set_page_config(page_title="Language Converter")

st.markdown("""
            <style>

            .title{
            font-size: 2em;
            color: red;
            text-align: center;
            padding: 20px;
            background-color: cyan;
            border-radius: 10px;
            box-shadow: 2px 2px 5px 0px rgba(0,0,0,0.1);
            }
            
            .text{
            font-size: 1.2em;
            color: #333333;
            }
            
            .stButton>button{
            background-color: #1f77b4;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            }

            </style>
""", unsafe_allow_html=True
)

# Render styled elements
st.markdown("<h1 class='title'>Language Converter</h1>", unsafe_allow_html=True)
st.markdown("<p class='text'>This is a Language Converter UI. You can change it to your preferred language!</p>", unsafe_allow_html=True)

# Initialize the translator
translator = Translator()

#audio
st.audio("ad.mp3", format="audio/mpeg", loop=False)

# Text input for the text to be translated
text_to_translate = st.text_area("Hi, Please enter text here to translate")

# Dropdowns for selecting source and target languages
source_language = st.selectbox("Select your source language", list(LANGUAGES.values()), index=list(LANGUAGES.keys()).index('en'))
target_language = st.selectbox("Select your target language you want", list(LANGUAGES.values()), index=list(LANGUAGES.keys()).index('hi'))

# Source and Target Languages codes
source_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(source_language)]
target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]

# Translation Button
if st.button("Translate"):
    if text_to_translate:
        translation = translator.translate(text_to_translate, src=source_language_code, dest=target_language_code)
        st.write(f"**Your Translated Text:**\n\n {translation.text}")
    else:
        st.error("Please enter some text to translate!")
        st.write("Enter text in the text area above, select source and target languages, and click 'Translate' to see the translation!")