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
    console.insert('end-1c', 'Saved File\n')

def run_clicked():
    #os.system('python3 ../main.py textEditorFile.coca')
    resultText = os.popen('python3 ../main.py textEditorFile.coca').read()

    resultTextArray = resultText.split("\n")

    for line in resultTextArray:
        print(line)
        if line.startswith("printing:"):
            console.insert('end-1c', f'{line[9:-1]}\n')

def clear_console_clicked():
    console.delete('1.0', 'end')

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
console.pack()

# Clear console button
clearConsole = Button(root, text="Clear Console", command=clear_console_clicked)
clearConsole.pack()

# Save button
saveButton = Button(root, text="Save", command=save_clicked)
saveButton.pack()

# Run button
runButton = Button(root, text="Run", command=run_clicked)
runButton.pack()


root.mainloop()
