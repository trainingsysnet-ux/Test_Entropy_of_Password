import re
from math import log2
import string
from tkinter import *



def entropy():
    password = e.get()
    res = 0
    L = len(password)
    if re.search(f"{[string.ascii_letters]}", password):
        res += len(string.ascii_letters)
    if re.search(f"{[string.digits]}", password):
        res += len(string.ascii_letters)
    if re.search(f"{[string.punctuation]}", password):
        res += len(string.punctuation)
    entropy = log2(res**L)
    lab2.config(text=f"Энтропия пароля {entropy}")


if __name__ == "__main__":
    root = Tk()
    root.title("Проверка энтропии пароля")
    root.resizable(width=False, height=False)
    root.geometry("300x250")
    lab = Label(text="Введите пароль", font=40)
    lab.pack(pady=5)
    e = Entry(root, show='*')
    e.pack(pady=5)
    lab2 = Label(text=f"Энтропия пароля: ")
    lab2.pack(pady=5)
    button = Button(root, text="Проверить пароль", font=40, command=entropy)
    button.pack(side=BOTTOM, pady=40)
    root.mainloop()
    
