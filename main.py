from tkinter import *
from tkinter import filedialog
import random

root = Tk()

root.geometry("1000x500")
root.title("RandomChoice")
root.config(bg="#F2B90C")




OUTPUT = []

entryName = Label(root, text="Inputs (',' seperated):")
entryName.config(bg="#F2B90C")
entryName.place(x=30, y=1)

ınputBox = Text(root, height=5, width=70)
ınputBox.place(x=30, y=20)

numBoxName = Label(root, text="Output number:")
numBoxName.config(bg="#F2B90C")
numBoxName.place(x=800, y=20)

outputNumBox = Text(root, height=1, width=5)
outputNumBox.place(x=920, y=20)


def submit():

    entry = ınputBox.get("1.0", "end-1c")
    ınput = entry.split(",")

        
    if cb1Var.get() == 1:
        unInput = []
        unInput.clear()
        for a in ınput:
            if a not in unInput:
                unInput.append(a)

        if cb2Var.get() == 1:
            outputNum = int(outputNumBox.get("1.0", "end-1c"))
            output = random.choices(unInput, k=outputNum)
            OUTPUT.clear()
            OUTPUT.insert(0, output)

        else:
            output = random.choice(unInput)
            OUTPUT.clear()
            OUTPUT.insert(0, output)

    else:
        if cb2Var.get() == 1:
            outputNum = int(outputNumBox.get("1.0", "end-1c"))
            output = random.choices(ınput, k=outputNum)
            OUTPUT.clear()
            OUTPUT.insert(0, output)

        else:
            output = random.choice(ınput)
            OUTPUT.clear()
            OUTPUT.insert(0, output)


        

    OUTPUTList = str(OUTPUT)

    outputLabel.config(text="Output: \t"+OUTPUTList)


cb1 = Checkbutton(root, text="Mode-1")
cb1.config(bg="#F2B90C")
cb1Var = IntVar()
cb1.config(variable=cb1Var)
cb1.config(onvalue=1, offvalue=0)
cb1.place(x=920, y=425)

cb2 = Checkbutton(root, text="Mode-2")
cb2.config(bg="#F2B90C")
cb2Var = IntVar()
cb2.config(variable=cb2Var)
cb2.config(onvalue=1, offvalue=2)
cb2.place(x=920, y=450)

submitBtn = Button(root, text="Submit Input")
submitBtn.config(command=submit)
submitBtn.config(width=15)
submitBtn.place(x=615, y=20)

outputLabel = Label(root)
outputLabel.config(bg="#F2B90C")
outputLabel.place(x=40, y=105)


def reset():
    ınputBox.delete(1.0, END)
    outputNumBox.delete(1.0, END)
    cb1.deselect()
    cb2.deselect()



clearEntriesBtn = Button(root, text="Clear all")
clearEntriesBtn.config(command=reset)
clearEntriesBtn.config(width=15)
clearEntriesBtn.place(x=615, y=50)


def infoWin():
    win = Toplevel()
    win.title("Information Window")
    win.geometry("400x200")

    mode1L = Label(win)
    mode1LTxt = "Mode-1: Filter input against multiple inputs."
    mode1L.config(text=mode1LTxt)
    mode1L.pack()

    mode2L = Label(win)
    mode2LTxt = "Mode-2: Enable multiple outputs."
    mode2L.config(text=mode2LTxt)
    mode2L.pack()

win2Btn = Button(root, text="Info", command=infoWin)
win2Btn.config(width=9)
win2Btn.config(bg="#F2B90C")
win2Btn.config(borderwidth=1)
win2Btn.config(relief=RIDGE)
win2Btn.place(x=920, y=470)

def outputAsFile():

    f = filedialog.asksaveasfile(
        defaultextension = ".txt",
        filetypes = [
            ("Text file", ".txt"),
            ("All files", ".*")
        ]
        )
    f.write(str(OUTPUT)
    f.close()




outputAsFileBtn = Button(root, text="OAF")
outputAsFileBtn.config(command=outputAsFile)
outputAsFileBtn.config(width=15)
outputAsFileBtn.place(x=615, y=80)








root.mainloop()