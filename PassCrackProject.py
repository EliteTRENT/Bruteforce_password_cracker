#Importing modules
import tkinter as tk
from tkinter import messagebox
import string
import itertools

#Creating functions using logic
def generate_characters():
    characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()_-+={[]}<>.?/\\")
    return characters

def search_file():
    target_pass = entry2.get().strip()
    if not target_pass:
        messagebox.showinfo("Error","Target password cannot be empty.")
        return
    
    try:
        max_length = int(entry1.get().strip())
        if max_length <= 0:
            messagebox.showinfo("Error","Max length must be a positive integer.")
            return
    except ValueError:
        messagebox.showinfo("Error","Max length must be a positive integer.")
        return
    try:
        with open("common.txt","r") as file:
            for line in file:
                if line.strip() == target_pass:
                    messagebox.showinfo("",f"Password Found: {target_pass}")
                    return
    except FileNotFoundError:
        messagebox.showerror("Error","The file 'common.txt' is not found.")
        return
    messagebox.showinfo("","Password not found in common.txt. Starting brute force...")
    brute_force(target_pass,max_length)

def brute_force(target_pass, max_length):
    characters = generate_characters()
    for length in range(1, max_length+1):
        for guess in itertools.product(characters, repeat = length):    
            guess_pass = ''.join(guess)
            if guess_pass == target_pass:
                messagebox.showinfo("Success",f"Password found using brute force: {guess_pass}")
                return
    messagebox.showinfo("Failure","Couldn't generate password using brute force.")
    return

#Creating entities of GUI 
root = tk.Tk()
root.title("Brute Force Password Cracker")
root.geometry("400x300")
label1 = tk.Label(root, text="Enter max length: ")
label1.pack(pady=10)
entry1 = tk.Entry(root, justify="center")
entry1.pack()
label2 = tk.Label(root, text="Enter target password: ")
label2.pack(pady=10)
entry2 = tk.Entry(root,justify="center")
entry2.pack()
button = tk.Button(root, text="Crack!", command = search_file)
button.pack(pady=15)
root.mainloop()
