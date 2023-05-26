#Sourceduty System V1.1
#Copyright (c) 2023, Sourceduty
#This software is free and open-source; anyone can redistribute it and/or modify it.

from tkinter import Tk, Menu
from tkinter import *
from PIL import ImageTk, Image  

# root window
root = Tk()
root.geometry('1000x500')
root.title('Sourceduty System 1.1')

img = Image.open('Background.png')
bg = ImageTk.PhotoImage(img)
label = Label(root, image=bg)
label.place(x = 0,y = 0)

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)
# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='3D printing')
sub_menu.add_command(label='3D models')

# add the File menu to the menubar
file_menu.add_cascade(
    label="3D",
    menu=sub_menu
)
    
# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# add the File menu to the menubar
file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)


menubar.add_cascade(
    label="Design",
    menu=file_menu,
    underline=0
)
# create the Log menu
log_menu = Menu(
    menubar,
    tearoff=0
)

log_menu.add_command(label='Welcome')
log_menu.add_command(label='About...')

menubar.add_cascade(
    label="Games",
    menu=file_menu,
    underline=0
)
# create the Log menu
log_menu = Menu(
    menubar,
    tearoff=0
)

log_menu.add_command(label='Welcome')
log_menu.add_command(label='About...')

# add the Log menu to the menubar
menubar.add_cascade(
    label="Log",
    menu=log_menu,
    underline=0
)
# create the Config menu
config_menu = Menu(
    menubar,
    tearoff=0
)

config_menu.add_command(label='Welcome')
config_menu.add_command(label='About...')

# add the Config menu to the menubar
menubar.add_cascade(
    label="Config",
    menu=config_menu,
    underline=0
)

root.mainloop()
