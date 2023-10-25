from pytube import Playlist

# Create a Playlist object for the YouTube playlist URL
playlist_url = 'https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID'
playlist = Playlist(playlist_url)

# Iterate through the videos in the playlist and download them
for video_url in playlist.video_urls:
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    download_path = '/path/to/your/download/directory'
    stream.download(output_path=download_path)
