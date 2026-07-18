import streamlit as st
import requests
import time

st.title("🎬 کارگەی ڕیکلامی زیرەک")

API_KEY = "REhabU5kQXhPVUJHbm1WemNqZ3ZjQm1zZWh:WXFqWmxhY1dITS1Gb2ZxTndsenNo"

script = st.text_area("دەقی ڕیکلامەکە:")
image_url = st.text_input("لینکێکی وێنە (JPG/PNG):")

if st.button("دروستکردنی ڤیدیۆ"):
    if script and image_url:
        # ١. دروستکردنی داواکاری
        url = "https://api.d-id.com/talks"
        headers = {"Authorization": f"Basic {API_KEY}", "Content-Type": "application/json"}
        payload = {"script": {"type": "text", "input": script}, "source_url": image_url}
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 201:
            talk_id = response.json().get("id")
            st.write("ڤیدیۆکە لە قۆناغی دروستکردندایە، تکایە چاوەڕێ بکە...")
            
            # ٢. چاوەڕێکردن بۆ تەواوبوونی ڤیدیۆکە
            while True:
                time.sleep(5) # هەر ٥ چرکە جارێک پشکنین دەکات
                get_url = f"https://api.d-id.com/talks/{talk_id}"
                result = requests.get(get_url, headers=headers).json()
                status = result.get("status")
                
                if status == "done":
                    video_url = result.get("result_url")
                    st.success("ڤیدیۆکە ئامادەیە!")
                    st.video(video_url) # ڤیدیۆکە لەناو سایتەکەدا پیشان دەدات
                    break
                elif status == "error":
                    st.error("هەڵەیەک لە دروستکردنی ڤیدیۆکەدا ڕوویدا.")
                    break
        else:
            st.error(f"هەڵە: {response.text}")
    else:
        st.warning("تکایە هەموو خانەکان پڕ بکەرەوە.")
