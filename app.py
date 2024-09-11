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
        background-color: #e6f2ff;
    }
    .stApp {
        max-width: 800px;
        margin: auto;
        padding-top: 30px;
    }
    h1 {
        color: #003366;
        font-size: 40px;
        text-align: center;
        margin-bottom: 10px;
    }
    .stTextInput, .stTextArea, .stButton {
        font-size: 18px !important;
    }
    p {
        text-align: center;
        color: #4B0082;
        font-weight: 500;
    }
    .stButton > button {
        background-color: #0066cc;
        color: white;
        font-size: 18px;
        padding: 12px 30px;
        border: none;
        border-radius: 6px;
        margin-top: 10px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #004d99;
    }
    .stTextInput input {
        border-radius: 10px;
        border: 2px solid #4CAF50;
        padding: 10px;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #4CAF50;
        padding: 12px;
    }
    .stSelectbox, .stTextInput {
        margin-bottom: 20px;
    }
    .supported-languages {
        font-weight: bold;
        color: #333;
        padding-top: 20px;
    }
    .footer {
        text-align: center;
        padding-top: 40px;
        font-size: 16px;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit UI
st.title("🌐 Language Translator")

st.write("Easily translate text between different languages with an intuitive interface.")

# Input text
source_text = st.text_area("📝 Enter the text you want to translate:", "")

# Input source language (fixed selection)
source_lang = st.selectbox("🌍 Select source language", ["en", "fr", "es", "de", "it"], index=0)

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
            translator = GoogleTranslator(source=source_lang, target=target_lang_code)
            translated_text = translator.translate(source_text)
            st.success(f"🎯 Translated Text: {translated_text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Show supported languages with a better design
if st.checkbox("Show supported languages"):
    st.write("Supported Languages:")
    st.write(
        """
        - English
        - French
        - Spanish
        - German
        - Italian
        """
    )

# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ using Streamlit and Deep Translator
    </div>
    """, unsafe_allow_html=True)
