from tkinter import *

#create window
window = Tk()
window.title("Event handler")
window.geometry("100x100")

#Event handler for keypress
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
    
#Bind key press event to handle_key press{ }
window.bind("<Key>", handle_keypress)

def handle_click(events):
    print("\nthe button has been clicked")
    
button = Button(text="click me")
button.pack()
button.bind("<Button-1>", handle_click)

window.mainloop()