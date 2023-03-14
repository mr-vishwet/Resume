import streamlit as st
import requests

# download the YouTube video and save it to a file
def download_video(video_url, file_path):
    response = requests.get(video_url)
    with open(file_path, "wb") as f:
        f.write(response.content)

# create a text input widget for entering the YouTube video URL
video_url = st.text_input("Enter YouTube video URL", "")

# create a download button that downloads the video when clicked
if st.button("Download video"):
    try:
        # download the video to the default download directory on the remote server
        file_name = "video.mp4"
        download_video(video_url, file_name)

        # offer the downloaded video as a download button
        st.download_button(
            label="Download video",
            data=file_name,
            mime="video/mp4",
        )
    except Exception as e:
        st.write("Error:", e)

