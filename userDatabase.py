import sqlite3
from tkinter import messagebox
from passwordEncryption import decryptPassword
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

connection = sqlite3.connect('userInfo.db')

cursor = connection.cursor()

masterPassword = "Romulus"


#method used to insert valid username and password into a database
def databaseInsert(username, password, salt):
    connection = sqlite3.connect('userInfo.db')

    cursor = connection.cursor()
    
    #creates database only if it doesn't exist
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS userInfo(
                    userID INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL, 
                    password BLOB NOT NULL,
                    salt BLOB NOT NULL
                )
                """)

    try:
        # Attempt to insert a new user into the userInfo table
        cursor.execute("""
                    INSERT INTO userInfo (username, password, salt) 
                    VALUES (?, ?, ?)
                    """, (username, password, salt))
        connection.commit()

    except sqlite3.IntegrityError as e:
        print(f"IntegrityError occurred: {e}")
    
    finally:
        cursor.close()
        connection.close()

    


#method used to check is username or password already exist in database
def uniqueCheck(username, password):
    connection = sqlite3.connect('userInfo.db')
    cursor = connection.cursor()
    
    #Queries are ran to check for a single instance of a username of password existing in a database
    
    #This chunk of code will be used for the "create new password" aspect of the program
    #Mainly it is a test to see if the decryption algorithm works
    #It will check is a user is attempting to use the same password
    
    #first the userID is sourced based on their username
    cursor.execute("SELECT userID FROM userInfo WHERE username=?", (username,))
    userID = cursor.fetchone() 
    if (userID is None):
        return True
    accUserId = userID[0]
    
    #Next the salt used for the encryption algorithm is sourced to be used for the decryption algorithm
    cursor.execute("SELECT salt FROM userInfo WHERE userID=?", (accUserId,))
    passwordSalt = cursor.fetchone()   
    if (passwordSalt is None):
        return True
    #Since the retrived output of the query is a tuple we need to use the first item in that tuple
    sourcePasswordSalt = passwordSalt[0]
    
    #encrypted password is retrieved next
    cursor.execute("SELECT password FROM userInfo WHERE salt=?", (sourcePasswordSalt,))
    encryptedPassword = cursor.fetchone() 
    if (encryptedPassword is None):
        return True
    accpassword = encryptedPassword[0]
    
    #
    plainText = decryptPassword(accpassword, sourcePasswordSalt)
    
    cursor.execute("SELECT 1 username FROM userInfo WHERE username=?", (username,))
    usernameExists = cursor.fetchone() is not None
    
    
    if (password == plainText):
        messagebox.showerror("Error", "password exists")
    if(usernameExists):
        messagebox.showerror("Error", "USERNAME EXISTS")
    #conditions used to inform the user their input attempts already exist in the database
    #if (usernameExists):
        #messagebox.showerror("Error", "username already exists")
    #if (passwordExists):
        #messagebox.showerror("Error", "password already exists")
    else:
        cursor.close()
        connection.close()
        return True


    
        
            
                   
                   
                   