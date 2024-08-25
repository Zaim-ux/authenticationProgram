import sqlite3
from tkinter import messagebox

connection = sqlite3.connect('userInfo.db')

cursor = connection.cursor()

#method used to insert valid username and password into a database
def databaseInsert(username, password):
    connection = sqlite3.connect('userInfo.db')

    cursor = connection.cursor()
    
    #creates database only if it doesn't exist
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS userInfo(
                    username TEXT NOT NULL PRIMARY KEY, 
                    password BLOB NOT NULL  
                )
                """)

    try:
        # Attempt to insert a new user into the userInfo table
        cursor.execute("""
                    INSERT INTO userInfo (username, password) 
                    VALUES (?, ?)
                    """, (username, password))
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
    cursor.execute("SELECT 1 FROM userInfo WHERE username=?", (username,))
    usernameExists = cursor.fetchone() is not None
    
    cursor.execute("SELECT 1 FROM userInfo WHERE password=?", (password,))
    passwordExists = cursor.fetchone() is not None
    
    #conditions used to inform the user their input attempts already exist in the database
    if (usernameExists):
        messagebox.showerror("Error", "username already exists")
    if (passwordExists):
        messagebox.showerror("Error", "password already exists")
    else:
        cursor.close()
        connection.close()
        return True


    
        
            
                   
                   
                   