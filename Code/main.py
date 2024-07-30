import tkinter
import customtkinter
from pytube import YouTube


#Declare download function
def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Download Error", text_color="red")
        
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.file_size
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size *100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')    
    pPercentage.update()
    
    #update progress bar
    progressBar.set(float(percentage_of_completion)/100)
    
    
        
#$system settings
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

#adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#finished downloading

finishLabel = customtkinter.CTkLabel(app, text = "")
finishLabel.pack()


#progress percentage
pPercentage=customtkinter.CTkLabel(app, text = "O%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


#Dowload button
download=customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)



#Run App
app.mainloop()


