from pathlib import Path
from pytube import YouTube

# current paths
current_path = Path(__file__).parent.absolute()

# Using readlines()
videos_text = open('videos.txt', 'r')
lines = videos_text.readlines()

# Strips the newline character
count = 0
for line in lines:
    if '[x]' in line:
        dir = line.split('[x]')[1].strip()
        current_path = current_path/dir
        current_path.mkdir(exist_ok=True)

    if not line.strip() == '' and not '[x]' in line:
        url = line.strip()
        count = count+1
        print("[+] downloading video from {}".format(url))
        yt = YouTube(url)
        stream = yt.streams.first()
        stream.download(current_path)
