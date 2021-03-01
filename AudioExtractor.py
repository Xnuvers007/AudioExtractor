import os
from moviepy.editor import *

def video_2_sound(video_path):
   nama = video_path.split("/")[-1]
   musik_path = movie_path.strip(nama)
   nama = nama.split(".")[0]
   video = VideoFileClip(os.path.join(f"{musik_path}{nama}.mp3"))

if __name__ == "__main__":
   print("Drag n Drop Video here or write the path where video location: ")
   movie_path = input(r"   >> ")
   video_2_sound(movie_path)
