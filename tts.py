import tkinter
import pyttsx3
from tkinter import *
 
def speak():
    engine = pyttsx3.init()
    engine.say(testEntry.get())
    engine.runAndWait()

# Create a GUI window
root = Tk()
root.geometry("900x600")
root.title("Test")

frame = Frame(root)
frame.pack()


testEntry = Entry(frame, width = 20)
testEntry.insert(0,'Text to speak')
testEntry.pack(padx = 5, pady = 5)

Button = Button(frame, text = "Submit", command = speak)
Button.pack(padx = 5, pady = 5)

root.mainloop()


# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# engine.runAndWait()

