from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    #// Put this sentence in a pop-up message box:

    # Get the player to enter an adjective
    #messagebox.showinfo(title=None, message='Get the player smart')
    adj = simpledialog.askstring(title='question', prompt='adjective?')
    # Get the player to enter a type of liquid
    #messagebox.showinfo(title=None, message='Get the player some Gatorade')
    liquid = simpledialog.askstring(title=None, prompt="name a liquid")
    # Get the player to enter a body part
    #messagebox.showinfo(title=None, message='Get the player a hand')
    body = simpledialog.askstring(title=None, prompt='name a body part')
    # Get the player to enter a verb
    #messagebox.showinfo(title=None, message='Get the player to run')
    verb = simpledialog.askstring(title=None, prompt='name a verb')
    # Get the player to enter a place
    #messagebox.showinfo(title=None, message='Get the player to Las Vegas')
    place = simpledialog.askstring(title=None, prompt='name a place')
    # The story below has has been written as a group of Strings joined together by + signs.
    # The story contains place holders, indicated by [** **] which you need to replace with
    # the values entered by the player.
    # Hint:  You will need to add more + signs to join the variables to the other parts of the story.
        
    story = (
    "Piranhas are more " + adj + " during the day, so cross the river at\n"
    "night. Piranhas are attracted to fresh " + liquid + " and will most\n"
    "likely take a bite out of your " + body + " if you " + verb + ". Whatever\n"
    "you do, if you have an open wound, try to find another way to get "
    "back to " + place + ". Good luck!"
    )

    
    # Make a pop-up that contains the final story. The \n escape characters add line breaks to the story. 
    # If you need to, move them around to make your story look better in the pop-up
    messagebox.showinfo(title=None, message=story)
    # If you want to write your own Madlib story, just change the story variable and ask the player different questions.


    # Run the window's .mainloop() method
    window.mainloop()