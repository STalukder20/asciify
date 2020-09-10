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
        self.img_path = "None"
        self.conv_btn = self.create_conv_btn()

    def create_root(self):
        root = tk.Tk()
        root.wm_title("Asciify")
        root.wm_iconbitmap("asterisk.ico")
        return root

    def create_slct_frame(self):
        slct_frame = ttk.Frame(self.root)
        slct_frame.grid(row=25, column=40)
        return slct_frame

    def create_file_btn(self):
        file_btn = ttk.Button(self.slct_frame, text="Select Image")
        file_btn.grid(row=0, column=0)
        file_btn["command"] = self.slct_btn_click
        return file_btn

    def create_inv_chk(self):
        invert_chk = ttk.Checkbutton(
            self.slct_frame, text="Black-White Inversion", var=self.invert_opt)
        invert_chk.grid(row=10, column=0)
        invert_chk["command"] = self.chk_btn_click
        print("initial state invert", self.invert_opt.get())
        return invert_chk

    def create_img_canv(self):
        canvas = tk.Canvas(self.root, width=300, height=300)
        canvas.grid(row=30, column=10)
        return canvas

    def create_conv_btn(self):
        conv_btn = ttk.Button(self.root, text="CONVERT")
        conv_btn.grid(row=30, column=40)
        conv_btn["command"] = self.conv_btn_click
        return conv_btn

    def chk_btn_click(self):
        print("chk_btn_click, invert_opt:", self.invert_opt.get())
        print("invert_chk state, type", self.invert_chk.state(),
              type(self.invert_chk.state()))
        print("selected" in self.invert_chk.state())

    def slct_btn_click(self):
        file_path = filedialog.askopenfilename(
            parent=self.root, initialdir=os.getcwd(), title="Image")
        self.img_path = file_path
        img = ImageTk.PhotoImage(Image.open(file_path))
        self.img_canvas.create_image(125, 125, anchor="center", image=img)
        self.img_canvas.mainloop()

    def conv_btn_click(self):
        save = open("newfile.txt", "w")
        ascii_mtrx = functions.all_together(
            self.img_path, invert_=self.invert_opt.get())
        functions.print_ascii_matrix(ascii_mtrx)
        img_window = tk.Tk()
        img_window.wm_title("Converted")
        img_scroll = ttk.Scrollbar(img_window)
        text_box = tk.Text(img_window, height=len(
            ascii_mtrx), width=len(ascii_mtrx[0]))
        text_box.pack(side=tk.LEFT, fill=tk.Y)

        for row in range(len(ascii_mtrx)):
            text_box.insert(tk.END, "\n")
            save.write("\n")
            line = ""
            for coln in range(len(ascii_mtrx[row])):
                line += ascii_mtrx[row][coln]
            text_box.insert(tk.END, line)
            save.write(line)

        img_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        img_scroll.config(command=text_box.yview)
        text_box.config(yscrollcommand=img_scroll.set)

        save.close()

        img_window.mainloop()


if __name__ == "__main__":
    main_gui = AsciifyGUI()
    main_gui.root.mainloop()
