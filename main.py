import streamlit as st
import requests
import time
import base64

st.title("🎬 کارگەی ڕیکلامی زیرەک")

# کلیلەکەت لێرە دابنێ
API_KEY = "REhabU5kQXhPVUJHbm1WemNqZ3ZjQm1zZWh:WXFqWmxhY1dITS1Gb2ZxTndsenNo"

# ئەنکۆدکردنی کلیلەکە بە شێوەیەکی دروست
encoded_key = base64.b64encode(API_KEY.encode()).decode()

script = st.text_area("دەقی ڕیکلامەکە:")
image_url = st.text_input("لینکێکی وێنە (JPG/PNG):")

if st.button("دروستکردنی ڤیدیۆ"):
    if script and image_url:
        st.write("خەریکی پەیوەندی بە D-ID... چاوەڕێ بە")
        
        url = "https://api.d-id.com/talks"
        # بەکارهێنانی کلیلە ئەنکۆدکراوەکە لەناو Basic Auth
        headers = {
            "Authorization": f"Basic {encoded_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "script": {"type": "text", "input": script},
            "source_url": image_url
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 201:
            talk_id = response.json().get("id")
            st.write("ڤیدیۆکە لە قۆناغی دروستکردندایە...")
            
            while True:
                time.sleep(5)
                get_url = f"https://api.d-id.com/talks/{talk_id}"
                result = requests.get(get_url, headers=headers).json()
                status = result.get("status")
                
                if status == "done":
                    video_url = result.get("result_url")
                    st.success("ڤیدیۆکە ئامادەیە!")
                    st.video(video_url)
                    break
                elif status == "error":
                    st.error("هەڵەیەک ڕوویدا، کلیلەکەت یان لینکەکەت کێشەی هەیە.")
                    break
        else:
            st.error(f"هەڵە: {response.text}")
    else:
        st.warning("تکایە هەموو خانەکان پڕ بکەرەوە.")
