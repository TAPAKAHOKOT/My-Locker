from tkinter import Tk, Entry, Label
import sys
from pyautogui import click, moveTo
from time import sleep
 
def exit(event):
    global k, entry

    if entry.get() == "hello": k = True

def gg(event):
    global k
    k = True

def on_closing():
    click(width//2, height//2)
    moveTo(width//2, height//2)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update()
    root.bind('<Escape>', exit)
    # root.bind('<Control-slash>',  gg)
    root.bind('<Control-KeyPress>',  gg)


root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.title("Hello")
root.geometry(str(width) + 'x' + str(height))
root.attributes("-fullscreen", True)

entry = Entry(root, font = 1)
entry.place(width = width//3, height = height//16, x = width//3, y = 15*height//32)

text = "Write password and press Escape"
label = Label(root, text = text, font = 1)
label.place(x = (width//2 - len(text) * 3), y = 13*height//32)

root.update(); sleep(0.2); click(width//2, height//2)

k = False

while k != True: on_closing()
