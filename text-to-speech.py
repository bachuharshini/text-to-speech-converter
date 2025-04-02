import tkinter as tk
from gtts import gTTS
import os

def convert_text_to_speech():
    text = text_entry.get()
    speech = gTTS(text=text, lang='en')
    speech.save("speech.mp3")
    play_audio()

def play_audio():
    if os.name == 'nt':  # Windows
        os.system("start speech.mp3")
    elif os.name == 'posix':  # macOS
        os.system("afplay speech.mp3")
    else:  # Linux and others
        os.system("xdg-open speech.mp3")

def exit_application():
    root.destroy()

root = tk.Tk()
root.title("Harshini Text-to-Speech Converter Project")

text_label = tk.Label(root, text="Enter Text:")
text_label.pack()

text_entry = tk.Entry(root, width=50)
text_entry.pack()

play_button = tk.Button(root, text="PLAY", command=convert_text_to_speech)
play_button.pack()

exit_button = tk.Button(root, text="EXIT", command=exit_application)
exit_button.pack()

root.mainloop()