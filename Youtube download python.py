import pytube
link="https://www.youtube.com/watch?time_continue=4&v=ChA_zph7aao"
yt=pytube.YouTube(link)
stream=yt.streams.first()
stream.download()
