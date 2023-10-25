from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=YOUR_VIDEO_ID')

# Choose the audio stream
audio_stream = yt.streams.get_audio_only()

# Download the audio to a specific directory
download_path = '/path/to/your/download/directory'
audio_stream.download(output_path=download_path, filename="audio_only.mp3")
print("Audio download complete!")
