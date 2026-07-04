from tkinter import *
import re

def check_password():
    password = entry.get()
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Minimum 8 characters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add an uppercase letter")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("• Add a lowercase letter")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("• Add a number")

    if re.search("[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("• Add a special character")

    if score == 5:
        result.config(text="🟢 Strong Password", fg="green")
    elif score >= 3:
        result.config(text="🟠 Medium Password", fg="orange")
    else:
        result.config(text="🔴 Weak Password", fg="red")

    if feedback:
        suggest.config(text="\n".join(feedback), fg="black")
    else:
        suggest.config(text="✓ Excellent! Your password is secure.", fg="green")


def show_password():
    entry.config(show="" if show.get() else "*")


def clear():
    entry.delete(0, END)
    show.set(0)
    entry.config(show="*")
    result.config(text="")
    suggest.config(text="")
    entry.focus()


win = Tk()
win.title("Password Complexity Checker")
win.geometry("500x420")
win.config(bg="lightgray")
win.resizable(False, False)

Label(win,
      text="🔐 Password Complexity Checker",
      font=("Arial",18,"bold"),
      bg="lightgray",
      fg="navy").pack(pady=10)

Label(win,
      text="Check how secure your password is",
      bg="lightgray",
      fg="gray").pack()

card = Frame(win, bg="white", bd=3, relief=RIDGE)
card.pack(pady=20, padx=20, fill="both")

Label(card,
      text="Enter Password",
      bg="white",
      font=("Arial",11,"bold")).pack(pady=(15,5))

entry = Entry(card, width=30, font=("Arial",12), show="*")
entry.pack()

show = IntVar()

Checkbutton(card,
            text="Show Password",
            variable=show,
            command=show_password,
            bg="white").pack(anchor="w", padx=50, pady=5)

Frame(card, bg="white").pack()

Button(card,
       text="Analyze Password",
       command=check_password,
       bg="royalblue",
       fg="white",
       width=18).pack(pady=5)

Button(card,
       text="Clear",
       command=clear,
       bg="gray",
       fg="white",
       width=18).pack()

result = Label(card,
               text="",
               bg="white",
               font=("Arial",12,"bold"))
result.pack(pady=10)

Label(card,
      text="Suggestions",
      bg="white",
      fg="navy",
      font=("Arial",11,"bold")).pack()

suggest = Label(card,
                text="",
                bg="white",
                justify=LEFT,
                wraplength=350)
suggest.pack(pady=(5,15))

win.bind("<Return>", lambda event: check_password())
entry.focus()

win.mainloop()