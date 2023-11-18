import streamlit as st
import pafy

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
