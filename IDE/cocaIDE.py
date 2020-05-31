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
    codeArea.insert(INSERT, "if(_your_expression_goes_here_) then {\n\n} else {\n\n}\n")

def insert_from():
    codeArea.insert(INSERT, "from int _var_ = _int_constant_ to _exp_ do {\n\n}\n")

def insert_while():
    codeArea.insert(INSERT, "while (_your_expression_goes_here_) do {\n\n}\n")

def insert_function():
    codeArea.insert(INSERT, "function _type_ _id_ (_your_parameters_go_here_)\n_optional_vars_here_\n{\n\n}\n")

def insert_main():
    codeArea.insert(INSERT, "main(){\n  _your_code_goes_here_\n\n}\n")

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
insertIf.pack(padx=5, pady=10, side=LEFT)

#Add if button
insertFrom = Button(root, text="Insert From", command=insert_from)
insertFrom.pack(padx=5, pady=10, side=LEFT)

#Add if button
insertWhile = Button(root, text="Insert While", command=insert_while)
insertWhile.pack(padx=5, pady=10, side=LEFT)

#Add if button
insertFunction = Button(root, text="Insert Function", command=insert_function)
insertFunction.pack(padx=5, pady=10, side=LEFT)

#Add if button
insertMain = Button(root, text="Insert Main", command=insert_main)
insertMain.pack(padx=5, pady=10, side=LEFT)

# Run button
runButton = Button(root, text="Run", command=run_clicked)
runButton.pack(padx=5, pady=10, side=RIGHT)

# Save button
saveButton = Button(root, text="Save", command=save_clicked)
saveButton.pack(padx=5, pady=10, side=RIGHT)

# Clear console button
clearConsole = Button(root, text="Clear Console", command=clear_console_clicked)
clearConsole.pack(padx=5, pady=10, side=RIGHT)

root.mainloop()
