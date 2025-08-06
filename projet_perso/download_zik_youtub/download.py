import yt_dlp

def download_audio(url):

    try:
        options = {
            'format': 'bestaudio/best',
            'outtmpl': 'C:/Users/allio/Downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error downloading audio: {e}")
if __name__ == "__main__":
    download_audio("https://www.youtube.com/watch?v=ilJI6CyRrao&ab_channel=JungTutis")
