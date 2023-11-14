import tkinter as tk
import time

class AdventureGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Adventure Game")
        self.master.geometry("500x400")

        self.background_color = "#f0f0f0"
        self.text_color = "#333333"
        self.button_color = "#55aacc"
        self.button_text_color = "#ffffff"
        self.font = ("Arial", 12)

        self.master.configure(bg=self.background_color)

        self.intro_text = tk.Label(
            self.master,
            text="Welcome to the Adventure Game!",
            bg=self.background_color,
            fg=self.text_color,
            font=("Arial", 18, "bold")
        )
        self.intro_text.pack(pady=20)

        self.start_button = tk.Button(
            self.master,
            text="Start",
            bg=self.button_color,
            fg=self.button_text_color,
            font=self.font,
            command=self.intro
        )
        self.start_button.pack(pady=10)

    def intro(self):
        self.clear_screen()
        self.game_text = tk.Label(self.master, text="You find yourself in a mysterious forest...")
        self.game_text.pack()

        self.choice_button_1 = tk.Button(self.master, text="Go deeper into the forest", command=self.go_deeper)
        self.choice_button_1.pack()

        self.choice_button_2 = tk.Button(self.master, text="Look for a path to get out", command=self.find_path)
        self.choice_button_2.pack()

    def go_deeper(self):
        self.clear_screen()
        self.game_text = tk.Label(self.master, text="You chose to go deeper into the forest.\nYou encounter a river blocking your path.")
        self.game_text.pack()

        self.choice_button_3 = tk.Button(self.master, text="Try to swim across", command=self.swim_across)
        self.choice_button_3.pack()

        self.choice_button_4 = tk.Button(self.master, text="Look for a bridge", command=self.find_bridge)
        self.choice_button_4.pack()

    def swim_across(self):
        self.clear_screen()
        self.game_text = tk.Label(self.master, text="You attempt to swim across...\nOh no! There are dangerous creatures in the water.\nYou were attacked and couldn't make it across.")
        self.game_text.pack()

        self.game_over()

    def find_bridge(self):
        self.clear_screen()
        self.game_text = tk.Label(self.master, text="You find a sturdy bridge and cross the river safely.\nYou continue your journey deeper into the forest...\nMore adventures await you on this path.")
        self.game_text.pack()

        self.choice_button_5 = tk.Button(self.master, text="Explore the cave", command=self.explore_cave)
        self.choice_button_5.pack()

        self.choice_button_6 = tk.Button(self.master, text="Follow the animal tracks", command=self.follow_tracks)
        self.choice_button_6.pack()

    def explore_cave(self):
        self.clear_screen()
        self.game_text = tk.Label(self.master, text="You enter a dark cave.\nYou hear strange noises echoing from the depths.")
        self.game_text.pack()

        self.choice_button_7 = tk.Button(self.master, text="Investigate the noises", command=self.investigate_noises)
        self.choice_button_7.pack()

        self.choice_button_8 = tk.Button(self.master, text="Leave the cave", command=self.leave_cave)
        self.choice_button_8.pack()

    def investigate_noises(self):
        self.clear_screen()
        self.game_text = tk.Label(self.master, text="As you move deeper into the cave, you encounter a treasure chest!\nCongratulations, you found treasure!")
        self.game_text.pack()

        self.play_again()

    def leave_cave(self):
        self.clear_screen()
        self.game_text = tk.Label(self.master, text="You decide to leave the cave and continue your adventure.")
        self.game_text.pack()

        self.choice_button_9 = tk.Button(self.master, text="Continue exploring", command=self.continue_exploring)
        self.choice_button_9.pack()

    def continue_exploring(self):
        self.clear_screen()
        self.game_text = tk.Label(self.master, text="You continue your exploration and find a map leading to the nearest village.\nYou successfully reach the village and are safe.")
        self.game_text.pack()

        self.play_again()

    def follow_tracks(self):
        self.clear_screen()
        self.game_text = tk.Label(self.master, text="You follow the tracks and encounter a friendly guide.\nThe guide helps you navigate safely out of the forest.\nCongratulations, you made it out!")
        self.game_text.pack()

        self.play_again()

    def find_path(self):
        self.clear_screen()
        self.game_text = tk.Label(self.master, text="You search for a path to get out of the forest.\nAfter a while, you find a road leading out of the forest.\nCongratulations! You successfully escaped the forest.")
        self.game_text.pack()

        self.play_again()

    def game_over(self):
        self.game_text = tk.Label(self.master, text="\nGame Over. Do you want to play again?")
        self.game_text.pack()

        self.play_again()

    def play_again(self):
        self.choice_button_again = tk.Button(self.master, text="Play Again", command=self.intro)
        self.choice_button_again.pack()

        self.choice_button_quit = tk.Button(self.master, text="Quit", command=self.quit_game)
        self.choice_button_quit.pack()

    def quit_game(self):
        self.master.destroy()

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    adventure_game = AdventureGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
