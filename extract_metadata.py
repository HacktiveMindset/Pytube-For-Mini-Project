from pytube import YouTube

url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'
yt = YouTube(url)

print("Video Title:", yt.title)
print("Video Views:", yt.views)
print("Video Length:", yt.length, "seconds")
