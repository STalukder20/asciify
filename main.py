import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
import functions

root = tk.Tk()
slct_frame = ttk.Frame(root)
file_btn = ttk.Button(slct_frame, text="Select Image")
invert_chk = ttk.Checkbutton(
    slct_frame, text="Black-white inversion")


def chk_btn_click() -> None:
    print(invert_chk.state(), type(invert_chk.state()))
    print("selected" in invert_chk.state())


def slct_btn_pressed() -> str:
    file_path = filedialog.askopenfilename(
        parent=root, initialdir=os.getcwd(), title="Image")
    return file_path


root.wm_title("Asciify")
root.wm_iconbitmap("asterisk.ico")

slct_frame.grid(row=50, column=50)

file_btn.grid(row=50, column=50)
file_btn["command"] = slct_btn_pressed

invert_chk.grid(row=100, column=50)
invert_chk["command"] = chk_btn_click

root.mainloop()
