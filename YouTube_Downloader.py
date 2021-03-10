from pytube import YouTube
#URL ="https://youtu.be/gNN7hyUi0To"
dUrl="https://youtu.be/gNN7hyUi0To"
ytd=YouTube(dUrl).streams.first().download()
print("Download Completed")