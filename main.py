import time
from pytube import YouTube
import os
import sys


def download_video(video_url):
    yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
    filename = yt.title.replace(' ', '_')
    print(f'Downloading file: {yt.title}')

    start_time = time.time()
    path_to_download_folder = os.path.expanduser('~/Downloads')
    yt.streams.get_highest_resolution().download(filename=os.path.join(path_to_download_folder, f'{filename}.mp4'))
    end_time = time.time()

    print(f'Download of {filename}.mp4 complete. {round(end_time - start_time, 2)} elapsed')


if __name__ == '__main__':
    if len(sys.argv) > 1 and 'youtube.com' in sys.argv[1]:
        download_video(sys.argv[1])
    else:
        url = ''

        while 'youtube.com' not in url:
            url = input('Enter YouTube video URL: ')

        download_video(url)

