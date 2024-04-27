import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
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
    reps = 0
    window.after_cancel(timer)
    title_text.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_time = WORK_MIN * 60
    # if it's even rep
    short_break = SHORT_BREAK_MIN * 60
    # if it's 8 rep
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_text.config(text="Long Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        title_text.config(text="Short Break", fg=PINK)
        count_down(short_break)
    else:
        title_text.config(text="Work Time", fg=GREEN)
        count_down(work_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            checkmarks.config(text={"✔" * reps / 2})
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pymodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_text = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
title_text.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
pomo_img = tk.PhotoImage(file="day22-30/day28/tomato.png")
canvas.create_image(100, 112, image=pomo_img)
timer_text = canvas.create_text(
    100, 138, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

start_butt = tk.Button(text="Start", command=start_timer)
start_butt.grid(row=2, column=0)

checkmarks = tk.Label(bg=YELLOW, fg=GREEN)
checkmarks.grid(row=3, column=1)

reset_butt = tk.Button(text="Reset", command=reset_timer)
reset_butt.grid(row=2, column=2)


window.mainloop()
