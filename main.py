from forms.customer_form import open_customer_form
import tkinter as tk
from config import *

root = tk.Tk()

root.title(APP_NAME)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.configure(bg=BACKGROUND)
root.resizable(False, False)

# ================= عنوان =================

title = tk.Label(
    root,
    text="نرم افزار مدیریت چاپ عبدی",
    font=("Tahoma", 22, "bold"),
    bg=BACKGROUND,
    fg=PRIMARY_COLOR
)
title.pack(pady=20)

version = tk.Label(
    root,
    text="نسخه 2.0",
    font=("Tahoma", 10),
    bg=BACKGROUND
)
version.pack()

# ================= فریم دکمه ها =================

menu = tk.Frame(root, bg=BACKGROUND)
menu.pack(pady=40)

BUTTON_WIDTH = 25
BUTTON_HEIGHT = 2

def not_ready():
    print("در مرحله بعد ساخته می‌شود.")

buttons = [

    ("👤 مدیریت مشتریان"),

    ("🧾 ثبت سفارش"),

    ("📋 سفارش ها"),

    ("📊 گزارش ها"),

    ("⚙️ تنظیمات"),

    ("❌ خروج")

]

for text in buttons:

    if text == "👤 مدیریت مشتریان":

        cmd = open_customer_form
        color = PRIMARY_COLOR

    elif text == "❌ خروج":

        cmd = root.destroy
        color = DANGER_COLOR

    else:

        cmd = not_ready
        color = PRIMARY_COLOR

    tk.Button(

        menu,

        text=text,

        width=BUTTON_WIDTH,

        height=BUTTON_HEIGHT,

        bg=color,

        fg="white",

        font=("Tahoma",11,"bold"),

        command=cmd

    ).pack(pady=8)

root.mainloop()