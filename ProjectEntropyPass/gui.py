from tkinter import *
from check_entropy import entropy
from generate_pass import generator


def GUI_tkinter():
    def update_entropy():
        password = e.get()
        new_value = entropy(password)
        lab2.config(text=f"Password Entropy: {round(new_value, 2)} bits")
    def generate_password():
        new_pass = generator()
        pass_entropy = entropy(new_pass)
        lab3.config(text=f"New password: {new_pass} Entropy: {round(pass_entropy, 2)} bits")
    root = Tk()
    root.title("Password Entropy Check")
    root.resizable(width=False, height=False)
    root.geometry("300x250")
    lab = Label(text="Enter the password", font=40)
    lab.pack(pady=5)
    e = Entry(root, show='*')
    e.pack(pady=5)
    lab2 = Label(text=f"Password Entropy: ")
    lab2.pack(pady=5)
    button = Button(root, text="CHECK", font=40, command=update_entropy)
    button.pack(side=BOTTOM)
    button2 = Button(root, text="Generate Password", font=40, command=generate_password)
    button2.pack(side=BOTTOM)
    lab3 = Label(text=f"New password:   Entropy: ")
    lab3.pack(side=BOTTOM)

    root.mainloop()