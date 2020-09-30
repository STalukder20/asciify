# asciify
Program to produce an ascii form of a given image.

## What is it?
The program outputs an ascii character form of a given .jpg or .png image.
A personal project to gain insight as to how ascii art is produced,
and to be able to create ascii art forms of any given image.

## How does it work?
This is a python program that uses the Python Image Library (Pillow) to turn the 
pixels into more useful RGB data. It then uses the data to determine 
which characters best correspond to each pixel, and outputs the mapped result.

## How do I use it?
It is assumed Python 3 is installed. This program was developed in version 3.8.5.
The following modules will be needed:
* Pillow (`> pip install Pillow`)
* Tkinter (should be included with Python)
* NumPy (`> pip install NumPy`)

After the modules are installed, simply run asciify&#46;py, and follow the GUI steps from 
top to bottom. That is, select an image, choose whether to invert, whether to save 
a .txt file containing the ascii form, then convert. The entire image will be converted,
even if the preview does not show it.

### Alternatively:
On a Windows machine, run the 'asciify.exe' executable inside the 'dist' folder.
This will not require any additional installations. Do not modify the 'build' folder.

## Motive 
The intent of this project was to, as previously stated, learn about how these things
that pop up on the internet every now and then are even created, and to be able to create them.
It also helped to understand more about image processing for future projects.