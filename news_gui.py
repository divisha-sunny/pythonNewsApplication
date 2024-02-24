import io
import webbrowser
import requests
from tkinter import * #imports all classes from tkinter
from urllib.request import urlopen
from PIL import ImageTk, Image

class NewsApp:

    def __init__(self):
        
        #Whatever is in constructor is executed first.
        # 1) Fetch Data -> For this we have to import a module named requests In this module we have get() function to fetch the data.
        #Explicitly we called json so that the data we got willbe stored in the json format in data variable. 
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=fc3c08dfcd1143c4887b8f1cdce5b9e8').json()
        #print(data)

        # 2) Initial GUI load = First we have import tkinter

        self.load_gui()

        # 3) Load the 1st item

        self.load_news_item(0) #We want to load first item
    
    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title('News Application')
        self.root.configure(background='black')
    
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):

        #Whenever I click next, this function should be called with next news item
        #For the next item to be displayed, first we have to clear the screen of the previous item.
        self.clear()

        # We have to display photo, heading, details

        #Image

        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://images.wondershare.com/repairit/aticle/2021/07/resolve-images-not-showing-problem-1.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image = photo)
        label.pack()

        #heading

        heading = Label(self.root, text= self.data['articles'][index]['title'], bg = 'black', fg = 'white',
                        wraplength=350, justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana', 15))

        #details

        details = Label(self.root, text= self.data['articles'][index]['description'], bg = 'black', fg = 'white',
                        wraplength=350, justify='center')
        details.pack(pady=(2,20))
        details.config(font=('verdana', 12))

        #Placing Buttons

        frame = Frame(self.root, bg = 'black')
        frame.pack(expand=True, fill = BOTH)

        if (index != 0):
            prev = Button(frame, text = 'Previous', width= 16, height= 3, command= lambda: self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text = 'Read More', width= 16, height= 3, command= lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if (index != len(self.data['articles'])-1):
            next = Button(frame, text = 'Next', width= 16, height= 3, command= lambda: self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()
    
    def open_link(self, url):
        webbrowser.open(url)

Obj = NewsApp()