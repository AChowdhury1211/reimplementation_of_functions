import pyperclip

def copy_terminal_output_python(command):
    try:
        # Execute the Python expression/command
        exec(command, globals())
        
        # Capture the output of the expression/command
        output = str(eval(command, globals()))
        
        # Copy the output to the clipboard
        pyperclip.copy(output)
        print("Output copied to clipboard:", output)
        return output
    except Exception as e:
        print("An error occurred:", e)

command = "5 + 3"
copy_terminal_output_python(command)


