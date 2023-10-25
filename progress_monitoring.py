from pytube import YouTube

# Create a YouTube object for the video URL you want to download
url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'
yt = YouTube(url)

# Define a progress callback function
def on_progress(stream, chunk, bytes_remaining):
    # Implement your progress update logic here
    pass

# Download the video to a specific directory and monitor progress
download_path = '/path/to/your/download/directory'
stream = yt.streams.get_highest_resolution()
stream.download(output_path=download_path, filename="video.mp4", on_progress=on_progress)
