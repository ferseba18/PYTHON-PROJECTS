import random
import tkinter as tk
from tkinter import ttk, messagebox

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper and Scissors")
        
        self.user_victories = 0
        self.computer_victories = 0
        
        self.options = ['rock', 'paper', 'scissors']
        
        self.label = tk.Label(root, text="Choose rock, paper, or scissors:")
        self.label.pack(pady=10)
        
        self.choice_var = tk.StringVar()
        self.choice_dropdown = ttk.Combobox(root, textvariable=self.choice_var, values=self.options, state='readonly')
        self.choice_dropdown.pack(pady=5)
        self.choice_dropdown.set("rock")  # Default selection
        
        self.play_button = tk.Button(root, text="Play", command=self.play_game)
        self.play_button.pack(pady=5)
        
        self.quit_button = tk.Button(root, text="Quit", command=self.quit_game)
        self.quit_button.pack(pady=5)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        
        self.score_label = tk.Label(root, text="User: 0 | Computer: 0")
        self.score_label.pack(pady=10)

    def play_game(self):
        user_input = self.choice_var.get().lower()
        computer_choice = random.choice(self.options)
        
        result_text = f"Computer chose: {computer_choice}\n"
        
        if user_input == computer_choice:
            result_text == "It's a tie!"
        elif (user_input == 'paper' and computer_choice == 'rock') or \
             (user_input == 'rock' and computer_choice == 'scissors') or \
             (user_input == 'scissors' and computer_choice == 'paper'):
            result_text == "You win!"
            self.user_victories += 1
        else:
            result_text == "Computer wins!"
            self.computer_victories += 1
        
        self.result_label.config(text=result_text)
        self.score_label.config(text=f"User: {self.user_victories} | Computer: {self.computer_victories}")
    
    def quit_game(self):
        final_result = f"Final Score:\nUser: {self.user_victories}\nComputer: {self.computer_victories}\n"
        
        messagebox.showinfo("Game Over", final_result)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
