# FlashPlay

## Description:
FlashPlay is a gamified learning app. Players start by importing or creating a deck of flashcards, which becomes the foundation for a series of interactive minigames. In total you can choose between three different mini games: 
1. Memory Game: The flashcards are upside-down and youu have to find the matching pairs <br>
<img width="300" alt="Bildschirmfoto 2025-07-01 um 15 47 53" src="https://github.com/user-attachments/assets/ba6eef85-ba0f-4735-b7bb-6f6f41920889" /> <br>
3. Snake Race: You race against a timed snake. If you answer the question correctly you get faster, if you answer incorrectly your snake gets slower<br>
<img width="330" alt="Bildschirmfoto 2025-07-01 um 16 00 17" src="https://github.com/user-attachments/assets/9eb5c364-da85-42a0-b81f-a1e58544c20c" /><br>
4. Package Sorter: On a production line small "Packages" with the front and back of a flashcards comes rolling in and you have to see if the back and fronts matches. If front and back matches it can go into dilivery if it is wron it needs to be picked up from the production line<br>
<img width="677" alt="Bildschirmfoto 2025-07-01 um 15 57 55" src="https://github.com/user-attachments/assets/8fb1f554-6f50-4c08-978a-8bdc947dce94" /><br>

## Installation
### Libraries:
1. Pygame for drawing minigames, GUI, game loops, event handling
2. random
3. time
4. os/ sys for running main file and handling paths files
5. json for saving/ loading user progress or custom decks

### file structure:
FlashPlay/<br>
├── flashplay.py   <br>
├── memory_game.py <br>
├── snake_race.py  <br>
├── package_sorter.py  <br>
├── deck.py  <br>
├── ui.py    <br>
├── media/    <br>
│    ├── images/<br>
│    ├── sounds/<br>
│    └── fonts/<br>
├── requirements.txt   <br>
├── README.md   <br>
├── documentation.md     .<br>
└── .gitignore<br>

## usage
run from terminal
python flashplay.py


