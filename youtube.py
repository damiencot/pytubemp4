from pathlib import Path

from pytube import YouTube
import os

from progress_bar import show_progress_bar

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
Downloaded_PATH = ""
if not os.path.exists(path_to_download_folder):
    os.makedirs('Downloaded_Videos')
    folder = "Downloaded_Videos"
    directory = os.getcwd()
    Downloaded_PATH = os.path.join(directory, folder)
    print("Downloads folder doesn't exist so Downloaded_Videos folder created")
else:
    Downloaded_PATH = path_to_download_folder
    print("Downloads folder exist")


link = input("Enter the video link: ")
print("Loading video...")

def youtube():
    try:
        SAVE_PATH = Downloaded_PATH

        yt = YouTube(link)
        print('Title :',yt.title)

        print('Available Formats: ')
        for stream in yt.streams:
            print(stream)

        itag =  input("\nEnter the itag number to select a format: ")
        stream = yt.streams.get_by_itag(itag)

        print("\nDownloading --> "+yt.title+' to '+SAVE_PATH)

        yt.register_on_progress_callback(show_progress_bar)
        stream.download(SAVE_PATH)

        print('Download Finished!')
        input('Press Return to Exit')
    except Exception as e:
        print("Error :",e)
        input('Press Return to Exit')