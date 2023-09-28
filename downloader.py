#     
#     ██████╗░██╗░░░██╗███╗░░██╗██╗██╗░░██╗
#     ██╔══██╗╚██╗░██╔╝████╗░██║██║╚██╗██╔╝
#     ██████╔╝░╚████╔╝░██╔██╗██║██║░╚███╔╝░
#     ██╔══██╗░░╚██╔╝░░██║╚████║██║░██╔██╗░
#     ██║░░██║░░░██║░░░██║░╚███║██║██╔╝╚██╗
#     ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝╚═╝╚═╝░░╚═╝


import os
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_mp3():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path="downloads")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        messagebox.showinfo("Success", f"{yt.title} has been successfully downloaded as an MP3.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

player = tk.Tk()
player.title("YouTube MP3 Downloader")

window_width = 500
window_height = 250
screen_width = player.winfo_screenwidth()
screen_height = player.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
player.geometry(f"{window_width}x{window_height}+{x}+{y}")
player.configure(bg="#333")

title_label = tk.Label(player, text="YouTube MP3 Downloader", font=("Arial", 24), bg="#333", fg="white")
title_label.pack(pady=20)

url_label = tk.Label(player, text="Enter the URL of the video you want to download:", font=("Arial", 12), bg="#333", fg="white")
url_label.pack()
url_entry = tk.Entry(player, width=40)
url_entry.pack(pady=10)

download_button = tk.Button(player, text="Download MP3", command=download_mp3, bg="lightgreen")
download_button.pack()

player.mainloop()
