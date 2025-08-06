import sqlite3
import os

class FlashcardManager:
    def __init__(self, db_path='db/flashcards.db'):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)  # Ensure db directory exists
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the flashcards table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                term TEXT NOT NULL,
                translation TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_flashcard(self, term, translation):
        """Inserts a new flashcard into the database."""
        self.cursor.execute('''
            INSERT INTO flashcards (term, translation)
            VALUES (?, ?)
        ''', (term, translation))
        self.conn.commit()

    def delete_flashcard(self, flashcard_id):
        """Deletes a flashcard by its ID."""
        self.cursor.execute('''
            DELETE FROM flashcards
            WHERE id = ?
        ''', (flashcard_id,))
        self.conn.commit()

    def get_all_flashcards(self):
        """Retrieves all flashcards from the database."""
        self.cursor.execute('SELECT * FROM flashcards')
        return self.cursor.fetchall()

    def update_flashcard(self, flashcard_id, new_term, new_translation):
        """Updates an existing flashcard with new term and translation."""
        self.cursor.execute('''
            UPDATE flashcards
            SET term = ?, translation = ?
            WHERE id = ?
        ''', (new_term, new_translation, flashcard_id))
        self.conn.commit()

    def get_flashcard_by_id(self, flashcard_id):
        """Retrieves a single flashcard by its ID."""
        self.cursor.execute('''
            SELECT * FROM flashcards
            WHERE id = ?
        ''', (flashcard_id,))
        return self.cursor.fetchone()

    def close(self):
        """Closes the database connection."""
        self.conn.close()
