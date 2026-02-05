from tkinter import *
from check_entropy import entropy
from generate_pass import generator


def GUI_tkinter():

    corrent_password = ""

    def update_entropy():
        password = e.get()
        new_value = entropy(password)
        lab2.config(text=f"Password Entropy: {round(new_value, 2)} bits")
    
    def generate_password():
        new_pass = generator()
        nonlocal corrent_password
        corrent_password = new_pass
        pass_entropy = entropy(new_pass)
        lab3.config(text=f"New password: {new_pass} Entropy: {round(pass_entropy, 2)} bits")
        
        
    
    def copy_to_clipboard():
        
        root.clipboard_clear()
        root.clipboard_append(corrent_password)
        print("Copy complete!")

    root = Tk()

    # X and Y center monitor
    screen_width = root.winfo_screenwidth()  
    screen_height = root.winfo_screenheight()
    window_width = 500
    window_height = 350
    x = (screen_width // 2) - (window_width // 2)  
    y = (screen_height // 2) - (window_height // 2) 
    
    root.title("Password Entropy Check")
    root.resizable(width=False, height=False)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    lab = Label(text="Enter the password", font=40)
    lab.pack(pady=5)

    e = Entry(root, show='*')
    e.pack(pady=5)

    lab2 = Label(text=f"Password Entropy: ")
    lab2.pack(pady=5)

    button = Button(root, text="CHECK", font=40, command=update_entropy)
    button.pack()

    
    # Button for copy
    button_copy = Button(root, text=f"Copy to clipboard", command=copy_to_clipboard)
    button_copy.pack(side=BOTTOM, pady=10)

    # Button for generate
    button_generate = Button(root, text="Generate Password", font=40, command=generate_password)
    button_generate.pack(side=BOTTOM, pady=20)

    # Label to generated password
    lab3 = Label(text=f"Create a new password for you! :)")
    lab3.pack(side=BOTTOM)



    root.mainloop()