from tkinter import *
from tkinter import filedialog
import random
import os


root = Tk()

root.geometry("1000x500")
root.title("RandomChoice")
root.config(bg="#F2B90C")


INPUTLEN = []
WEIGHTLEN = []
OUTPUT = []
WIPDATA = []

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

    ınWeightSubmit()

    entry = ınputBox.get("1.0", "end-1c")
    ınput = entry.split(",")

    lenInput = len(ınput)
    INPUTLEN.clear()
    INPUTLEN.insert(0, lenInput)

    #Zero's required
    def ZERR():
        ınlen = str(INPUTLEN)
        ınlen = ınlen.replace("[", "")
        ınlen = ınlen.replace("]", "")
        ınlen = ınlen.replace("'", "")
        ınlen = ınlen.replace(" ", "")
        
        welen = str(WEIGHTLEN)
        welen = welen.replace("[", "")
        welen = welen.replace("]", "")
        welen = welen.replace("'", "")
        welen = welen.replace(" ", "")

        try:
            i = int(ınlen) - int(welen)

            if i < 0:
                print("Weight's can't be more than ınputs!")

            else:
                wıpData = str(WIPDATA)
                wıpData = wıpData.replace("[", "")
                wıpData = wıpData.replace("]", "")
                wıpData = wıpData.replace("'", "")
                wıpData = wıpData.replace(" ", "")

                WIPDATA.clear()
                WIPDATA.insert(0, wıpData)

                for x in range(i):
                    WIPDATA.insert(1, ",1")
        except:
            pass

    ZERR()

    if cb1Var.get() == 1:
        unInput = []
        unInput.clear()
        for a in ınput:
            if a not in unInput:
                unInput.append(a)

        if cb2Var.get() == 1:
            outputNum = int(outputNumBox.get("1.0", "end-1c"))

            wıpdata = str(WIPDATA)
            wıpdata = wıpdata.replace("[", "")
            wıpdata = wıpdata.replace("]", "")
            wıpdata = wıpdata.replace("'", "")
            wıpdata = wıpdata.replace(" ", "")
            wıpdata = wıpdata.replace(",,", ",")

            wıpdata = wıpdata.split(",")

            WIPDATA.clear()
            WIPDATA.insert(0, wıpdata)

            string_list = WIPDATA[0]
            integer_map = map(int, string_list)
            wıpdata = list(integer_map)

            output = random.choices(unInput, k=outputNum, weights=wıpdata)
            OUTPUT.clear()
            OUTPUT.insert(0, output)

        else:
            wıpdata = str(WIPDATA)
            wıpdata = wıpdata.replace("[", "")
            wıpdata = wıpdata.replace("]", "")
            wıpdata = wıpdata.replace("'", "")
            wıpdata = wıpdata.replace(" ", "")
            wıpdata = wıpdata.replace(",,", ",")

            wıpdata = wıpdata.split(",")

            WIPDATA.clear()
            WIPDATA.insert(0, wıpdata)

            string_list = WIPDATA[0]
            integer_map = map(int, string_list)
            wıpdata = list(integer_map)

            output = random.choices(unInput, k=1, weights=wıpdata)
            OUTPUT.clear()
            OUTPUT.insert(0, output)

    else:
        if cb2Var.get() == 1:
            outputNum = int(outputNumBox.get("1.0", "end-1c"))


            wıpdata = str(WIPDATA)
            wıpdata = wıpdata.replace("[", "")
            wıpdata = wıpdata.replace("]", "")
            wıpdata = wıpdata.replace("'", "")
            wıpdata = wıpdata.replace(" ", "")
            wıpdata = wıpdata.replace(",,", ",")

            wıpdata = wıpdata.split(",")

            WIPDATA.clear()
            WIPDATA.insert(0, wıpdata)

            string_list = WIPDATA[0]
            integer_map = map(int, string_list)
            wıpdata = list(integer_map)

            output = random.choices(ınput, k=outputNum, weights=wıpdata)
            OUTPUT.clear()
            OUTPUT.insert(0, output)

        else:
            wıpdata = str(WIPDATA)
            wıpdata = wıpdata.replace("[", "")
            wıpdata = wıpdata.replace("]", "")
            wıpdata = wıpdata.replace("'", "")
            wıpdata = wıpdata.replace(" ", "")
            wıpdata = wıpdata.replace(",,", ",")

            wıpdata = wıpdata.split(",")

            WIPDATA.clear()
            WIPDATA.insert(0, wıpdata)

            string_list = WIPDATA[0]
            integer_map = map(int, string_list)
            wıpdata = list(integer_map)

            output = random.choices(ınput, k=1, weights=wıpdata)
            OUTPUT.clear()
            OUTPUT.insert(0, output)


        

    OUTPUTList = str(OUTPUT)

    OUTPUTList = OUTPUTList.replace("[", "")
    OUTPUTList = OUTPUTList.replace("]", "")
    OUTPUTList = OUTPUTList.replace("'", "")
    OUTPUTList = OUTPUTList.replace(" ", "")


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
    win.config(bg="#F2B90C")

    mode1L = Label(win)
    mode1LTxt = "Mode-1: Filter input against multiple inputs."
    mode1L.config(text=mode1LTxt)
    mode1L.config(bg="#F2B90C")
    mode1L.pack()

    mode2L = Label(win)
    mode2LTxt = "Mode-2: Enable multiple outputs."
    mode2L.config(text=mode2LTxt)
    mode2L.config(bg="#F2B90C")
    mode2L.pack()

    mode3L = Label(win)
    mode3LTxt = "OAF: Output as File"
    mode3L.config(text=mode3LTxt)
    mode3L.config(bg="#F2B90C")
    mode3L.pack()

    mode4L = Label(win)
    mode4LTxt = "IAF: Input as Folder"
    mode4L.config(text=mode4LTxt)
    mode4L.config(bg="#F2B90C")
    mode4L.pack()



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
    fData = str(OUTPUT)
    fData = fData.replace("[", "")
    fData = fData.replace("]", "")
    fData = fData.replace("'", "")
    fData = fData.replace(" ", "")
    f.write(fData)
    f.close()

outputAsFileBtn = Button(root, text="OAF")
outputAsFileBtn.config(command=outputAsFile)
outputAsFileBtn.config(width=6)
outputAsFileBtn.place(x=678, y=80)

def ınputAsFile():

    f = filedialog.askopenfile(
        mode="r",
        defaultextension = ".txt",
        filetypes = [
            ("Text file", ".txt")
        ]
        )
    
    fp = os.path.abspath(f.name)

    f = open(fp, "r")
    fData = f.read()
    f.close()
    fData = fData.replace("[", "")
    fData = fData.replace("]", "")
    fData = fData.replace("'", "")
    fData = fData.replace(" ", "")
    ınputBox.insert("1.0", fData)

ınputAsFileBtn = Button(root, text="IAF")
ınputAsFileBtn.config(command=ınputAsFile)
ınputAsFileBtn.config(width=6)
ınputAsFileBtn.place(x=615, y=80)

WIPlabel = Label(root, text="Weight input (',' seperated):")
WIPlabel.config(bg="#F2B90C")
WIPlabel.place(x=30, y=140)

WIP = Text(root, height=5, width=70)
WIP.place(x=30, y=170)

def ınWeightSubmit():
    WIPentry = WIP.get("1.0", "end-1c")
    WIPınput = WIPentry.split(",")

    WIPlen = len(WIPınput)
    WEIGHTLEN.clear()
    WEIGHTLEN.insert(0, WIPlen)

    WIPDATA.clear()
    WIPDATA.insert(0, WIPınput)











root.mainloop()