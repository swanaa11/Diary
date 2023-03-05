from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from datetime import *
from PIL import ImageTk, Image
from colorama import Fore
import json
import pandas as pd
import csv
from csv import DictWriter


bg = '#BABABA'
date = date.today()

window = Tk()
window.title("Diary")
window.geometry('350x450')
window.maxsize(350, 450)
window.minsize(350, 450)
window.config(bg=bg)
window.iconbitmap('expense.ico')
today = date.today()


def clear():
    rs_entry_gain.delete(0, END)
    rs_entry_loss.delete(0, END)
    text_entry.delete(0, END)


def store_data():
    heading = ["Date", "Receive", "Spent", "Text"]
    _data = {"Date": today, "Receive": rs_entry_gain.get(), "Spent": rs_entry_loss.get(), "Text": text_entry.get()}

    with open("data.csv", 'a') as data_file:
        writer = DictWriter(data_file, fieldnames=heading)
        writer.writerow(_data)
        data_file.close()

    file = pd.read_csv('data.csv')
    file.to_csv('data.csv', header=heading, index=False)
    clear()


def amount():

    if rs_entry_gain.get().isdigit() & rs_entry_loss.get().isdigit():
        # print('+'+Fore.GREEN+gain, '-'+Fore.RED+loss, Fore.YELLOW+_text)
        store_data()

    elif rs_entry_gain.get().isdigit():
        # print('+' + Fore.GREEN + gain, Fore.YELLOW + _text)
        store_data()

    elif rs_entry_loss.get().isdigit():
        # print('-'+Fore.RED+loss, Fore.YELLOW+_text)
        store_data()

    else:
        messagebox.showinfo(title='Error', message='Enter valid number')
        clear()


def statement():
    root = Tk()
    root.title("Diary")
    root.geometry('350x450')
    root.maxsize(350, 450)
    root.minsize(350, 450)
    root.iconbitmap('expense.ico')

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Date", "Receive", "Spent", "Text"), height=400, selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    # scrollbarx.config(command=tree.xview)
    # scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Date', text="Date", anchor=W)
    tree.heading('Receive', text="Receive", anchor=W)
    tree.heading('Spent', text="Spent", anchor=W)
    tree.heading('Text', text="Text", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=65)
    tree.column('#3', stretch=NO, minwidth=0, width=65)
    tree.column('#4', stretch=NO, minwidth=0, width=150)
    tree.pack()

    with open('data.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            _date = row['Date']
            _receive = row['Receive']
            _spent = row['Spent']
            __text = row['Text']
            tree.insert("", 0, values=(_date, _receive, _spent, __text))

    root.mainloop()


logo = Image.open('logo.png')
resized_logo = logo.resize((100, 100))
logo = ImageTk.PhotoImage(resized_logo)
logo_label = Label(window, image=logo)
logo_label.pack()
logo_label.config(bg=bg)

date = Label(text=f"{today}", bg=bg, fg="black")
date.pack()
date.config(font=('prospekt', 24))

rs_entry_gain = Label(text="Received Amount : ", bg=bg, fg="black")
rs_entry_gain.pack(pady=5)
rs_entry_gain.config(font=('robot', 12))
rs_entry_gain = Entry(width=30)
rs_entry_gain.pack(pady=5)

rs_entry_loss = Label(text="Spent Amount : ", bg=bg, fg="black")
rs_entry_loss.pack(pady=5)
rs_entry_loss.config(font=('robot', 12))
rs_entry_loss = Entry(width=30)
rs_entry_loss.pack(pady=5)

text = Label(text="Text : ", bg=bg, fg="black")
text.pack(pady=5)
text.config(font=('robot', 12))
text_entry = Entry(width=30)
text_entry.pack()

search = Button(text="Submit", bg="black", fg="white", width=25, command=amount)
search.pack(pady=20)

cal_button = Button(text="Statement", width=25, bg="black", fg="white", command=statement)
cal_button.pack(padx=10)

window.mainloop()

# df = pd.read_csv('data.csv')
# print(df)

