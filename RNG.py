from tkinter import *
import random
import sys

window = Tk() #making a window
window.geometry("360x240")
window.title("Random Number Generator")
odd = BooleanVar()
even = BooleanVar()
rep = BooleanVar()
rowNum = 0
icon = PhotoImage(file='RNGlogo.png')
window.iconphoto(True,icon)

def returnRand(r1,r2,odd,even):
    if(r1 == r2):
        return r1
    elif(odd == even):
        return random.randint(r1,r2)    
    elif(odd):     #if user inputs (2,100) and odd is checked, ensures only odd numbers between range is given
        if(r1 % 2 == 0): 
            r1 += 1
        if(r2 % 2 == 1):  #ensures second range is included
            r2 += 1
        return random.randrange(r1,r2,2)
    elif(even):     #if user inputs (3,101) and even is checked, ensures only even numbers between range is given  
        if(r1 % 2 == 1): 
            r1 += 1
        if(r2 % 2 == 0):  #ensures second range is included
            r2 += 1     
        return random.randrange(r1,r2,2)

warning = Label(window, text= "That's not an integer!!! >:(", font = ("Arial", 10), fg='red')
def generateRand():
    range1 = r1Entry.get()
    range2 = r2Entry.get()

    if(range1 == ''):               #empty input defaults to range(-10,10)
        r1Entry.insert(1,-10)
        range1 = -10
    if(range2 == ''):
        range2 = 10
        r2Entry.insert(0,10)   

    try:
        range1 = int(range1) 
        range2 = int(range2)
        warning.grid_remove()       #just in case there was a warning before
    except ValueError:
        warning.grid(row=2,column=1,padx=5)           

    condOdd = odd.get()
    condEven = even.get()
    condRep = rep.get()

    text = returnRand(range1,range2,condOdd,condEven)
    if(condRep == True):
        i = 0
        while(i < 100):
            text = returnRand(range1,range2,condOdd,condEven)
            randListBox.insert(END, text)
            i += 1
    else:
        randListBox.insert(END, text)
        

def clear():
    randListBox.delete(0,END)
        

r1Label = Label(window, text="Min range?")
r2Label = Label(window, text="Max range?")
r1Entry = Entry(window, font=("Arial",10))
r2Entry = Entry(window, font=("Arial",10))

oddCheck = Checkbutton(window, 
                        text="Odd?", 
                        variable=odd, 
                        onvalue=True,
                        offvalue=False)

evenCheck = Checkbutton(window, 
                        text="Even?", 
                        variable=even, 
                        onvalue=True,
                        offvalue=False)

repeatCheck = Checkbutton(window, 
                        text="Repeat x 100?", 
                        variable=rep, 
                        onvalue=True,
                        offvalue=False)

randButton = Button(window,  
                    text="Generate Random Number",
                    command = generateRand,
                    font = ("Arial", 10),
                    fg = "black")

clearButton = Button(window,  
                    text="Clear",
                    command = clear,
                    font = ("Arial", 10),
                    fg = "black")

sb = Scrollbar(window,orient=VERTICAL)

randListBox = Listbox(window,width= 20, height = 5)

sb.configure(command=randListBox.yview)
randListBox.configure(yscrollcommand=sb.set)

r1Label.grid(row=10,column=0)
r1Entry.grid(row=10,column=1,padx=5)
r2Label.grid(row=11,column=0)
r2Entry.grid(row=11,column=1,padx=5)

oddCheck.grid(row=12,column=0)
evenCheck.grid(row=12,column=1)
repeatCheck.grid(row=12,column=3)

randButton.grid(row=13,column=1)
clearButton.grid(row=1,column=1)
sb.grid(row=0,column=2)
randListBox.grid(row=0,column=1)


if __name__ == '__main__':
    window.mainloop()
