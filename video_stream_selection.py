from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=YOUR_VIDEO_ID')

# Choose a video stream by criteria like resolution and file format
stream = yt.streams.filter(res="720p", file_extension="mp4").first()

# Download the selected video stream to a specific directory
download_path = '/path/to/your/download/directory'
stream.download(output_path=download_path)
