# main.py
"""
Main application file that initializes the GUI, handles navigation between screens,
and connects flashcard and game modules.
"""

import tkinter as tk
from flashcards import FlashcardManager
from game_memory import MemoryGame
from game_race import RaceGame
from game_sorting import SortingGame  # Placeholder for future game

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Vocabulary Flashcards")
        self.flashcard_manager = FlashcardManager()
        self.setup_main_menu()

    def setup_main_menu(self):
        # TODO: GUI layout for main menu with buttons to start games, edit flashcards, view progress
        pass

    def launch_memory_game(self):
        # TODO: Launch memory game interface
        pass

    def launch_race_game(self):
        # TODO: Launch race game
        pass

    def launch_sorting_game(self):
        # TODO: Launch sorting game (if implemented)
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
