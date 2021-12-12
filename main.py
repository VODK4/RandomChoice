from tkinter import *
import random


#fucntions
def elementCountList():

    OUTPUT = []

    entryName = Label(root, text="Inputs (',' seperated):")
    entryName.config(bg="#F2B90C")
    entryName.pack()

    ınputBox = Entry(root)
    ınputBox.pack()

    def textToList():
        entry = ınputBox.get()
        ınput = entry.split(",")

        output = random.choice(ınput)
        OUTPUT.insert(0, output)

        OUTPUTList = str(OUTPUT)

        outputLabel.config(text="Output="+OUTPUTList)



    Button(root, text="Submit Input", command=textToList).pack()

    
    outputLabel = Label(root)
    outputLabel.pack()




    
   
#framework
root = Tk()

root.geometry("1000x500")
root.title("RandomChoice")
root.config(bg="#F2B90C")

elementCountList()



root.mainloop()