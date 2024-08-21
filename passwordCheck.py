from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import re
from userDatabase import databaseInsert

def submit():
    #retrieves user input into a variable
    password = entry.get()
    
    #iterates through the dictionary and uses regex to check if the user input has met each condition
    #If condition is met then the image in label will change to green tick otherwise red cross
    for key, value in thisdict.items():
        if re.match(value, password):
            key.config(image = green)
        else:
            key.config(image = red)  

    for key in thisdict.keys():
        key.pack()
    
    #sepereate condition made to check if the password is of appropriate length
    if (len(password) >= 8):
        condition1.config(image = green)
    else:
        condition1.config(image=red)
    
    #displays most recent password attempt in currentPassword label
    currentPassword.config(text="current password: " + password)


def save():
    password = entry.get()
    
    #Checks to see if user password meets all conditions to be saved
    if re.match(passwordVerification, password) and (len(password) >= 8):
        savedPassword.config(text="saved password = " + password)
        databaseInsert(password)
 
    else:
        #if conditions aren't met an error pop up will display 
        messagebox.showerror("Error", "Password doesn't meet all requirements")


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

password = entry.get()

#Submit button created on GUI which will call the submit() method
#allows user to enter their chosen password to be verified
submit = Button(window, text="submit", command=submit, padx=30, pady=20, font=20)
submit.pack(side = BOTTOM)

#Save button created on GUI to call the save() method
#allows user the save their password only if ALL conditions are met
save = Button(window, text="save", command=save, padx=30, pady=20, font=20)
save.pack(side = BOTTOM)

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

#Label used to display the users most recent password attempt
currentPassword = Label(window, text="current password: " + password, font=25)
currentPassword.pack()

savedPassword = Label(window, text="saved password: " + password, font=25)
savedPassword.pack()

#Dictionary created to link each condition label with the condition itself
#Will be used to change the image in the label depending on if the condition has been met
thisdict = {
    condition2 : lowercaseCheck,
    condition3 : uppercaseCheck,
    condition4 : numberCheck,
    condition5 : characterCheck
    }


window.mainloop()
