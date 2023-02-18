import tkinter.filedialog
from tkinter.messagebox import *

import customtkinter
from pytube import YouTube
from moviepy.editor import *

def download(link):
   try:
        pasta = tkinter.filedialog.askdirectory()
        downloader = YouTube(link).streams.get_highest_resolution()
        downloader.download(pasta)

        mp4 = ".mp4"
        mp3 = ".mp3"

        video_file = downloader.title+mp4
        mp3_file = f"{downloader.title+mp3}"

        video = VideoFileClip(video_file)
        audio = video.audio
        audio.write_audiofile(mp3_file)

        video_file.close()
        mp3_file.close()

   except:
       showinfo(f"Download : {downloader.title+mp3}", "Downloade comcluido com sucesso")


janela =  customtkinter.CTk()

janela.title("Baixar video do youtube - Copie e cole o link do video")
janela.resizable(False, False)

label = customtkinter.CTkLabel(janela, text="Copie e cole a URL do video aqui (Ctrl + v)")
label.grid(column=0, row=0, padx=10, pady=10)

txt_url = customtkinter.CTkEntry(janela, width=350)
txt_url.grid(column=1, row=0, padx=10, pady=10)

btn_download = customtkinter.CTkButton(janela, text="Dowload", command=lambda : download(txt_url.get()))
btn_download.grid(column=0, row=1, padx=10, pady=10)

janela.mainloop()