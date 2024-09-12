LOGIN AUTHENTICATION PROGRAM

This project is an experimentation with integrating UI, encryption and databases together. Using a simple GUI users are shown a simple login screen where they are given 3 options:
Submit their details, create a new account or to reset their password. Passwords are encrypted in the databases using methods such as salting and the AES. When passwords are needed
for comparision they are decrypted from the databases using the same methods. Users are required to meet a series of requirements in order to have a valid password (Uppercase letters, 
numbers etc.) otherwise the password will be rejected. I used Visual Studio Code with some extensions that let me view the SQLite database. 

Languages used: Python, SQL
Tools used: Tkinter, Regex, SQLite3, PyCrypto

Installations needed:
pip install pycryptodome
pip install Pillow

To use the program run the loginPage.py file
