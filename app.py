import streamlit as st
from deep_translator import GoogleTranslator

# Function to get language code from language name
def get_language_code(language_name):
    languages = {
        'English': 'en',
        'French': 'fr',
        'Spanish': 'es',
        'German': 'de',
        'Italian': 'it'
    }
    return languages.get(language_name.capitalize(), None)

# Custom CSS for styling the app
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        max-width: 800px;
        margin: auto;
        padding-top: 40px;
        padding-bottom: 40px;
        background: #fff;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        padding: 30px;
    }
    h1 {
        color: #003366;
        font-size: 42px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    p {
        text-align: center;
        color: #4B0082;
        font-size: 20px;
    }
    .stTextInput, .stTextArea, .stButton {
        font-size: 18px !important;
    }
    .stTextArea textarea, .stTextInput input {
        padding: 12px;
        font-size: 18px;
        border-radius: 10px;
        border: 2px solid #4CAF50;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background-color: #ff6666;
        color: white;
        font-size: 20px;
        padding: 12px 24px;
        border: none;
        border-radius: 10px;
        margin-top: 20px;
        cursor: pointer;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ff4d4d;
        transform: translateY(-2px);
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.3);
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
st.title("🌍 Language Translator")

st.write("Translate text between languages with ease and style. Powered by Deep Translator.")

# Input text
source_text = st.text_area("📝 Enter the text you want to translate:", "", height=150)

# Input source language (fixed selection)
source_lang = st.selectbox("🌐 Select source language", ["English", "French", "Spanish", "German", "Italian"], index=0)

# Target language input (searchable by name)
target_language_search = st.text_input("🔎 Enter target language name (e.g., French, Spanish, German):")

# Translate button
if st.button("Translate"):
    target_lang_code = get_language_code(target_language_search)

    if target_lang_code is None:
        st.warning(f"⚠ Error: '{target_language_search}' is not a valid language name. Please try again.")
    else:
        try:
            # Using deep-translator for translation
            translator = GoogleTranslator(source=source_lang.lower(), target=target_lang_code)
            translated_text = translator.translate(source_text)
            st.success(f"🎯 *Translated Text*: {translated_text}")
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
        """
    )

# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ using Streamlit and Deep Translator
    </div>
    """, unsafe_allow_html=True)
