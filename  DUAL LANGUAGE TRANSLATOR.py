import tkinter as tk
from tkinter import messagebox
from transformers import MarianMTModel, MarianTokenizer

# Load pre-trained models
model_fr = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-fr')
tokenizer_fr = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-fr')

model_hi = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-hi')
tokenizer_hi = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-hi')

def translate(text):
    if len(text) < 10:
        return "Upload again", "Upload again"

    # Translate to French
    tokens_fr = tokenizer_fr(text, return_tensors="pt")
    translated_fr = model_fr.generate(**tokens_fr)
    french_translation = tokenizer_fr.decode(translated_fr[0], skip_special_tokens=True)

    # Translate to Hindi
    tokens_hi = tokenizer_hi(text, return_tensors="pt")
    translated_hi = model_hi.generate(**tokens_hi)
    hindi_translation = tokenizer_hi.decode(translated_hi[0], skip_special_tokens=True)

    return french_translation, hindi_translation

def process_input():
    text = entry.get()
    french, hindi = translate(text)
    
    if french == "Upload again":
        messagebox.showerror("Error", "Input text must have 10 or more letters.")
    else:
        output_fr.config(text=f"French: {french}")
        output_hi.config(text=f"Hindi: {hindi}")

# Set up the GUI
root = tk.Tk()
root.title("Dual Language Translator")

# Input section
tk.Label(root, text="Enter English text:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Buttons
tk.Button(root, text="Translate", command=process_input).pack(pady=10)

# Output section
output_fr = tk.Label(root, text="French: ")
output_fr.pack(pady=5)

output_hi = tk.Label(root, text="Hindi: ")
output_hi.pack(pady=5)

# Run the GUI
root.mainloop()
