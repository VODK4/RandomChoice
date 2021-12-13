from tkinter import *
import random


#fucntions
def elementCountList():

    OUTPUT = []

    entryName = Label(root, text="Inputs (',' seperated):")
    entryName.config(bg="#F2B90C")
    entryName.place(x=30, y=1)

    ınputBox = Text(root, height=5, width=70)
    ınputBox.place(x=30, y=20)

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

    def clearEntries():
        ınputBox.delete(1.0, END)


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

    clearEntriesBtn = Button(root, text="Clear Input")
    clearEntriesBtn.config(command=clearEntries)
    clearEntriesBtn.config(width=15)
    clearEntriesBtn.place(x=615, y=50)


    
    outputLabel = Label(root)
    outputLabel.config(bg="#F2B90C")
    outputLabel.place(x=40, y=105)






    
   
#framework
root = Tk()

root.geometry("1000x500")
root.title("RandomChoice")
root.config(bg="#F2B90C")

elementCountList()



root.mainloop()