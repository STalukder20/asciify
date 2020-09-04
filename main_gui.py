import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from PIL import ImageTk, Image
import functions


class AsciifyGUI:

    def __init__(self):
        self.root = self.create_root()
        self.invert_opt = tk.BooleanVar(master=self.root)
        self.slct_frame = self.create_slct_frame()
        self.file_btn = self.create_file_btn()
        self.invert_chk = self.create_inv_chk()
        self.img_canvas = self.create_img_canv()

    def create_root(self):
        root = tk.Tk()
        root.wm_title("Asciify")
        root.wm_iconbitmap("asterisk.ico")
        return root

    def create_slct_frame(self):
        slct_frame = ttk.Frame(self.root)
        slct_frame.grid(row=25, column=25)
        return slct_frame

    def create_file_btn(self):
        file_btn = ttk.Button(self.slct_frame, text="Select Image")
        file_btn.grid(row=50, column=50)
        file_btn["command"] = self.slct_btn_pressed
        return file_btn

    def create_inv_chk(self):
        invert_chk = ttk.Checkbutton(
            self.slct_frame, text="Black-White Inversion", var=self.invert_opt)
        invert_chk.grid(row=100, column=50)
        invert_chk["command"] = self.chk_btn_click
        print("initial state invert", self.invert_opt.get())
        return invert_chk

    def create_img_canv(self):
        canvas = tk.Canvas(self.root, width=300, height=300)
        canvas.grid(row=30, column=10)
        return canvas

    def chk_btn_click(self):
        print("chk_btn_click, invert_opt:", self.invert_opt.get())
        print("invert_chk state, type", self.invert_chk.state(),
              type(self.invert_chk.state()))
        print("selected" in self.invert_chk.state())

    def slct_btn_pressed(self):
        file_path = filedialog.askopenfilename(
            parent=self.root, initialdir=os.getcwd(), title="Image")
        print(file_path)
        img = ImageTk.PhotoImage(Image.open(file_path))
        self.img_canvas.create_image(20, 20, anchor="center", image=img)
        self.img_canvas.mainloop()


if __name__ == "__main__":
    main_gui = AsciifyGUI()
    main_gui.root.mainloop()
