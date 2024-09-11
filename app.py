import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize Google Translator
translator = Translator()

# Function to get language code from language name
def get_language_code(language_name):
    for lang_code, lang_name in LANGUAGES.items():
        if lang_name.lower() == language_name.lower():
            return lang_code
    return None

# Custom CSS for styling the app
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
    }
    .stTextInput, .stTextArea, .stButton {
        font-size: 16px !important;
        color: #333333;
    }
    h1, h2, h3, p {
        text-align: center;
        color: #4B0082;
    }
    .stButton > button {
        background-color: #ff5733; /* New button background color */
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #c70039; /* New button hover color */
    }
    .stTextInput input, .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #4CAF50;
        padding: 10px;
        color: #333333;
        font-size: 16px;
        background-color: #f0f8ff;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #6a0dad;
        box-shadow: 0px 0px 8px #6a0dad;
    }
    .lang-list {
        text-align: center;
        font-size: 16px;
        color: #333333;
    }
    footer {
        font-size: 12px;
        color: #808080;
        padding: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit UI
st.title("Language Translator")

# Input text
source_text = st.text_area("Enter the text you want to translate:", "")

# Input source language dropdown
source_lang = st.selectbox("Select source language", list(LANGUAGES.keys()), index=list(LANGUAGES.keys()).index('en'))

# Input target language dropdown
target_lang = st.selectbox("Select target language", list(LANGUAGES.keys()), index=list(LANGUAGES.keys()).index('fr'))

# Translate button
if st.button("Translate"):
    # Using googletrans for translation
    translated_text = translator.translate(source_text, src=source_lang, dest=target_lang).text
    st.success(f"**Translated Text**: {translated_text}")
