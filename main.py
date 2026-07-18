import streamlit as st
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip
import os

# ١. ناونیشان و ڕوونی بەرنامەکە
st.set_page_config(page_title="کارگەی ڕیکلام", page_icon="🎬")
st.title("🎬 کارگەی دروستکردنی ڕیکلامی ئۆتۆماتیک")
st.write("وەک پڕۆگرامسازێک، تەنها ئەمر بکە و ڤیدیۆکەت وەرگرەوە!")

# ٢. وەرگرتنی زانیارییەکان لە بەکارهێنەر
product_name = st.text_input("📦 ناوی بەرهەم یان بزنسەکەت:")
ad_text = st.text_area("✍️ دەقی ڕیکلامەکە (بە ئینگلیزی یان لاتینی بۆ ئەوەی ئەی ئای بیخوێنێتەوە):")
uploaded_image = st.file_uploader("🖼️ وێنەی بەرهەمەکە لێرە باربکە", type=["png", "jpg", "jpeg"])

# ٣. دوگمەی داگیرساندنی بزووێنەری کۆدەکە
if st.button("🚀 ڕیکلامەکە دروست بکە"):
    if product_name and ad_text and uploaded_image:
        with st.spinner("کۆدەکە خەریکی مۆنتاژ و دروستکردنی دەنگە... چاوەڕێ بە..."):
            try:
                # خەزنکردنی کاتیی وێنە بارکراوەکە
                image_path = "temp_prod_img.png"
                with open(image_path, "wb") as f:
                    f.write(uploaded_image.getbuffer())
                
                # دروستکردنی دەنگی ئەی ئای
                audio_path = "temp_ad_audio.mp3"
                tts = gTTS(text=ad_text, lang='en')
                tts.save(audio_path)
                
                # دروستکردنی ڤیدیۆکە بە MoviePy
                audio_clip = AudioFileClip(audio_path)
                video_clip = ImageClip(image_path).set_duration(audio_clip.duration)
                final_video = video_clip.set_audio(audio_clip)
                
                output_filename = f"{product_name}_ad.mp4"
                final_video.write_videofile(output_filename, fps=24, codec="libx264", audio_codec="aac")
                
                # پیشاندانی ئەنجامەکە لە ئەپەکەدا
                st.success("✨ ڕیکلامەکەت بە سەرکەوتوویی ئامادە بوو!")
                st.video(output_filename)
                
                # دوگمەی دابەزاندن بۆ کڕیارەکە
                with open(output_filename, "rb") as file:
                    st.download_button(
                        label="📥 دابەزاندنی ڤیدیۆی ڕیکلامەکە",
                        data=file,
                        file_name=output_filename,
                        mime="video/mp4"
                    )
                    
                # پاککردنەوەی فایلە کاتییەکان
                audio_clip.close()
                video_clip.close()
                
            except Exception as e:
                st.error(f"هەڵەیەک لە کۆدەکەدا ڕوویدا: {e}")
    else:
        st.warning("تکایە دڵنیا ببەرەوە کە ناوی بەرهەم، دەق، و وێنەکەت داناوە!")
