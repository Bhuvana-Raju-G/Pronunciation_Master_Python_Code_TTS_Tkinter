import tkinter 
from tkinter import * 
import pyttsx3

tk=tkinter.Tk() 
tk.title('Text to Speech')
tk.geometry("300x200")
tk.resizable(width=False,height=False)

TBox=Text(tk,height=10,width=100,bg="#dfe6e9")
TBox.pack()

def speaktext():
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty("voices",voices[1].id)

    if not TBox.get("1.0","end-1c"):
       engine.say("enter Something")
       engine.runAndWait()
    else:
        text=TBox.get("1.0","end-1c")
        engine.say(text)
        engine.runAndWait()

SpeakBtn=Button(tk,command=speaktext,text="Speak",bg="#6c5ce7",activebackground='#dfe6e9',width="100",font='bold',fg='white')
SpeakBtn.pack()

tk.mainloop()