import tkinter as tk
from tkinter import messagebox, simpledialog
from flashcards import FlashcardManager
from game_memory import MemoryGame
from game_race import RaceGame

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Vocabulary Flashcards")
        self.flashcard_manager = FlashcardManager()
        self.setup_main_menu()

    def setup_main_menu(self):
        """Sets up the main menu interface."""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Vocabulary Flashcards", font=("Helvetica", 18, "bold")).pack(pady=10)

        tk.Button(self.root, text="Play Memory Game", width=25, command=self.launch_memory_game).pack(pady=5)
        tk.Button(self.root, text="Play Race Game", width=25, command=self.launch_race_game).pack(pady=5)

        tk.Button(self.root, text="Manage Flashcards", width=25, command=self.manage_flashcards).pack(pady=5)
        tk.Button(self.root, text="Exit", width=25, command=self.root.quit).pack(pady=20)

    def launch_memory_game(self):
        flashcards = self.flashcard_manager.get_all_flashcards()
        if flashcards:
            MemoryGame(self.root, flashcards)  # Pass root or Toplevel
        else:
            messagebox.showinfo("No Flashcards", "Add flashcards before playing.")

    def launch_race_game(self):
        flashcards = self.flashcard_manager.get_all_flashcards()
        if flashcards:
            RaceGame(self.root, flashcards)  # Same structure as MemoryGame
        else:
            messagebox.showinfo("No Flashcards", "Add flashcards before playing.")

    def manage_flashcards(self):
        """Displays flashcard management UI."""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Manage Flashcards", font=("Helvetica", 16)).pack(pady=10)

        flashcards = self.flashcard_manager.get_all_flashcards()
        for fc in flashcards:
            frame = tk.Frame(self.root)
            frame.pack(pady=2)

            tk.Label(frame, text=f"{fc[0]}. {fc[1]} → {fc[2]}", width=40, anchor="w").pack(side="left")

            tk.Button(frame, text="Edit", command=lambda f=fc: self.edit_flashcard(f)).pack(side="left", padx=5)
            tk.Button(frame, text="Delete", command=lambda f=fc: self.delete_flashcard(f[0])).pack(side="left")

        tk.Button(self.root, text="Add New Flashcard", command=self.add_flashcard).pack(pady=10)
        tk.Button(self.root, text="Back to Main Menu", command=self.setup_main_menu).pack(pady=5)

    def add_flashcard(self):
        term = simpledialog.askstring("Add Flashcard", "Enter term:")
        if not term:
            return
        translation = simpledialog.askstring("Add Flashcard", "Enter translation:")
        if not translation:
            return
        self.flashcard_manager.add_flashcard(term, translation)
        self.manage_flashcards()

    def edit_flashcard(self, flashcard):
        new_term = simpledialog.askstring("Edit Flashcard", "Edit term:", initialvalue=flashcard[1])
        if not new_term:
            return
        new_translation = simpledialog.askstring("Edit Flashcard", "Edit translation:", initialvalue=flashcard[2])
        if not new_translation:
            return
        self.flashcard_manager.update_flashcard(flashcard[0], new_term, new_translation)
        self.manage_flashcards()

    def delete_flashcard(self, flashcard_id):
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this flashcard?")
        if confirm:
            self.flashcard_manager.delete_flashcard(flashcard_id)
            self.manage_flashcards()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()


