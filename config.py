import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

def get_api_key():
    try:
        import streamlit as st
        if 'GROQ_API_KEY' in st.secrets:
            return st.secrets['GROQ_API_KEY']
    except Exception:
        pass
    return os.environ.get('GROQ_API_KEY')

def get_groq_client():
    api_key = get_api_key()
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found set it in env or in streamlit secrets"
        )


    return Groq(api_key=api_key)
