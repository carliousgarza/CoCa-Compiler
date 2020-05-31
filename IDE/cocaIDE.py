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
    resultText = os.popen('python3 ../main.py textEditorFile.coca').read()
    resultTextArray = resultText.split("\n")

    for line in resultTextArray:
        print(line)
        if line.startswith("printing:"):
            console.insert('end-1c', f'{line[9:-1]}\n')

def clear_console_clicked():
    console.delete('1.0', 'end')

def insert_if():
    codeArea.insert(INSERT, "if(/* your expression goes here*/) then {\n\n} else {\n\n}\n")

def insert_from():
    codeArea.insert(INSERT, "from int /*var*/ = /*int_constant*/ to /*exp*/ do {\n\n}\n")

def insert_while():
    codeArea.insert(INSERT, "while (/* your expression goes here*/ ) do {\n\n}\n")

def insert_function():
    codeArea.insert(INSERT, "function /*type*/ /*id*/ (/*your parameters go here*/) /*optional vars here*/ {\n\n}\n")

def insert_main():
    codeArea.insert(INSERT, "main(){\n /*your code goes here*/\n\n}\n")

# Root Window
root = Tk()
root.title('CoCa Compiler')
root.resizable(False, False)

# Text editor textarea
codeArea = Text(root, height=35, width=100)
codeArea.configure(background='white', foreground="black")
codeArea.insert(1.0, "program textEditorFile;\n//Code goes here\n")
codeArea.pack()

# Console textarea
console = Text(root, height=15, width=100)
console.configure(background='black',foreground="#000fff000")
console.pack()

#Add if button
insertIf = Button(root, text="Insert If", command=insert_if)
insertIf.pack()

#Add if button
insertFrom = Button(root, text="Insert From", command=insert_from)
insertFrom.pack()

#Add if button
insertWhile = Button(root, text="Insert While", command=insert_while)
insertWhile.pack()

#Add if button
insertFunction = Button(root, text="Insert Function", command=insert_function)
insertFunction.pack()

#Add if button
insertMain = Button(root, text="Insert Main", command=insert_main)
insertMain.pack()

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
