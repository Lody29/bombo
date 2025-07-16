import tkinter as tk
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

submit = tk.Button(base,text="submit",command =submit_username)
submit.pack(pady = 5)

base.mainloop()
