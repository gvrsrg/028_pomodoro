from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Countdown", bg=GREEN)
    check_marks.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    marks_count = reps//2
    check_marks.config(text=MARK*marks_count)

    work_sec = WORK_MIN# * 60
    short_break_sec = SHORT_BREAK_MIN# * 60
    long_break_sec = LONG_BREAK_MIN# * 60
    time_sec = 0
    if reps==8:
        reps = 0
        time_sec = long_break_sec
        title_label.config(text="Break", fg=RED)
    else:
        if reps%2==1:
            time_sec = work_sec
            title_label.config(text="WORKING", fg=GREEN)

        else:
            time_sec = short_break_sec
            title_label.config(text="Break", fg=PINK)

    count_down(time_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    minutes = count//60
    seconds = count%60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Countdown", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, borderwidth=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW,  borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()