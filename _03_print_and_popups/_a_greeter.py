from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window = Tk()

    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Ask the user for their name and save it to a variable
    # name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    name = simpledialog.askstring(title='question', prompt='What is your name')

    age = simpledialog.askstring('first question', 'Hello' + name + 'how old are you')
    # Show a message box with your message using the .showinfo() method
    messagebox.showinfo(title=None, message='Hello' + name + 'You are' + age)
    messagebox.showwarning(title=None, message='WARNING!' + name + 'is here')
    messagebox.showerror(title=None, message= name + "is right behind you")
    # Print your message to the console using the print() function
    print('have a nice day')
    # Show an error message using messagebox.showerror()
    messagebox.showerror(title=None, message= name + 'does not understand')
    # Run the window's .mainloop() method
    window.mainloop()