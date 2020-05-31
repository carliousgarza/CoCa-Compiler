from tkinter import *
import sys
import os

def save_clicked():
    # Get code from the codeArea
    code = codeArea.get('0.0', 'end-1c')
    # Get and write to file
    fileName = 'textEditorFile.coca'
    file = open(fileName, 'w')
    file.write(code)
    file.close
    console.insert('1.0', 'Saved File\n')

def run_clicked():
    os.system('python3 ../main.py textEditorFile.coca')

# Root Window
root = Tk()
root.title('CoCa Compiler')
root.resizable(False, False)

# Text editor textarea
codeArea = Text(root, height=35, width=100)
codeArea.configure(background='white', foreground="black")
#codeArea.insert(1.0, "//Code goes here")
codeArea.pack()

# Console textarea
console = Text(root, height=15, width=100)
console.configure(background='black',foreground="#000fff000")
#console.configure(background='black',foreground="#000fff000", state="disabled")
console.pack()

# Save button
runButton = Button(root, text="Save", command=save_clicked)
runButton.pack()

# Run button
runButton = Button(root, text="Run", command=run_clicked)
runButton.pack()


root.mainloop()
