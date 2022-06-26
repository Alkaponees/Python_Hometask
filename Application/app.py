
from lib.download import Downloader_youtube_movie

Download_youtube_movie = Downloader_youtube_movie()

exit = False

while not exit:
    choice = Download_youtube_movie.menu()
    if choice == 1:
        Download_youtube_movie.download_youtube_video()
    elif choice == 2:
        Download_youtube_movie.download_youtube_playlist()
        exit = True
    else :
        print("Read help:")