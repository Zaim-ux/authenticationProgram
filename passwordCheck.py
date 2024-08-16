from tkinter import *
from PIL import Image, ImageTk
import os
import re

def submit():
    password = entry.get()


#conditions made to see if inputted password meets requirements
lowercaseCheck = r'^(?=.*[a-z])'
uppercaseCheck = r'^(?=.*[A-Z])'
numberCheck = r'^(?=.*\d)'
characterCheck = r'^(?=.*[@$!%*?&])'

#this variable will check if the inputted password meets all requirements
passwordVerification = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])'


#Retrieves the file path for the image needed
script_dir = os.path.dirname(__file__)



#window is created and icon is customised 
window = Tk()
window.geometry("420x400")
zPath = os.path.join(script_dir, 'zIcon.jpg')
zIcon = Image.open(zPath)
image = ImageTk.PhotoImage(zIcon)
window.wm_iconphoto(False, image)
window.title("passwordVerifier")

#input button created for user to enter password
entry = Entry()
entry.config(font= 25)
entry.pack()

#Submit button created on GUI which will call the submit() method
#allows user to enter their chosen password to be verified
submit = Button(window, text="submit", command=submit, padx=30, pady=20, font=20)
submit.pack(side = BOTTOM)

#Green tick image created to indicate a condition has been met on GUI
greenPath = os.path.join(script_dir, 'greenTick.png')
greenTick = Image.open(greenPath).resize((20, 20))
green = ImageTk.PhotoImage(greenTick)

#Red cross image created to indicate a condition hasn't been met on GUI
redPath = os.path.join(script_dir, 'redX.png')
redX = Image.open(redPath).resize((20, 20))
red = ImageTk.PhotoImage(redX)

#Labels created to show the user which conditions are required for their password as well as
#if the condition has been met with an image
condition1 = Label(window, text="8 characters long?", image=red, compound='right')
condition1.pack(anchor=W, padx=150)

condition2 = Label(window, text="lowercase letters?", image=red, compound='right')
condition2.pack(anchor=W, padx=150)

condition3 = Label(window, text="uppercase?", image = red, compound='right')
condition3.pack(anchor=W, padx=150)

condition4 = Label(window, text="numbers?", image = red, compound='right')
condition4.pack(anchor=W, padx=150)

condition5 = Label(window, text="special characters?", image = red, compound='right')
condition5.pack(anchor=W, padx=150)


window.mainloop()
