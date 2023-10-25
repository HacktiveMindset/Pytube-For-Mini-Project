from pytube import YouTube

# Create a YouTube object for the video URL you want to download
url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'
yt = YouTube(url)

# Get the video's captions and save them to a file
caption = yt.captions.get_by_language_code('en')
download_path = '/path/to/your/download/directory'
caption.download(output_path=download_path)
