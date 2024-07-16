from tkinter import *
from tkinter import messagebox, filedialog
import os


def createWidgets():
    global textArea

    textArea = Text(root)
    textArea.grid(sticky=N + S + W + E)

    menuBar = Menu(root)
    root.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=exitApp)
    menuBar.add_cascade(label="File", menu=fileMenu)


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)


def openFile():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        with open(file, "r") as f:
            textArea.insert(1.0, f.read())


def saveFile():
    global file
    if file is None:
        file = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(textArea.get(1.0, END))
            root.title(os.path.basename(file) + " - Notepad")
    else:
        with open(file, "w") as f:
            f.write(textArea.get(1.0, END))


def exitApp():
    root.quit()


root = Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")

file = None

createWidgets()

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
