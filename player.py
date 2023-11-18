import streamlit as st
import pafy
import os

# Function to get video URL
def get_video_url():
    video_url = st.text_input("Enter video URL:")
    return video_url

# Function to display video player
def display_video(video_url):
    try:
        video = pafy.new(video_url)
        best_stream = video.getbest(preftype="mp4")
        st.video(best_stream.url)
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Download youtube-dl binary
def download_youtube_dl():
    os.system("mkdir -p bin")
    os.system("curl -L https://yt-dl.org/downloads/latest/youtube-dl -o bin/youtube-dl")
    os.system("chmod +x bin/youtube-dl")

# Check if youtube-dl is available, otherwise download it
if not os.path.isfile("bin/youtube-dl"):
    st.warning("Downloading youtube-dl...")
    download_youtube_dl()
    st.success("youtube-dl downloaded successfully.")

# Main function
def main():
    st.title("Video Player")

    # Get video URL from user input
    video_url = get_video_url()

    # Display video player
    if st.button("Play Video"):
        display_video(video_url)

if __name__ == "__main__":
    main()
