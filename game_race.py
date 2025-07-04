# game_race.py
"""
Race game: Character moves forward on correct answers, slows on wrong ones.
Can use Turtle or Canvas animations.
"""

import tkinter as tk
import random
import time
# Optional: import turtle

class RaceGame:
    def __init__(self, root, flashcards):
        self.root = root
        self.flashcards = flashcards
        self.setup_race_scene()

    def setup_race_scene(self):
        # TODO: Draw characters, background race track, start button
        pass

    def ask_question(self):
        # TODO: Present a question and answer options
        pass

    def handle_answer(self, user_input):
        # TODO: Move character forward or slow down based on correctness
        pass

    def start_race(self):
        # TODO: Trigger race loop/timer
        pass
