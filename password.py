from tkinter import *
import re

def check_password():

    password = txt_password.get()
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Password should contain at least 8 characters.")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add at least one uppercase letter.")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("• Add at least one lowercase letter.")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("• Add at least one number.")

    if re.search("[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("• Add at least one special character.")

    if score == 5:
        result.config(text="🟢 Password Strength : Strong", fg="green")
    elif score >= 3:
        result.config(text="🟠 Password Strength : Medium", fg="orange")
    else:
        result.config(text="🔴 Password Strength : Weak", fg="red")

    if feedback:
        suggestion.config(text="\n".join(feedback), fg="blue")
    else:
        suggestion.config(
            text="✓ Excellent! Your password satisfies all the requirements.",
            fg="green"
        )


def show_password():

    if show.get():
        txt_password.config(show="")
    else:
        txt_password.config(show="*")


def clear_data():

    txt_password.delete(0, END)
    result.config(text="")
    suggestion.config(text="")
    show.set(0)
    txt_password.config(show="*")
    txt_password.focus()


# ---------------- Main Window ---------------- #

win = Tk()
win.title("Password Strength Checker")
win.geometry("560x400")
win.config(bg="aliceblue")
win.resizable(False, False)

Label(
    win,
    text="🔐 Password Strength Checker",
    font=("Arial",18,"bold"),
    bg="aliceblue",
    fg="navy"
).pack(pady=(15,5))

Label(
    win,
    text="Check the strength of your password",
    font=("Arial",10),
    bg="aliceblue",
    fg="gray"
).pack()

Label(
    win,
    text="Enter Password",
    font=("Arial",11,"bold"),
    bg="aliceblue"
).pack(pady=(20,5))

txt_password = Entry(
    win,
    width=35,
    font=("Arial",12),
    show="*",
    bd=2
)
txt_password.pack()

show = IntVar()

Checkbutton(
    win,
    text="Show Password",
    variable=show,
    command=show_password,
    bg="aliceblue",
    font=("Arial",10)
).pack(pady=5)

button_frame = Frame(win, bg="aliceblue")
button_frame.pack(pady=10)

Button(
    button_frame,
    text="Check Password",
    command=check_password,
    bg="royalblue",
    fg="white",
    font=("Arial",10,"bold"),
    width=16
).grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="Clear",
    command=clear_data,
    bg="gray",
    fg="white",
    font=("Arial",10,"bold"),
    width=16
).grid(row=0, column=1, padx=10)

result = Label(
    win,
    text="",
    font=("Arial",12,"bold"),
    bg="aliceblue"
)
result.pack(pady=10)

Label(
    win,
    text="Suggestions",
    font=("Arial",11,"bold"),
    bg="aliceblue",
    fg="navy"
).pack()

suggestion = Label(
    win,
    text="",
    justify=LEFT,
    anchor="nw",
    bg="white",
    width=55,
    height=6,
    relief=SOLID,
    bd=1,
    wraplength=450,
    padx=10,
    pady=10,
    font=("Arial",10)
)
suggestion.pack(pady=10)

win.bind("<Return>", lambda event: check_password())

txt_password.focus()

win.mainloop()