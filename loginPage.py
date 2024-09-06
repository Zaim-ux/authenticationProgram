from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from userDatabase import uniqueCheck
from passwordCheck import openPasswordPage

#the submit button will check if the username and password exists within the database
#via the uniqueCheck method in the userDatabase python file
def submit():
    username = usernameEntry.get()
    password = passwordEntry.get()
    uniqueCheck(username, password, False)

#the forgot password button will take the user to a different window to reset their password
#which gets updated and encrypted into the database
def forgotPassword():
    openPasswordPage(window, True)

#the new user button will take the user to a page where they can enter a username and
#password and be added onto the database
def newUser():
    openPasswordPage(window, False)
    
    

#Basic tkinter window made with user input fields for username, password and
#buttons depending on what the user wants to do
script_dir = os.path.dirname(__file__)
window = Tk()
window.geometry("420x400")
window.resizable(0, 0)
zPath = os.path.join(script_dir, 'zIcon.jpg')
zIcon = Image.open(zPath)
image = ImageTk.PhotoImage(zIcon)
window.wm_iconphoto(False, image)
window.title("passwordVerifier")

usernameEntry = Entry()
usernameEntry.config(font = 25)
usernameEntry.insert(0, "username")
usernameEntry.pack()

username = usernameEntry.get()

passwordEntry = Entry()
passwordEntry.config(font= 25)
passwordEntry.insert(0, "password")
passwordEntry.pack()

password = passwordEntry.get()

submit = Button(window, text="submit", command=submit, padx=30, pady=20, font=20)
submit.pack()

newUser = Button(window, text="create new account?", command=newUser, padx=30, pady=20, font=20)
newUser.pack()

forgotPassword = Button(window, text="forgot password?", command=forgotPassword, padx=30, pady=20, font=20)
forgotPassword.pack()

window.mainloop()