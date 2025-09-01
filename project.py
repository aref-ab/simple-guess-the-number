from tkinter import *
import random


main = Tk()
main.title("?")
main.geometry("600x500")
main.config(bg="#7717EC")


def on_click_yes():
    lives = 10
    main.destroy()
    game = Tk()
    game.title("Guess the number")
    game.geometry("600x500")
    game.config(bg="#7717EC")
    pic = PhotoImage(file="heart.png")

    heart_lb = Label(game, image=pic, bg="#7717EC")
    heart_lb.place(x=360, y=10)

    lives_lb = Label(game, text=f"You have {lives}", font=(
        "tahoma", 15), bg="#7717EC", fg="white")
    lives_lb.pack(pady=10)
    number = random.randint(1, 100)
    attempts = 0
    btn_exit = Button(game, text="Exit", font=("tahoma", 10),
                      bg="#EC1743", fg="white", padx=5, pady=2,
                      activebackground="#7717EC", foreground="black", border=3, command=game.destroy)
    btn_exit.place(x=550, y=10)

    def check_guess():
        nonlocal attempts
        nonlocal lives
        try:
            if lives <= 0:
                result_lb.config(text=f"Game Over! The number was {number}.")
                entry.config(state='disabled')
                submit_btn.config(state='disabled')
                return
            guess = int(entry.get())
            attempts += 1
            if guess < number:
                result_lb.config(text="Too low! Try again.")
            elif guess > number:
                result_lb.config(text="Too high! Try again.")
            else:
                result_lb.config(
                    text=f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                entry.config(state='disabled')
                submit_btn.config(state='disabled')
            lives -= 1
            lives_lb.config(text=f"You have {lives}")
            entry.delete(0, END)
        except ValueError:
            result_lb.config(text="Please enter a valid number.")

    prompt_lb = Label(game, text="Guess a number between 1 and 100", font=(
        "tahoma", 20), bg="#7717EC", fg="white")
    prompt_lb.pack(pady=20)

    entry = Entry(game, font=("tahoma", 15), width=10)
    entry.pack(pady=10)

    submit_btn = Button(game, text="Submit Guess", font=("tahoma", 15),
                        bg="#17EC77", fg="white", padx=10, pady=5, activebackground="#7717EC", foreground="black", border=5, command=check_guess)
    submit_btn.pack(pady=10)

    result_lb = Label(game, text="", font=(
        "tahoma", 15), bg="#7717EC", fg="white")
    result_lb.pack(pady=20)

    game.mainloop()


def on_click_no():
    main.destroy()


start_lb = Label(main, text="Welcome!\ndo you want to play?", font=(
    "tahoma", 25), bg="#7717EC", fg="white")
start_lb.pack(pady=20)

btn_yes = Button(main, text="Yes", font=("tahoma", 15),
                 bg="#17EC77", fg="white", padx=20, pady=10, activebackground="#7717EC", foreground="black", border=5, command=on_click_yes)
btn_yes.place(x=160, y=250)

btn_no = Button(main, text="No", font=("tahoma", 15),
                bg="#EC1743", fg="white", padx=20, pady=10, activebackground="#7717EC", foreground="black", border=5, command=on_click_no)
btn_no.place(x=360, y=250)


main.mainloop()
