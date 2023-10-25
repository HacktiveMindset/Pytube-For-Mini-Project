from pytube import YouTube

# Create a YouTube object for the video URL you want to download
url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'
yt = YouTube(url)

# Choose a stream for downloading (e.g., the highest resolution stream)
stream = yt.streams.get_highest_resolution()

# Download the video to a specific directory
download_path = '/path/to/your/download/directory'
stream.download(output_path=download_path)
print("Download complete!")
