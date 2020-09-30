import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from PIL import ImageTk, Image
import functions


class AsciifyGUI:

    def __init__(self):
        self.img_path = None
        self.save_name = None
        self.root = self.create_root()
        self.invert_opt = tk.BooleanVar(master=self.root)
        self.slct_frame = self.create_slct_frame()
        self.file_btn = self.create_file_btn()
        self.invert_chk = self.create_inv_chk()
        self.img_canvas = self.create_img_canv()
        self.conv_btn = self.create_conv_btn()
        self.save_btn = self.create_save_btn()
        self.fname_disp = self.create_fname_disp()

    def create_root(self):
        root = tk.Tk()
        root.wm_title("Asciify")
        # root.wm_iconbitmap("asterisk.ico")
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
        return invert_chk

    def create_img_canv(self):
        canvas = tk.Canvas(self.root, width=300, height=300)
        canvas.grid(row=30, column=10)
        return canvas

    def create_conv_btn(self):
        conv_btn = ttk.Button(self.root, text="CONVERT")
        conv_btn.grid(row=40, column=40)
        conv_btn["command"] = self.conv_btn_click
        return conv_btn

    def create_save_btn(self):
        save_button = ttk.Button(self.root, text="Save")
        save_button["command"] = self.save_btn_click
        save_button.grid(row=30, column=40)
        return save_button

    def create_fname_disp(self):
        file_name = tk.Text(self.root, height=1, width=15)
        file_name.grid(row=33, column=40)
        return file_name

    def slct_btn_click(self):
        file_path = filedialog.askopenfilename(
            parent=self.root, initialdir=os.getcwd(), title="Image")
        if ((file_path[-3:] != "jpg") and (file_path[-3:] != "png")):
            messagebox.showerror("Error", "Please select a JPEG or PNG image.")
            return
        self.img_path = file_path
        img = ImageTk.PhotoImage(Image.open(file_path))
        self.img_canvas.create_image(125, 125, anchor="center", image=img)
        self.img_canvas.mainloop()

    def save_btn_click(self):
        file_name = simpledialog.askstring(
            "Name", prompt="Name the file", parent=self.root)
        self.save_name = file_name
        self.fname_disp.configure(state="normal")
        self.fname_disp.delete("1.0", tk.END)
        self.fname_disp.insert(tk.END, file_name)
        self.fname_disp.configure(state="disabled")

    def conv_btn_click(self):
        save = None
        if (self.save_name != None):
            save = open(self.save_name+".txt", "w")
        ascii_mtrx = functions.all_together(
            self.img_path, invert_=self.invert_opt.get())
        img_window = tk.Tk()
        img_window.wm_title("Converted")
        img_scroll = ttk.Scrollbar(img_window)
        text_box = tk.Text(img_window, height=len(
            ascii_mtrx), width=len(ascii_mtrx[0]))
        text_box.pack(side=tk.LEFT, fill=tk.Y)

        for row in range(len(ascii_mtrx)):
            text_box.configure(state="normal")
            text_box.insert(tk.END, "\n")
            if (save != None):
                save.write("\n")
            line = ""
            for coln in range(len(ascii_mtrx[row])):
                line += ascii_mtrx[row][coln]
            text_box.insert(tk.END, line)
            text_box.configure(state="disabled")
            if (save != None):
                save.write(line)

        img_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        img_scroll.config(command=text_box.yview)
        text_box.config(yscrollcommand=img_scroll.set)

        if (save != None):
            save.close()

        img_window.mainloop()


if __name__ == "__main__":
    main_gui = AsciifyGUI()
    main_gui.root.mainloop()
