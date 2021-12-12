import pyttsx3
from tkinter import *
 
# Define speak function
def speak():
    engine = pyttsx3.init()
    engine.say(scriptEntry.get("1.0",END))
    engine.runAndWait()


# Create a GUI window
root = Tk()
root.geometry("900x600")
root.title("ScriptToSpeech")
frame = Frame(root)
frame.pack()

# Create a text box
scriptEntry = Text(frame, width = 30, height = 3) 
scriptEntry.insert(1.0,'Text to speak')
scriptEntry.pack(padx = 5, pady = 5)

# Create a button to speak
speakButton = Button(frame, text = "Submit", command = speak)
speakButton.pack(padx = 5, pady = 5)

root.mainloop()


