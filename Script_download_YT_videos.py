from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=tv_9doDQJU0'
 
yt_obj = YouTube(youtube_video_url)

for stream in yt_obj.streams:
    print(stream)

filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
 
for mp4_filter in filters:
    print(mp4_filter)

filters.get_highest_resolution().download()    
