#!/usr/bin/env python3

from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from subprocess import Popen
from signal import SIGINT
from time import sleep
from os import path

fossil_repo = "/path/to/myrepo.fossil"
fossil_command = "fossil"
fossil_icon = path.join(path.dirname(__file__), "fossil3.gif")


def showDialog():
    root = Tk()
    root.title("Fossil SCM")

    frame1 = Frame(root, padding=10)
    frame1.grid()

    label1image = PhotoImage(file=fossil_icon)
    label1 = Label(frame1, image=label1image)
    label1.grid(row=0, column=0)

    label2 = Label(frame1, text="Fossil is running",
                   width=20, anchor=W, padding=(20))
    label2.grid(row=0, column=1)

    button1 = Button(frame1, text="Terminate", command=lambda: root.quit())
    button1.grid(row=1, column=0, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    child = Popen([fossil_command, "ui", fossil_repo])
    showDialog()
    child.send_signal(SIGINT)
    sleep(2)  # wait for terminate subprocess.
    child.terminate()
    child.poll()
