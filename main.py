import streamlit as st

st.title("حاسیبەی پێشکەوتوو")

num1 = st.number_input("ژمارەی یەکەم")
num2 = st.number_input("ژمارەی دووەم")

# لێرەدا هەموو کردارەکان دەخەینە ناو لیستێکەوە
operations = ["کۆکردنەوە", "لێدەرکردن", "لێکدان", "دابەشکردن"]
op = st.selectbox("جۆری کردار", operations)

# لێرەدا پایتۆن خۆی بەپێی هەڵبژاردنەکەی تۆ کردارەکە دەکات
if op == "کۆکردنەوە": st.write("ئەنجام:", num1 + num2)
elif op == "لێدەرکردن": st.write("ئەنجام:", num1 - num2)
elif op == "لێکدان": st.write("ئەنجام:", num1 * num2)
elif op == "دابەشکردن":
    if num2 != 0: st.write("ئەنجام:", num1 / num2)
    else: st.write("هەڵە: دابەشکردن بەسەر سفر نابێت")
