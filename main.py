import streamlit as st

st.title("حاسیبەی سادە")

num1 = st.number_input("ژمارەی یەکەم")
num2 = st.number_input("ژمارەی دووەم")
operation = st.selectbox("جۆری کردار", ["کۆکردنەوە", "لێدەرکردن"])

if st.button("ئەنجام"):
    if operation == "کۆکردنەوە":
        st.write("ئەنجام:", num1 + num2)
    else:
        st.write("ئەنجام:", num1 - num2)
      
