import tkinter as tk
import tkinter.filedialog
from tkinter import ttk

root = tk.Tk("Text Editor")




def create_toolbox_frame(master):
    frame = tk.Frame(master)


    savebutton = tk.Button(root, text="Save as", command=saveas)
    savebutton.grid( row=0, sticky="w")
    

    openbutton = tk.Button(root, text="Open", command=openfile)
    openbutton.grid( row=0, sticky="e")




def saveas():
    global text
    t = text.get("1.0", "end-1c")  # read from line 1 character 0, and to the of the file without newline
    savelocation = tkinter.filedialog.asksaveasfilename()
    try:
        with open(savelocation, "w+") as file:
            file.write
    except FileNotFoundError:
        print("Error: No such file")



def openfile():
    global text
    openlocation = tkinter.filedialog.askopenfilename()
    
    try:
        with open(openlocation) as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())
    except FileNotFoundError:
        print("Error: No such file")


create_toolbox_frame(root)

text = tk.Text(root)
text.grid()



root.mainloop()
