from tkinter import *
from PIL import Image, ImageTk
import os
import re

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

window.mainloop()
