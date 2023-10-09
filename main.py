import sys                      # imports required libraries
import platform
v=sys.version                   # checks python version
print(v)
if "v2" in v:                   # imports Tkinter depending on version
    from Tkinter import *
    import tkFileDialog
elif "v3" in v or "3.4" in v:
    from tkinter import *
    from tkinter import filedialog

root=Tk("Text Editor")          # the root with a tk window
text=Text(root)                 # makes root into a text box
text.grid()   

def saveas():                   # makes a save as button
    global text         

    t = text.get("1.0", "end-1c")   # gets text from the text box and saves it in wherever the user wants
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

button=Button(root, text="Save", command=saveas)    # makes button with command 
button.grid()

# sets font to helvetica
def FontHelvetica():
    global text
    text.config(font="Helvetica")

# sets font to courier
def FontCourier():
    global text
    text.config(font="Courier")

# makes the button and the selection for fonts.
font=Menubutton(root, text="Font") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu

helvetica=IntVar() 
courier=IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier,
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, 
command=FontHelvetica)

root.mainloop()