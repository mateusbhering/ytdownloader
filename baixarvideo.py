from pytube import YouTube
from sys import argv

link = input("Digite a URL do vídeo: ")
path = input("Onde deseja salvar o vídeo: ")

yt = YouTube(link)

baixar = yt.streams.get_highest_resolution()

baixar.download(path)

print("Download concluído")