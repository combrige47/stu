import yt_dlp  
import os
def get_video_title(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict.get('title', None)
def download_video(url,resolution='1080',download_path='small_cat/video',custom_name='%(title)s'):  
    ydl_opts = {  
        'format': f"bestvideo[height<={resolution}]+bestaudio/best", 
        'outtmpl': f'{download_path}/{custom_name}.%(ext)s',     
    }  
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:  
        ydl.download([url]) 
    if custom_name=='%(title)s':
        title=get_video_title(url)
        return f'{download_path}/{title}.webm'
    else:
        return f'{download_path}/{custom_name}.webm'


download_video(url='https://www.youtube.com/watch?v=AFbNkDoc8Wg')