# -*- coding: utf-8 -*-
__author__ = 'Dima'
from tkinter import *
from test import *

root = Tk()


def lol():
    root1 = Tk()
    root.withdraw()
    root1.mainloop()
menu = Menu(root)
root.config(menu = menu)

pMenu = Menu(menu)

menu.add_cascade(label = 'добавить',menu=pMenu)

pMenu.add_command(label = "группу",command = lol)
pMenu.add_command(label = "препода")
pMenu.add_command(label = "предметы")
root.mainloop()