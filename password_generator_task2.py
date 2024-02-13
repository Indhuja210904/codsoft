import random
import string
import tkinter as tk

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    name = name_entry.get()
    password_length = int(length_entry.get())
    
    password = generate_password(password_length)
    
    result_label.config(text=f"Hello {name}, your generated password is: {password}")


app = tk.Tk()
app.title("Password Generator App")
app.configure(bg="#e6e6e6") 


tk.Label(app, text="Enter your name:", bg="#e6e6e6").pack()
name_entry = tk.Entry(app)
name_entry.pack()

tk.Label(app, text="Enter the desired password length:", bg="#e6e6e6").pack()
length_entry = tk.Entry(app)
length_entry.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_and_display_password, bg="#4CAF50", fg="white")
generate_button.pack()

result_label = tk.Label(app, text="", bg="#e6e6e6")
result_label.pack()


app.mainloop()
