import sqlite3

class FlashcardManager:
    def __init__(self, db_path='db/flashcards.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        # TODO: Create table if not exists
        pass

    def add_flashcard(self, term, translation):
        # TODO: Insert new flashcard into DB
        pass

    def delete_flashcard(self, flashcard_id):
        # TODO: Remove flashcard by ID
        pass

    def get_all_flashcards(self):
        # TODO: Retrieve all flashcards
        pass

    def update_flashcard(self, flashcard_id, new_term, new_translation):
        # TODO: Update existing flashcard
        pass
