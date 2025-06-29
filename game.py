import tkinter as tk
import random
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x250")
secret_number = random.randint(1, 100)
tries = 0


def check_guess():
    global tries
    try:
        user_guess = int(entry.get())
        tries += 1
        if user_guess < secret_number:
            result_label.config(text="too low!!")
        elif user_guess > secret_number:
            result_label.config(text="too high!!")
        else:
            result_label.config(text=f"correct in {tries} tries")
            submit_btn.config(state="disabled")
            play_again_btn.config(state="normal")
    except ValueError:
        result_label.config(text="please enter the valid number")


def play_agian():
    global secret_number, tries
    secret_number = random.randint(1, 100)
    tries = 0
    entry.delete(0, tk.END)
    result_label.config(text="")
    submit_btn.config(state="normal")
    play_again_btn.config(state="disabled")


# create GUI elements
# instruction
tk.Label(root, text="guess a number(1-100):").pack(pady=10)
# inut box
entry = tk.Entry(root)
entry.pack(pady=5)
# submit button
submit_btn = tk.Button(root, text="submit", command=check_guess)
submit_btn.pack(pady=5)
# label to show result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
# play again button
play_again_btn = tk.Button(root, text="play agian", command=play_agian)
play_again_btn.pack(pady=5)
play_again_btn.config(state="disabled")
# start the app
root.mainloop()
