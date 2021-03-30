from tkinter import *
from pytube import *
from pytube import Playlist
 
 
 
   
window=Tk()

#Tittle Of The Window
window.title("Download Youtube Videos")
#size Of The Window
window.geometry('350x200')


    
#multiple Video i.e PLaylist Action 
def lst():
    playlist = Playlist(url.get())
    #Shows The Number of Videos Available in The Playlist On The Status Box 
    number=len(playlist.video_urls)
    status='Number of videos in Link:'+str(number)
    t1.insert(END,status)
    
    i=0 #Video Count Initialization
    for video in playlist.videos:
        video.streams.first().download()
        #Video count Iteration
        i=i+1
        #Shows The Status on The Status Box
        status ="Video Downloaded Successfully:"+str(i)
        t1.insert(END,status)
       
#single Video link Action      
def single():
      link =url.get()
      yt_obj = YouTube(link)
      filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
      filters.get_highest_resolution().download()
      #Showing Status Of Download To The Status Box
      status ="Video Downloaded Successfully"
      t1.insert(END,status)   
    
#Download Button
b1=Button(window,text="Download",command=single)
b1.place(x=200,y=20)

#Playlist Download Button
b1=Button(window,width=35,text="Playlist Download",command=lst)
b1.place(x=10,y=50)

#Taking Input OF The link in the Entry Box
lbl = Label(window, text="Enter The Link")
url=StringVar()
e1=Entry(window,width=30,textvariable=url)
e1.place(x=10,y=20)

#Showing Download Status [Status Box]
t1=Text(window,height=7,width=41)
t1.place(x=10,y=80)

#Helps To keep up the Tinkter Window Alive
window.mainloop()
