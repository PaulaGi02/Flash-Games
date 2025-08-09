import tkinter as tk
from tkinter import messagebox, font
import random
import time

class RoundedCard(tk.Canvas):
    """A Canvas widget simulating a card with rounded corners."""
    def __init__(self, master, width, height, bg, border_color, radius=18, **kwargs):
        super().__init__(master, width=width, height=height, bd=0, highlightthickness=0, bg=master['bg'], **kwargs)
        self.radius = radius
        self.bg = bg
        self.border_color = border_color
        self.card_id = self.create_round_rect(2, 2, width-2, height-2, radius, fill=bg, outline=border_color, width=3)
        # Place button on top, invisible border
        self.button = tk.Button(self, text="", font=("Helvetica", 11, "bold"),
                               bg=bg, fg="#677E52", activebackground=bg,
                               activeforeground="#677E52", relief='flat', bd=0,
                               width=8, height=3, cursor='hand2')
        self.create_window(width//2, height//2, window=self.button, width=width-24, height=height-24)

    def create_round_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1+r, y1,
            x2-r, y1,
            x2, y1,
            x2, y1+r,
            x2, y2-r,
            x2, y2,
            x2-r, y2,
            x1+r, y2,
            x1, y2,
            x1, y2-r,
            x1, y1+r,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def set_card_color(self, color):
        self.itemconfig(self.card_id, fill=color)

class MemoryGame:
    def __init__(self, root, flashcards):
        self.root = root
        self.flashcards = flashcards
        self.original_title = self.root.title()

        # Color scheme
        self.colors = {
            'cream': '#F6E8B1',  # Light cream background
            'sage': '#B0CC99',  # Sage green for cards
            'brown': '#89725B',  # Brown for text/borders
            'lime': '#B7CA79',  # Lime green for card backs
            'dark_green': '#677E52'  # Dark green for all text
        }

        # Game state
        self.cards = []
        self.card_widgets = []
        self.flipped_cards = []
        self.matched_pairs = set()
        self.moves = 0
        self.start_time = time.time()
        self.game_frame = None

        # Card animation variables
        self.flip_animation_running = False

        self.setup_game()

    def setup_game(self):
        """Initialize the game board"""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.title("FlashPlay - Memory Game")
        self.root.configure(bg=self.colors['cream'])

        header_frame = tk.Frame(self.root, bg=self.colors['cream'], pady=20)
        header_frame.pack(fill='x')
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        tk.Label(header_frame, text="🧠 Memory Game",
                 font=title_font, bg=self.colors['cream'],
                 fg=self.colors['dark_green']).pack()

        info_frame = tk.Frame(self.root, bg=self.colors['cream'], pady=10)
        info_frame.pack()
        info_font = font.Font(family="Helvetica", size=12)
        self.moves_label = tk.Label(info_frame, text="Moves: 0",
                                    font=info_font, bg=self.colors['cream'],
                                    fg=self.colors['dark_green'])
        self.moves_label.pack(side='left', padx=20)
        self.time_label = tk.Label(info_frame, text="Time: 0s",
                                   font=info_font, bg=self.colors['cream'],
                                   fg=self.colors['dark_green'])
        self.time_label.pack(side='right', padx=20)

        self.prepare_cards()
        self.create_game_board()
        self.create_control_buttons()
        self.update_timer()

    def prepare_cards(self):
        max_pairs = min(8, len(self.flashcards))
        selected_flashcards = random.sample(self.flashcards, max_pairs)
        self.cards = []
        for fc in selected_flashcards:
            self.cards.append({
                'id': len(self.cards),
                'content': fc[1],  # term
                'pair_id': fc[0],
                'type': 'term'
            })
            self.cards.append({
                'id': len(self.cards),
                'content': fc[2],  # translation
                'pair_id': fc[0],
                'type': 'translation'
            })
        random.shuffle(self.cards)

    def create_game_board(self):
        self.game_frame = tk.Frame(self.root, bg=self.colors['cream'], pady=20)
        self.game_frame.pack(expand=True, fill='both')

        num_cards = len(self.cards)
        cols = 4 if num_cards <= 16 else 6
        rows = (num_cards + cols - 1) // cols

        self.card_widgets = []
        CARD_WIDTH, CARD_HEIGHT = 160, 100


        for i, card in enumerate(self.cards):
            row = i // cols
            col = i % cols

            card_canvas = RoundedCard(
                self.game_frame,
                width=CARD_WIDTH,
                height=CARD_HEIGHT,
                bg=self.colors['lime'],  # Card back color
                border_color=self.colors['brown'],
                radius=18
            )
            card_canvas.grid(row=row, column=col, padx=8, pady=8, sticky='nsew')
            self.game_frame.grid_rowconfigure(row, weight=1)
            self.game_frame.grid_columnconfigure(col, weight=1)

            card_btn = card_canvas.button
            card_btn.config(command=lambda idx=i: self.on_card_click(idx))

            def on_enter(e, btn=card_btn, canvas=card_canvas):
                if not self.flip_animation_running and btn.cget('text') == "":
                    btn.configure(bg=self.colors['sage'])
                    canvas.set_card_color(self.colors['sage'])
            def on_leave(e, btn=card_btn, canvas=card_canvas):
                if not self.flip_animation_running and btn.cget('text') == "":
                    btn.configure(bg=self.colors['lime'])
                    canvas.set_card_color(self.colors['lime'])
            card_btn.bind('<Enter>', on_enter)
            card_btn.bind('<Leave>', on_leave)

            self.card_widgets.append({
                'button': card_btn,
                'canvas': card_canvas,
                'flipped': False,
                'matched': False
            })

    def on_card_click(self, card_index):
        if (self.flip_animation_running or
                self.card_widgets[card_index]['flipped'] or
                self.card_widgets[card_index]['matched'] or
                len(self.flipped_cards) >= 2):
            return
        self.flip_card(card_index, reveal=True)
        self.flipped_cards.append(card_index)
        if len(self.flipped_cards) == 2:
            self.moves += 1
            self.moves_label.config(text=f"Moves: {self.moves}")
            self.root.after(1000, self.check_for_match)

    def flip_card(self, card_index, reveal=True):
        card_widget = self.card_widgets[card_index]
        card_data = self.cards[card_index]
        if reveal:
            self.animate_card_flip(card_index, "", card_data['content'], reveal=True)
            card_widget['flipped'] = True
        else:
            self.animate_card_flip(card_index, card_data['content'], "", reveal=False)
            card_widget['flipped'] = False

    def animate_card_flip(self, card_index, old_text, new_text, reveal=True):
        self.flip_animation_running = True
        button = self.card_widgets[card_index]['button']
        canvas = self.card_widgets[card_index]['canvas']
        # Disable hover during animation
        button.unbind('<Enter>')
        button.unbind('<Leave>')

        def shrink_phase(width=8, step=0):
            if width > 0:
                button.configure(width=width - 1)
                self.root.after(40, lambda: shrink_phase(width - 1, step + 1))
            else:
                self.flip_card_content(card_index, new_text, reveal)
                self.root.after(50, lambda: expand_phase(1))

        def expand_phase(width=1):
            if width <= 8:
                button.configure(width=width)
                self.root.after(40, lambda: expand_phase(width + 1))
            else:
                # Re-enable hover effects
                def on_enter(e, btn=button, cnv=canvas):
                    if not self.flip_animation_running and btn.cget('text') == "":
                        btn.configure(bg=self.colors['sage'])
                        cnv.set_card_color(self.colors['sage'])
                def on_leave(e, btn=button, cnv=canvas):
                    if not self.flip_animation_running and btn.cget('text') == "":
                        btn.configure(bg=self.colors['lime'])
                        cnv.set_card_color(self.colors['lime'])
                button.bind('<Enter>', on_enter)
                button.bind('<Leave>', on_leave)
                self.flip_animation_running = False

        shrink_phase()

    def flip_card_content(self, card_index, new_text, reveal):
        button = self.card_widgets[card_index]['button']
        canvas = self.card_widgets[card_index]['canvas']
        button.configure(text=new_text)
        if reveal:
            if self.cards[card_index]['type'] == 'term':
                button.configure(bg=self.colors['sage'], fg=self.colors['dark_green'])
                canvas.set_card_color(self.colors['sage'])
            else:
                button.configure(bg=self.colors['cream'], fg=self.colors['dark_green'])
                canvas.set_card_color(self.colors['cream'])
        else:
            button.configure(bg=self.colors['lime'], fg=self.colors['dark_green'])
            canvas.set_card_color(self.colors['lime'])

    def check_for_match(self):
        if len(self.flipped_cards) != 2:
            return
        card1_idx, card2_idx = self.flipped_cards
        card1 = self.cards[card1_idx]
        card2 = self.cards[card2_idx]
        if card1['pair_id'] == card2['pair_id'] and card1['type'] != card2['type']:
            self.handle_match(card1_idx, card2_idx)
        else:
            self.root.after(500, lambda: self.handle_no_match(card1_idx, card2_idx))
        self.flipped_cards = []

    def handle_match(self, card1_idx, card2_idx):
        self.card_widgets[card1_idx]['matched'] = True
        self.card_widgets[card2_idx]['matched'] = True
        for idx in [card1_idx, card2_idx]:
            button = self.card_widgets[idx]['button']
            canvas = self.card_widgets[idx]['canvas']
            canvas.set_card_color(self.colors['dark_green'])
            button.configure(state='disabled')
        self.matched_pairs.add(self.cards[card1_idx]['pair_id'])
        if self.is_game_won():
            self.root.after(1000, self.show_game_over)

    def handle_no_match(self, card1_idx, card2_idx):
        self.flip_card(card1_idx, reveal=False)
        self.flip_card(card2_idx, reveal=False)

    def is_game_won(self):
        total_pairs = len(set(card['pair_id'] for card in self.cards))
        return len(self.matched_pairs) == total_pairs

    def show_game_over(self):
        elapsed_time = int(time.time() - self.start_time)
        message = f"🎉 Congratulations! 🎉\n\n"
        message += f"You completed the memory game!\n\n"
        message += f"📊 Your Stats:\n"
        message += f"• Moves: {self.moves}\n"
        message += f"• Time: {elapsed_time}s\n"
        message += f"• Pairs: {len(self.matched_pairs)}"
        result = messagebox.askquestion("Game Complete!",
                                        message + "\n\nWould you like to play again?")
        if result == 'yes':
            self.reset_game()
        else:
            self.return_to_main_menu()

    def reset_game(self):
        self.flipped_cards = []
        self.matched_pairs = set()
        self.moves = 0
        self.start_time = time.time()
        self.setup_game()

    def return_to_main_menu(self):
        self.root.title(self.original_title)
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Thanks for playing!\n\nReturning to main menu...",
                 font=("Helvetica", 16), bg=self.colors['cream'],
                 fg=self.colors['dark_green']).pack(expand=True)

    def create_control_buttons(self):
        control_frame = tk.Frame(self.root, bg=self.colors['cream'], pady=20)
        control_frame.pack()
        button_font = font.Font(family="Helvetica", size=11, weight="bold")

        # Reset button with card styling
        reset_frame = tk.Frame(control_frame,
                               bg=self.colors['brown'],
                               relief='flat', bd=0)
        reset_frame.pack(side='left', padx=15)

        reset_inner = tk.Frame(reset_frame,
                               bg=self.colors['sage'],
                               relief='flat', bd=0)
        reset_inner.pack(expand=True, fill='both', padx=3, pady=3)

        reset_btn = tk.Button(reset_inner,
                              text="🔄 New Game",
                              font=button_font,
                              bg=self.colors['sage'],
                              fg=self.colors['dark_green'],
                              activebackground=self.colors['lime'],
                              activeforeground=self.colors['dark_green'],
                              relief='flat',
                              bd=0,
                              padx=20,
                              pady=8,
                              cursor='hand2',
                              command=self.reset_game)
        reset_btn.pack(expand=True, fill='both', padx=2, pady=2)

        # Back button with card styling
        back_frame = tk.Frame(control_frame,
                              bg=self.colors['brown'],
                              relief='flat', bd=0)
        back_frame.pack(side='right', padx=15)

        back_inner = tk.Frame(back_frame,
                              bg=self.colors['sage'],
                              relief='flat', bd=0)
        back_inner.pack(expand=True, fill='both', padx=3, pady=3)

        back_btn = tk.Button(back_inner,
                             text="← Back to Menu",
                             font=button_font,
                             bg=self.colors['sage'],
                             fg=self.colors['dark_green'],
                             activebackground=self.colors['lime'],
                             activeforeground=self.colors['dark_green'],
                             relief='flat',
                             bd=0,
                             padx=20,
                             pady=8,
                             cursor='hand2',
                             command=self.return_to_main_menu)
        back_btn.pack(expand=True, fill='both', padx=2, pady=2)

        # Add hover effects to buttons
        def add_button_hover(button, inner_frame, normal_bg=None):
            if normal_bg is None:
                normal_bg = self.colors['sage']
            def on_enter(e):
                button.configure(bg=self.colors['lime'])
                inner_frame.configure(bg=self.colors['lime'])
            def on_leave(e):
                button.configure(bg=normal_bg)
                inner_frame.configure(bg=normal_bg)
            button.bind('<Enter>', on_enter)
            button.bind('<Leave>', on_leave)
        add_button_hover(reset_btn, reset_inner)
        add_button_hover(back_btn, back_inner)

    def update_timer(self):
        if hasattr(self, 'time_label'):
            elapsed_time = int(time.time() - self.start_time)
            self.time_label.config(text=f"Time: {elapsed_time}s")
            if not self.is_game_won():
                self.root.after(1000, self.update_timer)

# Example usage for testing
if __name__ == "__main__":
    sample_flashcards = [
        (1, "Hello", "Hola"),
        (2, "Goodbye", "Adiós"),
        (3, "Water", "Agua"),
        (4, "Food", "Comida"),
        (5, "House", "Casa"),
        (6, "Cat", "Gato"),
        (7, "Dog", "Perro"),
        (8, "Book", "Libro")
    ]
    root = tk.Tk()
    root.geometry("800x700")
    root.resizable(True, True)
    game = MemoryGame(root, sample_flashcards)
    root.mainloop()