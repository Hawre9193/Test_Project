import streamlit as st
import random

st.title("🎲 یارییەکی شێتگیری")

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 10)

guess = st.number_input("ژمارەیەک لە نێوان ١ بۆ ١٠ هەڵبژێرە:", min_value=1, max_value=10)

if st.button("پشکنین"):
    if guess == st.session_state.number:
        st.success("ئۆھ! تۆ زیرەکیت، بەڵام بڕوا ناکەم بە ڕێکەوت بووبێت! 😎")
        st.session_state.number = random.randint(1, 10)
    else:
        st.error("هەڵەیە! تۆ هیچ لە ژمارە نازانیت، دیسان هەوڵ بدە! 🤡")
        
