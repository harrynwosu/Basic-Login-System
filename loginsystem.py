from tkinter import Tk, Button, Frame
from tkinter import simpledialog
from tkinter import messagebox

cred = {} #Dictionary that contains the login details of all users

root = Tk()
root.withdraw() #removes window from the screen without destroying it


def user():
    """Creates a dialog box that asks if the user is a new user
       Creates a new account if the new user wishes to do so
    """
    response = messagebox.askyesno(title="New User?", message="Do you have an account?")
    if response == True:
        login()
    else:
        res = messagebox.askyesno(title="New Account", message="Create a new account?")
        if res == True: #Create new account if user wishes
            create_account()
            login()
        else:
            pass

def login():
    """Prompts an existing user for a username and password"""
    username = simpledialog.askstring(title="Login", prompt="Username:")
    password = simpledialog.askstring(title="Login", prompt="Password:")
    if username in cred:
        if cred[username] == password:
            messagebox.showinfo(title="Login", message="Login successful")
    else:
        resp = messagebox.askretrycancel(title="Login", message="Incorrect login details!")
        if resp == True:
            login()
        else:
            pass


def create_account():
    """Prompts user to create a new account with user details
       User details are stored in the users' credentials dictionary
    """
    username = simpledialog.askstring(title="Username", prompt="Enter your username:")
    password = simpledialog.askstring(title="Password", prompt="Enter a password:")
    conf_password = simpledialog.askstring(title="Confirm Password", prompt="Confirm password:")
    #Original password must match with confirmed password for a successul account creation
    if conf_password != password:
        resp = messagebox.askretrycancel(title="Login", message="Passwords don't match")
        if resp == True:
            create_account()
        else:
            pass
    else:
        cred[username] = password
        login()

root.geometry('100x100')
 
def run_program(): 
    try:  
        Button(root, text='Login', command=login).pack()
        Button(root, text='New User', command=user).pack()
    except Exception: #Catches any exceptions that arise during the program execution
        messagebox.showwarning(title="Error", message="There was an error in your login!")

if __name__ == "__main__": 
    root = Tk()
    run_program()
    root.mainloop()


