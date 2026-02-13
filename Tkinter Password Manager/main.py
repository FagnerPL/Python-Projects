import json
import os
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "logo.png")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def rand_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_letters = [choice(letters) for _ in range(randint(8, 10))]
    rand_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    rand_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    new_password = rand_symbols + rand_numbers + rand_letters
    shuffle(new_password)

    password_entry.insert(0, f"{"".join(new_password)}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    site = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        site: {
            "email": email,
            "password": password
        }
    }

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty information", message="There are empty fields!")

    else:
        try:
            with open("data.json", mode="r") as file:
                #Read old file
                data = json.load(file)
                #Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                #Creating a new file
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", mode="w") as file:
                #Saving update data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH DATA ------------------------------- #

def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        messagebox.showinfo(website, f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
    except (KeyError, FileNotFoundError):
        messagebox.showinfo("Error", "No Data File Found")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file=IMAGE_PATH)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, pady=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, pady=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, pady=2)

#Entrys
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=51)
email_entry.insert(0, "fagner@email.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

#Buttons
search_button = Button(text="Search", relief="groove", width=14, command=find_password)
search_button.grid(row=1, column=2)

pass_generate = Button(text="Generate Password", relief="groove", command=rand_password)
pass_generate.config(padx=0)
pass_generate.grid(column=2, row=3)

add_button = Button(text="Add", width=43, relief="groove",  command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()