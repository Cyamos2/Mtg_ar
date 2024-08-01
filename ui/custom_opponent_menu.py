import tkinter as tk
from tkinter import messagebox
import requests
import json
import os
from ai_opponents.ai_opponent import create_ai_opponent

class CustomOpponentMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Custom Opponent")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Opponent Name:").grid(row=0, column=0, padx=10, pady=10)
        self.opponent_name_entry = tk.Entry(self.root)
        self.opponent_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Decklist URL:").grid(row=1, column=0, padx=10, pady=10)
        self.decklist_url_entry = tk.Entry(self.root)
        self.decklist_url_entry.grid(row=1, column=1, padx=10, pady=10)

        self.create_opponent_button = tk.Button(self.root, text="Create Opponent", command=self.create_opponent)
        self.create_opponent_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.status_label = tk.Label(self.root, text="", fg="red")
        self.status_label.grid(row=3, column=0, columnspan=2)

    def create_opponent(self):
        opponent_name = self.opponent_name_entry.get()
        decklist_url = self.decklist_url_entry.get()

        if not opponent_name or not decklist_url:
            self.status_label.config(text="Both fields are required.")
            return

        try:
            response = requests.get(decklist_url)
            response.raise_for_status()
            decklist = response.json()
        except requests.exceptions.RequestException as e:
            self.status_label.config(text=f"Error fetching decklist: {e}")
            return

        ai_opponent = create_ai_opponent(opponent_name, decklist_url)
        messagebox.showinfo("Success", f"Custom opponent '{opponent_name}' created successfully!")
        self.status_label.config(text="", fg="green")

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = CustomOpponentMenu(root)
    root.mainloop()
