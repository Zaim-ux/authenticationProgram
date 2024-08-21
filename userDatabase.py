import sqlite3

connection = sqlite3.connect('userInfo.db')

cursor = connection.cursor()

def databaseInsert(password):
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS userInfo(
                    username TEXT NOT NULL PRIMARY KEY, 
                    password TEXT NOT NULL  
                )
                """)

    try:
        # Attempt to insert a new user into the userInfo table
        cursor.execute("""
                    INSERT INTO userInfo (username, password) 
                    VALUES (?, ?)
                    """, ('Wiliam', password))

    except sqlite3.IntegrityError as e:
        print(f"IntegrityError occurred: {e}")

    cursor.execute("""
                SELECT * FROM userInfo
                """)

    connection.commit()
    connection.close()