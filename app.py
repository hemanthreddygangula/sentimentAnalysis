import streamlit as st
import joblib
import base64
st.set_page_config(layout='wide')
st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        font-family:Felix Titling Regular;
    }
    </style> 
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .small-font {
        font-size: 18px !important;
        font-family:Felix Titling Regular;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .medium-font {
        font-size:20px !important;
        font-family:Felix Titling Regular;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">IMDB Review Sentiment Analysis !!</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">Enter Review !!</p>', unsafe_allow_html=True)
review = st.text_input("Here")
model = joblib.load('imdb-rating')
op = model.predict([review])
if st.button('Analyse'):
  st.markdown(f'<p class="medium-font"> The Review is {op[0]} </p>',unsafe_allow_html=True)
