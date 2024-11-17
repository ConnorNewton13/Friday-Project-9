import openai
import sqlite3
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_openai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def on_submit():
    prompt = prompt_entry.get() 
    if not prompt:
        messagebox.showwarning("Input Error", "Please enter a prompt.")
        return
    
    response = get_openai_response(prompt)
    
    output_text.delete(1.0, tk.END)  
    output_text.insert(tk.END, response) 

root = tk.Tk()
root.title("OpenAI Completion GUI")

prompt_label = tk.Label(root, text="Enter your prompt:")
prompt_label.pack(padx=10, pady=5)

prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(padx=10, pady=10)

output_label = tk.Label(root, text="Completion Output:")
output_label.pack(padx=10, pady=5)

output_text = tk.Text(root, height=10, width=50)
output_text.pack(padx=10, pady=5)

root.mainloop()