# game_memory.py
"""
Memory game: Players flip cards to match terms and translations.
Uses Canvas for layout and interactivity.
"""

import tkinter as tk
import random
import time

class MemoryGame:
    def __init__(self, root, flashcards):
        self.root = root
        self.flashcards = flashcards  # List of (term, translation) tuples
        self.setup_game_board()

    def setup_game_board(self):
        # TODO: Create card grid using Canvas
        pass

    def on_card_click(self, card_id):
        # TODO: Reveal card, check for matches
        pass

    def check_for_match(self):
        # TODO: Check if two flipped cards match
        pass

    def reset_game(self):
        # TODO: Reset state and reshuffle cards
        pass
