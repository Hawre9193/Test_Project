import streamlit as st
import requests

st.title("🎬 کارگەی ڕیکلام")

# لێرە کلیلەکانت بە ڕاستەوخۆ دابنێ بۆ ئەوەی ئیش بکات
ELEVENLABS_KEY = "کلیلەکەی_ELEVENLABS_لێرە_دابنێ"
DID_KEY = "کلیلەکەی_DID_لێرە_دابنێ"

product = st.text_input("ناوی بەرهەم:")
script = st.text_area("دەقی ڕیکلام:")

if st.button("دروستکردنی ڤیدیۆ"):
    st.write("خەریکین ڤیدیۆکە دروست دەکەین...")
    # لێرە کۆدی API-یەکانت کار دەکات
    st.success("سەرکەوتوو بوو!")
