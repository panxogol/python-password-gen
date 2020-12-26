# --- IMPORTS ---
import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# --- CONSTANTS ---
# COLORS
WHITE_BLUE = "#e0fbfc"
LIGHT_BLUE = "#98c1d9"
BLUE = "#3d5a80"
ORANGE = "#ee6c4d"
DARK_BLUE = "#293241"

# Font
LABEL_FONT = "Consolas"
LABEL_FONT_SIZE = 18
LABEL_FONT_STYLE = "normal"
LABEL_FONT_ALIGN = "e"
LABEL_WIDTH = 15

ENTRY_FONT = "Consolas"
ENTRY_FONT_SIZE = 16
ENTRY_FONT_STYLE = "normal"

BUTTON_FONT = "Consolas"
BUTTON_FONT_SIZE = 12
BUTTON_FONT_STYLE = "bold"


# --- FUNCTIONS ---
def main():
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def generate_password():
        # Password Generator Project
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = [random.choice(letters) for _ in range(nr_letters)]
        password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
        password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

        random.shuffle(password_list)

        password = "".join(password_list)

        txt_password.delete(0, tk.END)
        txt_password.insert(0, password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_password():
        website = txt_website.get()
        username = txt_email.get()
        password = txt_password.get()

        if website == "" or username == "" or password == "":
            messagebox.showerror(title="Blank fields", message="Please write some values in the blank fields.")
            if website == "":
                txt_website.focus()
            elif username == "":
                txt_email.focus()
            else:
                txt_password.focus()

        else:
            msgb_title = website
            msgb_message = f"These are the details you have entered\n" \
                           f"Email/Username: {username}\n" \
                           f"Password: {password}\n" \
                           f"Are you sure that you want to save these values?"
            data_is_ok = messagebox.askokcancel(title=msgb_title, message=msgb_message)

            if data_is_ok:
                with open(file="data.txt", mode="a") as file:
                    file.write(f"{website} | {username} | {password}\n")

                txt_website.delete(0, tk.END)
                txt_password.delete(0, tk.END)
                txt_website.focus()

                try:
                    pyperclip.copy(password)
                    messagebox.showinfo(title="Password", message="Yor new password was copied to clipboard")

                except ImportError as err:
                    err_msg = "Your password was saved but not copied to the clipboard. Please check if you" \
                              "have installed the pyperclip package.\n" \
                              f"{err}"
                    messagebox.showerror(title="Error", message=err_msg)

    # ---------------------------- UI SETUP ------------------------------- #
    # --- WINDOW SETUP ---
    window = tk.Tk()
    window.title("Password Gen")
    window.config(padx=100, pady=50, bg=WHITE_BLUE)

    # --- CANVAS ---
    canvas = tk.Canvas(width=200, height=200, highlightthickness=0, bg=WHITE_BLUE)
    img_logo = tk.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=img_logo)
    canvas.grid(row=0, column=1)

    # --- LABELS ---
    lb_website = tk.Label(text="Website:", bg=WHITE_BLUE, fg=DARK_BLUE, anchor=LABEL_FONT_ALIGN)
    lb_website.config(font=(LABEL_FONT, LABEL_FONT_SIZE, LABEL_FONT_STYLE), width=LABEL_WIDTH)
    lb_website.grid(row=1, column=0)

    lb_email = tk.Label(text="Email/Username:", bg=WHITE_BLUE, fg=DARK_BLUE, anchor=LABEL_FONT_ALIGN)
    lb_email.config(font=(LABEL_FONT, LABEL_FONT_SIZE, LABEL_FONT_STYLE), width=LABEL_WIDTH)
    lb_email.grid(row=2, column=0)

    lb_password = tk.Label(text="Password:", bg=WHITE_BLUE, fg=DARK_BLUE, anchor=LABEL_FONT_ALIGN)
    lb_password.config(font=(LABEL_FONT, LABEL_FONT_SIZE, LABEL_FONT_STYLE), width=LABEL_WIDTH)
    lb_password.grid(row=3, column=0)

    # --- ENTRIES ---
    txt_website = tk.Entry(fg=BLUE, width=36)
    txt_website.config(font=(ENTRY_FONT, ENTRY_FONT_SIZE, ENTRY_FONT_STYLE))
    txt_website.grid(row=1, column=1, columnspan=2)
    txt_website.focus()

    txt_email = tk.Entry(fg=BLUE, width=36)
    txt_email.config(font=(ENTRY_FONT, ENTRY_FONT_SIZE, ENTRY_FONT_STYLE))
    txt_email.grid(row=2, column=1, columnspan=2)
    txt_email.insert(tk.END, "your.email@email.com")

    txt_password = tk.Entry(fg=BLUE, width=21)
    txt_password.config(font=(ENTRY_FONT, ENTRY_FONT_SIZE, ENTRY_FONT_STYLE))
    txt_password.grid(row=3, column=1, columnspan=1)

    # --- BUTTONS ---
    btn_generate = tk.Button(text="Generate Password", fg=DARK_BLUE)
    btn_generate.config(font=(BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE), command=generate_password)
    btn_generate.grid(row=3, column=2)

    btn_add = tk.Button(text="Add", fg=DARK_BLUE, width=47)
    btn_add.config(font=(BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE), command=save_password)
    btn_add.grid(row=4, column=1, columnspan=2)

    # --- MAINLOOP ---
    window.mainloop()


# --- RUN ---
if __name__ == '__main__':
    main()
