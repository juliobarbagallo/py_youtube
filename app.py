from pytube import YouTube

# prompt user to enter YouTube video URL
video_url = input("Enter YouTube video URL: ")

# create YouTube object with video URL
yt = YouTube(video_url)

# get the first audio stream from the YouTube video
audio = yt.streams.filter(only_audio=True).first()

# download the audio stream to a local file
audio.download(output_path="./", filename="audio.mp3")
