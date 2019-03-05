import json
import time
import requests
import tkinter as tk
from playsound import playsound
from PIL import Image, ImageTk
import multiprocessing

def play():
	time.sleep(1.1)
	while(True):
		playsound("bitch-lasagna.mp3")

def subcount():
# To create a key for api follow the steps below:
# 	(Use this link for following the steps https://www.youtube.com/watch?v=G6a-UbG0KGk)
# 	1) Go to https://console.developers.google.com
# 	2) Create new project
# 	3) Enter that project
# 	4) Go to credentials from left section
# 	5) Click on "Create credentials" -> Click on "API key"
# 	6) Copy the apikey on your screen can paste it as value assigned to key in subcount() fuction
# 	7) Then go the library from left section and search for YouTube Data API v3
# 	8) Enable the YouTube Data API v3 and your are good to go.
	key = "Enter your API key here as per given steps above"
	pewd = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=PewDiePie&key=" + key
	tseries = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key=" + key

	p = requests.get(pewd)
	t = requests.get(tseries)

	li = (p.text).split(',')

	li_ = (t.text).split(',')
	
	pdp = str(li[9][25:len(li[9])-1])
	ts = str(li_[9][25:len(li[9])-1])

	

	diff = int(pdp) - int(ts)
	if(diff < 0):
		label.configure(text = "\n" + "\t" + "PewDiePie : " + pdp + "\t" + "\t" + "\t" + "Tseries : " + ts + "\t" + "\t" + "\n" + "Tseries is ahead of PewDiePie by "+ str(diff) + "\n")
	else:
		label.configure(text = "\n" + "\t" + "PewDiePie : " + pdp + "\t" + "\t" + "\t" + "Tseries : " + ts + "\t" + "\t" + "\n\n" + "PewDiePie is ahead of Tseries by "+ str(diff) + "\n")
	root.after(1000,subcount)


song_thread = multiprocessing.Process(target=play)
song_thread.start()

root = tk.Tk()
root.title("PewDiePie Vs Tseries")

img = ImageTk.PhotoImage(Image.open("pewd_vs_tseries.jpg"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

label = tk.Label(root, text="")
label.pack()
subcount()

root.mainloop()
song_thread.terminate()
