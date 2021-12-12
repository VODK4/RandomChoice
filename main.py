from tkinter import *
import random


#fucntions
def elementCountList():

    OUTPUT = []

    entryName = Label(root, text="Inputs (',' seperated):")
    entryName.config(bg="#F2B90C")
    entryName.pack()

    ınputBox = Text(root, height=5, width=70)
    ınputBox.pack()

    def submit():
        entry = ınputBox.get("1.0", "end-1c")
        ınput = entry.split(",")

        output = random.choice(ınput)
        OUTPUT.clear()
        OUTPUT.insert(0, output)

        OUTPUTList = str(OUTPUT)

        if cb1Var.get() == 1:
            ınput = str(list(dict.fromkeys(ınput)))

        outputLabel.config(text="Output="+OUTPUTList)


    cb1 = Checkbutton(root, text="Allow item only once.")
    cb1.config(bg="#F2B90C")

    cb1Var = IntVar()
    cb1.config(variable=cb1Var)
    cb1.config(onvalue=1, offvalue=0)
    cb1.pack()

    Button(root, text="Submit Input", command=submit).pack()

    
    outputLabel = Label(root)
    outputLabel.config(bg="#F2B90C")
    outputLabel.pack()




    
   
#framework
root = Tk()

root.geometry("1000x500")
root.title("RandomChoice")
root.config(bg="#F2B90C")

elementCountList()



root.mainloop()