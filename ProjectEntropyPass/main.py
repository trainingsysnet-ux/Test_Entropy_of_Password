from tkinter import *
from check_entropy import entropy

def GUI_tkinter():
    def update_entropy():
        password = e.get()
        new_value = entropy(password)
        lab2.config(text=f"Password Entropy: {round(new_value, 2)} bits")
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
    button.pack(side=BOTTOM, pady=40)


    
    root.mainloop()



if __name__ == "__main__":
    GUI_tkinter()

    
