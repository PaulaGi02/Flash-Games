# FlashPlay

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDSVal2ctLp9z5koMXiOIA2iryJXrAHxNoMKT9+mvsiQgfG4U/b1E+IToyXzw5v38eRNnLcjwMVa7y1K7lfapySjL58wKgN8NP45r+RjeH6aOYGf2OSrv1yGICYHeSwHsgFG0DPcnQPgUQextKKkowE0vVFEocDpcOPtNFDLbNe9wq1c8oCkbcNQLGTkRvWlQF72tbvcxG92k2hIOMQVp/8HIdnBmzAyPPmIzzSSb0oZxM48rEEIWLi6UP8GHC1P9tcltCzr0MjhoGoJlLSjLSP7b+cRRZi5WjbchpbfnG62EEtLutqFuu7bvWRgc3LkQdlbU8oXS9tNd+HuNH5JuxQ+WcP0dq77XJhHylipvh5RstipDgQW27MjFyGkkNClyR2ixq0by51/lX6c+1nx3Sw1uKim2tw94uoFvPg30l89shFeQbJx6CpjDx8fV3aC4n8zC1WH1t0RoT2kr2CCl//0WGGaovEQIi7J9Ex/a2J2uuiVmZ0y5maHmBmMxYFjawnSC5/bx8DZc/iTf5sIZqSAX3tsPHNmPcatVq+apwcGNFj7N+0GEID7S1ewgRDmRt6Ohh2VYpy7Yk7QznABDg+tYKKtcpqm08/5x5WfFO1QW4UriIEdy2xdmtHgboJZFcYnLlsm3g+w8HnLt6CTPx6JFW0Ox3YWY6PphuydnXT4w== frieda.schuetze@stud.leuphana.de

## Description:
FlashPlay is a gamified vocabulary learning app. Players start by importing or creating a deck of flashcards, which becomes the foundation for a series of interactive minigames. In total you can choose between three different mini games: 
1. Memory Game: The flashcards are upside-down and youu have to find the matching pairs <br>
<img width="300" alt="Bildschirmfoto 2025-07-01 um 15 47 53" src="https://github.com/user-attachments/assets/ba6eef85-ba0f-4735-b7bb-6f6f41920889" /> <br>
3. Snake Race: You race against a timed snake. If you answer the question correctly you get faster, if you answer incorrectly your snake gets slower<br>
<img width="330" alt="Bildschirmfoto 2025-07-01 um 16 00 17" src="https://github.com/user-attachments/assets/9eb5c364-da85-42a0-b81f-a1e58544c20c" /><br>

## Installation
### Libraries:
1. Pygame for drawing minigames, GUI, game loops, event handling
2. random
3. time
4. os/ sys for running main file and handling paths files
5. json for saving/ loading user progress or custom decks

### file structure:
vocab_flashcards/ 

├── main.py <br>
├── flashcards.py <br>
├── game_memory.py <br>
├── game_race.py <br>
├── media/ <br>
│   ├── images/ <br>
│   └── sounds/    <br>
├── DB/ <br>
│   └── flashcards.db    <br>
├── requirements.txt   <br>
├── README.md   <br>
├── LICENCE  <br>
├── documentation.md     .<br>
└── .gitignore<br>

## usage
run from terminal
python flashplay.py


