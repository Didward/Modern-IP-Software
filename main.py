# Modules
import tkinter
import customtkinter
import requests
import json
import pyperclip
from tkinter import ANCHOR, messagebox
import tkintermapview

# I don't think I need to explain this
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Creating the app and customising it
app = customtkinter.CTk()
app.title("IP")
app.geometry("400x200")
app.resizable(False, False)

# This label is no where to be found on the app...
textbox = customtkinter.CTkEntry(app, text="Hello World!")
textbox.pack(side=tkinter.TOP)

# The function that gets the ip
def on_click():
    ip_address = requests.get("https://api.ipify.org").text # I used ipify's api for this
    textbox.delete(0, tkinter.END) # Deleted everything already in the text box
    textbox.insert(0, ip_address) # Inserted the text

# Creating a button and placing it near the middle of the window
button = customtkinter.CTkButton(app, text="Get IP", command=on_click)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# I just used the api again and used pyperclip to just copy it
def copy_to_clipboard():
    ip_address = requests.get("https://api.ipify.org").text # I already said this bruh
    pyperclip.copy(ip_address)# Copies to clipboard

    # send a notification
    messagebox.showinfo("IP Copied", "IP address copied to clipboard")

# This thing is the copy button
copy_button = customtkinter.CTkButton(
    app, text="Copy IP", command=copy_to_clipboard)
copy_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

# The loop thing
app.mainloop()
