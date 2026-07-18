import streamlit as st
import requests
import time

st.title("🎬 کارگەی ڕیکلامی زیرەک")

# کلیلەکەت ڕاستەوخۆ لێرە دانراوە
API_KEY = "DHZmNDAxOUBnbWFpbC5jb20:Gb5eGN6xw6lF5IKnBFsuP"

script = st.text_area("دەقی ڕیکلامەکە:")
image_url = st.text_input("لینکێکی وێنە (JPG/PNG):")

if st.button("دروستکردنی ڤیدیۆ"):
    if script and image_url:
        st.write("خەریکی پەیوەندی بە D-ID... چاوەڕێ بە")
        
        url = "https://api.d-id.com/talks"
        headers = {
            "Authorization": f"Basic {API_KEY}",
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
                    st.error(f"هەڵە ڕوویدا: {result}")
                    break
        else:
            st.error(f"هەڵە: {response.status_code} - {response.text}")
    else:
        st.warning("تکایە هەموو خانەکان پڕ بکەرەوە.")
