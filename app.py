import streamlit as st
from deep_translator import GoogleTranslator

# Function to get language code from language name
def get_language_code(language_name):
    languages = {
        'English': 'en',
        'French': 'fr',
        'Spanish': 'es',
        'German': 'de',
        'Italian': 'it',
        'Malayalam': 'ml'
    }
    return languages.get(language_name.capitalize(), None)

# Custom CSS for styling the app with new color scheme
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #f093fb 0%, #f5576c 100%);
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        max-width: 800px;
        margin: auto;
        padding-top: 40px;
        padding-bottom: 40px;
        background: #fff;
        border-radius: 20px;
        box-shadow: 0px 4px 25px rgba(0, 0, 0, 0.15);
        padding: 30px;
    }
    h1 {
        color: #3D155F;
        font-size: 45px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    p {
        text-align: center;
        color: #A239CA;
        font-size: 20px;
    }
    .stTextInput, .stTextArea, .stButton {
        font-size: 18px !important;
    }
    .stTextArea textarea, .stTextInput input {
        padding: 12px;
        font-size: 18px;
        border-radius: 15px;
        border: 2px solid #5A189A;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
    }
    .stButton > button {
        background-color: #E07A5F;
        color: white;
        font-size: 20px;
        padding: 12px 30px;
        border: none;
        border-radius: 15px;
        margin-top: 20px;
        cursor: pointer;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #F4A261;
        transform: translateY(-3px);
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.3);
    }
    .stSelectbox, .stTextInput {
        margin-bottom: 25px;
    }
    .supported-languages {
        font-weight: bold;
        color: #333;
        padding-top: 20px;
    }
    .footer {
        text-align: center;
        padding-top: 30px;
        font-size: 16px;
        color: #333;
    }
    .stCheckbox {
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit UI
st.title("Language Translator")

st.write("Translate text between languages effortlessly with a colorful and elegant interface.")

# Input text
source_text = st.text_area("📝 Enter the text you want to translate:", "", height=150)

# Input source language (dropdown selection)
source_lang = st.selectbox("🌐 Select source language", ["English", "French", "Spanish", "German", "Italian", "Malayalam"], index=0)

# Target language input (dropdown selection)
target_lang = st.selectbox("🎯 Select target language", ["English", "French", "Spanish", "German", "Italian", "Malayalam"], index=1)

# Translate button
if st.button("Translate"):
    target_lang_code = get_language_code(target_lang)
    source_lang_code = get_language_code(source_lang)

    if target_lang_code is None:
        st.warning(f"⚠ Error: '{target_lang}' is not a valid language name. Please try again.")
    else:
        try:
            # Using deep-translator for translation
            translator = GoogleTranslator(source=source_lang_code, target=target_lang_code)
            translated_text = translator.translate(source_text)
            st.success(f"🌍 *Translated Text*: {translated_text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Show supported languages with better design
if st.checkbox("Show supported languages"):
    st.write("Supported Languages:")
    st.markdown(
        """
        - **English**
        - **French**
        - **Spanish**
        - **German**
        - **Italian**
        - **Malayalam**
        """
    )

