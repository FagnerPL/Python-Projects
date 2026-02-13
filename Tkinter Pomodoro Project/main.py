from tkinter import *
import math
import os

# ---------------------------- CONSTANTS ------------------------------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "tomato.png") 

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    main_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps += 1
    print(reps)

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        main_label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        main_label.config(text="BREAK", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        main_label.config(text="TIMER", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        checks = ""
        for _ in range(math.floor(reps / 2)):
            checks += "✓"
            check_label.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=IMAGE_PATH)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
print(os.getcwd())

#Labels
main_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
main_label.grid(column=1, row=0)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=3)

#Buttons
start_button = Button(text="Start", width=5, font=(FONT_NAME, 10, "bold"), command=start_time)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=5,font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()