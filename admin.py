import tkinter as tk
import sqlite3
base = tk.Tk()
base.title("Admin 1loger")
base.geometry("400x200")

#first label
info = tk.Label(base,text = "welcome back admin",font=("arial",14) )
info.pack(pady=10)

#signup
Username = tk.Entry(base,font=("arial",14))
Username.pack(pady=5)

password = tk.Entry(base,font=("arial",14))
password.pack(pady = 5)

def submit_username():
    user = Username.get()
    pw = password.get()
    if user and pw:
        conn = sqlite3.connect("app.db")
        cursor = conn.cursor()

        cursor.execute(
            '''
         CREATE TABLE IF NOT EXISTS admins(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         username TEXT,
         password ,text)
'''
        )
        try:
            cursor.execute(
            'Insert into admins(username , password)values(?,?) ', (user,pw)
            )
            conn.commit
            print("your new user was added")

        except sqlite3.IntegrityError : 
            print("An error occured... tracing error.")
        conn.close()
    else: print("enter a username!!")

submit = tk.Button(base,text="submit",command = submit_username)
submit.pack(pady = 5)

base.mainloop()
