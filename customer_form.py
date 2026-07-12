import tkinter as tk
from tkinter import ttk

from config import *


def open_customer_form():

    win = tk.Toplevel()

    win.title("مدیریت مشتریان")

    win.geometry("1000x650")

    win.configure(bg=BACKGROUND)

    # ===================== عنوان =====================

    tk.Label(

        win,

        text="مدیریت مشتریان",

        bg=BACKGROUND,

        fg=PRIMARY_COLOR,

        font=("Tahoma",18,"bold")

    ).pack(pady=15)

    # ===================== فرم =====================

    form = tk.Frame(win,bg=BACKGROUND)

    form.pack(pady=10)

    tk.Label(form,text="نام",bg=BACKGROUND).grid(row=0,column=0,padx=5,pady=5)

    name_entry = tk.Entry(form,width=35)

    name_entry.grid(row=0,column=1)

    tk.Label(form,text="تلفن",bg=BACKGROUND).grid(row=1,column=0,padx=5,pady=5)

    phone_entry = tk.Entry(form,width=35)

    phone_entry.grid(row=1,column=1)

    tk.Label(form,text="آدرس",bg=BACKGROUND).grid(row=2,column=0,padx=5,pady=5)

    address_entry = tk.Entry(form,width=35)

    address_entry.grid(row=2,column=1)

    # ===================== دکمه ها =====================

    buttons = tk.Frame(win,bg=BACKGROUND)

    buttons.pack(pady=15)

    tk.Button(

        buttons,

        text="ثبت",

        width=12,

        bg=SUCCESS_COLOR,

        fg="white"

    ).grid(row=0,column=0,padx=5)

    tk.Button(

        buttons,

        text="ویرایش",

        width=12

    ).grid(row=0,column=1,padx=5)

    tk.Button(

        buttons,

        text="حذف",

        width=12,

        bg=DANGER_COLOR,

        fg="white"

    ).grid(row=0,column=2,padx=5)

    # ===================== جدول =====================

    columns=("name","phone","address")

    tree=ttk.Treeview(

        win,

        columns=columns,

        show="headings",

        height=18

    )

    tree.heading("name",text="نام")

    tree.heading("phone",text="تلفن")

    tree.heading("address",text="آدرس")

    tree.column("name",width=220)

    tree.column("phone",width=180)

    tree.column("address",width=500)

    tree.pack(fill="both",expand=True,padx=15,pady=15)