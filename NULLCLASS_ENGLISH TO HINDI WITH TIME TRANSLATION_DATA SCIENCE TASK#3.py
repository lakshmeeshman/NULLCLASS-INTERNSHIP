import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
from datetime import datetime

# Function to translate words
def translate_word():
    word = entry.get().strip()
    if not word:
        messagebox.showerror("Error", "Please enter a word.")
        return
    
    if word[0].lower() in 'aeiou':
        messagebox.showerror("Error", "This word starts with a vowel. Please provide another word.")
        return
    
    current_time = datetime.now().time()
    if not (current_time.hour == 21 or (current_time.hour == 22 and current_time.minute == 0)):
        messagebox.showerror("Error", "Translations for words starting with vowels are only allowed between 9 PM and 10 PM.")
        return
    
    try:
        translator = Translator()
        translation = translator.translate(word, src='en', dest='hi')
        output_label.config(text=f'Translation: {translation.text}')
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

# Create the GUI application
app = tk.Tk()
app.title("English to Hindi Translator")

# Input section
tk.Label(app, text="Enter an English word:").pack(pady=5)
entry = tk.Entry(app, width=50)
entry.pack(pady=5)

# Translate button
translate_button = tk.Button(app, text="Translate", command=translate_word)
translate_button.pack(pady=5)

# Output section
output_label = tk.Label(app, text="Translation: ")
output_label.pack(pady=20)

# Run the GUI application
app.mainloop()
