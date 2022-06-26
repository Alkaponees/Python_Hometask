from subprocess import call
import os

class Downloader_youtube_movie(): 
    def menu(self):
        choice = int(input("1.Download video \n 2.Download Playlist \n 0.Exit "))
        return choice
    
    def download_youtube_video(self):
        movie_url = input('Enter movie url: ')
        movie_info = "youtube-dl " + movie_url + " -F"
        call (movie_info, shell = False)
        movie_format = input ("Enter format of movie... ")
        os.chdir("Downloads")
        download_command = "youtube-dl -f " + movie_format +" "+ movie_url + " -c"
        call(download_command, shell=False)
    def download_youtube_playlist(self):
        playlist_url = input('Enter playlist URL... ')
        os.chdir("Downloads")
        download_playlist_command = "youtube-dl -f best"  +" "+ playlist_url 
        call(download_playlist_command, shell=False)