import tkinter as tk
import pandas as pd
import random
from tkinter import messagebox
import pathlib

BACKGROUND_COLOR = "#B1DDC6"
dict_words = {}
rand_word = {}

######################################## ------ Manage Data File ------ ########################################
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/english words.csv")
    dict_words = data.to_dict(orient="records")
else:
    dict_words = data.to_dict(orient="records")


######################################## --- Create New Flash Card ---  ########################################

def next_card():
    global rand_word, timer, data, dict_words
    window.after_cancel(timer)
    try:
        rand_word = random.choice(dict_words)
    except IndexError:
        if messagebox.askyesno(title="Cards Ends", message="You finish all the cards available. Do you want start again?"):
            data = pd.read_csv("data/english words.csv")
            dict_words = data.to_dict(orient="records")
            next_card()
        else:
            file = pathlib.Path("data/words_to_learn.csv")
            if file.exists():
                file.unlink()
                window.quit()
    else:
        canvas.itemconfigure(title, text="English", fill="black")
        canvas.itemconfigure(word, text=rand_word["en_word"], fill="black")
        canvas.itemconfig(back_image, image=card_front)

        timer = window.after(3000, translate_card)

def translate_card():
    canvas.itemconfig(back_image, image=card_back)
    canvas.itemconfigure(title, text="Português", fill="white")
    canvas.itemconfigure(word, text=rand_word["pt_word"], fill="white")


######################################## -Remove and save flash cards-  ########################################

def right_button():
    dict_words.remove(rand_word)
    df = pd.DataFrame(dict_words)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

######################################## Create the User Interface (UI) ########################################
window = tk.Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, translate_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
back_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Buttons
right_img = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=right_img, highlightthickness=0, border=0, text="Right", command=right_button)
known_button.grid(column=1, row= 2)

wrong_img = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=wrong_img, highlightthickness=0, border=0, text="Right", command=next_card)
unknown_button.grid(column=0, row= 2)

next_card()

window.mainloop()