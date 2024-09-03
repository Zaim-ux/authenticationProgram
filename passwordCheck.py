from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import re
from userDatabase import databaseInsert, uniqueCheck, usernameCheck, updateUserPassword
from passwordEncryption import encryptPassword
def openPasswordPage(oldWindow, resetTrue):

#Remodelled the entire file to be stored within a method so that the page can be opened 
#when button is pressed on seperate window
    def test():
        #retrieves user input to store username
        username = usernameEntry.get()
        
        #retrieves user input to store password
        password = passwordEntry.get()
        
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
        
        #checks if username or password already exist in database
        uniqueCheck(username, password, resetTrue)
        
        #displays most recent password attempt in currentPassword label
        currentPassword.config(text="current password: " + password)

    def save():
        username = usernameEntry.get()
        password = passwordEntry.get()
        
        #Checks to see if user password meets all conditions to be saved
        if re.match(passwordVerification, password) and (len(password) >= 8) and usernameCheck(username):
            savedPassword.config(text="saved password = " + password)
            #saves both username and password to the database
            passwordSalt, newPassword = encryptPassword(password)
            
            databaseInsert(username, newPassword, passwordSalt)
    
        else:
            #if conditions aren't met an error pop up will display 
            messagebox.showerror("Error", "Please try another username")

    def updatePassword():
        username = usernameEntry.get()
        password = passwordEntry.get()
        
        #Checks to see if user password meets all conditions to be saved
        if re.match(passwordVerification, password) and (len(password) >= 8):
            savedPassword.config(text="saved password = " + password)
            #saves both username and password to the database
            passwordSalt, newPassword = encryptPassword(password)
            
            updateUserPassword(username, newPassword, passwordSalt)
            

    #conditions made to see if inputted password meets requirements
    lowercaseCheck = r'^(?=.*[a-z])'
    uppercaseCheck = r'^(?=.*[A-Z])'
    numberCheck = r'^(?=.*\d)'
    characterCheck = r'^(?=.*[@$!%*?&])'

    #this variable will check if the inputted password meets all requirements
    passwordVerification = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])'

    #Retrieves the file path for the image needed
    script_dir = os.path.dirname(__file__)
    
    #Green tick image created to indicate a condition has been met on GUI
    greenPath = os.path.join(script_dir, 'greenTick.png')
    
    #Red cross image created to indicate a condition hasn't been met on GUI
    redPath = os.path.join(script_dir, 'redX.png')
    
    green = ImageTk.PhotoImage(Image.open(greenPath).resize((20, 20)))
    red = ImageTk.PhotoImage(Image.open(redPath).resize((20, 20)))
    
    
    #window is created and icon is customised 
    passwordWindow = Toplevel(oldWindow)
    passwordWindow.geometry("420x400")
    passwordWindow.resizable(0, 0)
    zPath = os.path.join(script_dir, 'zIcon.jpg')
    zIcon = Image.open(zPath)
    image = ImageTk.PhotoImage(zIcon)
    #window.wm_iconphoto(False, image)
    passwordWindow.title("passwordVerifier")

    #input button created for user to enter username
    usernameEntry = Entry(passwordWindow)
    usernameEntry.config(font = 25)
    usernameEntry.insert(0, "username")
    usernameEntry.pack()

    username = usernameEntry.get()

    #input button created for user to enter password
    passwordEntry = Entry(passwordWindow)
    passwordEntry.config(font= 25)
    passwordEntry.insert(0, "password")
    passwordEntry.pack()

    password = passwordEntry.get()


    #Submit button created on GUI which will call the submit() method
    #allows user to enter their chosen password to be verified
    test = Button(passwordWindow, text="test password", command=test, padx=30, pady=20, font=20)
    test.pack(side = BOTTOM)

    #Save button created on GUI to call the save() method
    #allows user the save their password only if ALL conditions are met
    save = Button(passwordWindow, text="Update Database", command=save, padx=30, pady=20, font=20)
    save.pack(side = BOTTOM)

    #if the reset password page is called then remove the save button and replace with the
    #replace password button that has different functionality 
    if (resetTrue):
        save.pack_forget()
        reset = Button(passwordWindow, text="Update Password", command=updatePassword, padx=30, pady=20, font=20)
        reset.pack(side=BOTTOM)

    #Labels created to show the user which conditions are required for their password as well as
    #if the condition has been met with an image
    condition1 = Label(passwordWindow, text="8 characters long?", image=red, compound='right')
    condition1.pack(anchor=W, padx=150)

    condition2 = Label(passwordWindow, text="lowercase letters?", image=red, compound='right')
    condition2.pack(anchor=W, padx=150)

    condition3 = Label(passwordWindow, text="uppercase?", image = red, compound='right')
    condition3.pack(anchor=W, padx=150)

    condition4 = Label(passwordWindow, text="numbers?", image = red, compound='right')
    condition4.pack(anchor=W, padx=150)

    condition5 = Label(passwordWindow, text="special characters?", image = red, compound='right')
    condition5.pack(anchor=W, padx=150)

    #Label used to display the users most recent password attempt
    currentPassword = Label(passwordWindow, text="current password: " + password, font=25)
    currentPassword.pack()

    savedPassword = Label(passwordWindow, text="saved password: " + password, font=25)
    savedPassword.pack()

    #Dictionary created to link each condition label with the condition itself
    #Will be used to change the image in the label depending on if the condition has been met
    thisdict = {
        condition2 : lowercaseCheck,
        condition3 : uppercaseCheck,
        condition4 : numberCheck,
        condition5 : characterCheck
        }


    passwordWindow.mainloop()
