import tkinter as tk
import random
import time

class MemoryGame:
    def __init__(self, parent, flashcards):
        self.parent = parent
        self.flashcards = flashcards
        self.cards = []
        self.flipped_cards = []
        self.matched = set()
        self.moves = 0

        self.window = tk.Toplevel(self.parent)
        self.window.title("Memory Game")
        self.setup_game_board()

    def setup_game_board(self):
        """Sets up the memory game board with flashcard pairs."""
        for widget in self.window.winfo_children():
            widget.destroy()

        self.moves = 0
        self.flipped_cards = []
        self.matched = set()

        # Create pairs (term ↔ translation) and shuffle
        paired_cards = []
        for term, translation in [(fc[1], fc[2]) for fc in self.flashcards]:
            paired_cards.append(('term', term))
            paired_cards.append(('translation', translation))

        random.shuffle(paired_cards)

        self.cards = []
        self.card_buttons = []

        # Determine grid size
        total = len(paired_cards)
        cols = 4
        rows = (total + cols - 1) // cols

        for i in range(total):
            card_info = {
                "id": i,
                "type": paired_cards[i][0],
                "text": paired_cards[i][1],
                "matched": False,
                "button": None
            }
            self.cards.append(card_info)

        for i, card in enumerate(self.cards):
            btn = tk.Button(self.window, text="❓", width=12, height=4,
                            command=lambda idx=i: self.on_card_click(idx))
            btn.grid(row=i // cols, column=i % cols, padx=5, pady=5)
            card["button"] = btn
            self.card_buttons.append(btn)

        self.status_label = tk.Label(self.window, text="Moves: 0", font=("Arial", 12))
        self.status_label.grid(row=rows, column=0, columnspan=cols, pady=10)

    def on_card_click(self, card_id):
        """Handle a card being clicked."""
        if self.cards[card_id]["matched"] or card_id in self.flipped_cards:
            return

        self.flip_card(card_id)
        self.flipped_cards.append(card_id)

        if len(self.flipped_cards) == 2:
            self.window.after(800, self.check_for_match)

    def flip_card(self, card_id):
        """Reveal the card's text."""
        card = self.cards[card_id]
        card["button"].config(text=card["text"], state="disabled")

    def hide_card(self, card_id):
        """Flip the card back over."""
        card = self.cards[card_id]
        card["button"].config(text="❓", state="normal")

    def check_for_match(self):
        """Check if the two flipped cards match."""
        id1, id2 = self.flipped_cards
        card1, card2 = self.cards[id1], self.cards[id2]

        # Check for match: one is term, one is translation, and they correspond in the flashcard data
        is_match = False
        for fc in self.flashcards:
            if {card1["text"], card2["text"]} == {fc[1], fc[2]}:
                is_match = True
                break

        if is_match:
            card1["matched"] = True
            card2["matched"] = True
            self.matched.update({id1, id2})
        else:
            self.hide_card(id1)
            self.hide_card(id2)

        self.flipped_cards.clear()
        self.moves += 1
        self.status_label.config(text=f"Moves: {self.moves}")

        if self.is_game_won():
            self.window.after(500, self.show_game_over)

    def is_game_won(self):
        """Check if all pairs have been matched."""
        return all(card["matched"] for card in self.cards)

    def show_game_over(self):
        """Display 'You Won' message and allow user to restart or return."""
        for btn in self.card_buttons:
            btn.config(state="disabled")

        game_over_frame = tk.Frame(self.window)
        game_over_frame.grid(row=10, column=0, columnspan=4, pady=10)

        tk.Label(game_over_frame, text=f"You Won in {self.moves} moves!", font=("Arial", 14, "bold")).pack(pady=5)
        tk.Button(game_over_frame, text="Play Again", command=self.reset_game).pack(pady=2)
        tk.Button(game_over_frame, text="Return to Menu", command=self.window.destroy).pack(pady=2)

    def reset_game(self):
        """Resets the game state and reshuffles the cards."""
        self.setup_game_board()
