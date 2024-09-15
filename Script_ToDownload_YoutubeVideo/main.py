from pytubefix import YouTube
from pytubefix import Search
from pytubefix.cli import on_progress

""" Search video """
result = Search('')

for media in result.videos:
    print(f'Title: {media.title}')
    print(f'Author: {media.author}')
    print(f'URL: {media.watch_url}')
    print(f'Duration: {media.length} seconds')
    print('---')

""" Download mp4 """
url = 'https://www.youtube.com/watch?v=ws1YxJtVaIM'
video = YouTube(url, on_progress_callback=on_progress)

print("Progress: ")
video_streams = video.streams.get_highest_resolution()
video_streams.download()
print("\nYour video " + url.title() + " is successfully downloaded.")

""" Download mp3 """
print("Progress: ")
audio_streams = video.streams.get_audio_only()
audio_streams.download(mp3=True)
print("\nYour video " + url.title() + " is successfully downloaded.")
