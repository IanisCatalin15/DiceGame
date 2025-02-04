Virtual Dice Game 🎲
This is a Python-based virtual dice game designed to help players play social games like Monopoly, Board games, or any other dice-based games without the need for physical dice. Simply input the number of players, roll the dice, and let the game begin!

Features 🌟
Roll the dice virtually: Players can roll a 6-sided die by interacting with the program.
Handles tied rolls: If two or more players roll the same number, the program re-rolls until a winner is determined.
Keeps players in the game: Players who lose in a re-roll are not removed—they simply get re-ordered and continue playing.
Player management: Players can choose whether they want to continue the game. Those who wish to leave the game are removed, but those who lose in a tie remain part of the game and get re-ordered.
Game Restart Option: After the game ends, you have the option to restart and play again.
How to Use 💻
Requirements 📝
Python 3.x
No additional libraries are required. The program uses standard Python libraries like random and time.
Steps to Run 🚀
Clone or download this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/virtual-dice-game.git
Navigate to the directory where the file is stored.

Run the game by executing the Python script:

bash
Copy
Edit
python dice_game.py
Play the game:

The program will prompt you to enter the number of players and their names.
Once all players have entered, the dice roll will happen.
The player with the highest roll will go first, and if there are ties, those players will re-roll until there is a winner.
Players can choose whether they want to continue after each round.
Restart the game if you'd like to play again after it ends.
