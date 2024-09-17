import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox

class RockPaperScissorsGame(QWidget):
    def __init__(self):
        super().__init__()
        
        self.user_score = 0
        self.computer_score = 0
        
        self.setWindowTitle('Rock-Paper-Scissors Game')
        self.setGeometry(100, 100, 300, 200)

        self.result_label = QLabel("Make your choice:",self)
        
        self.rock_button = QPushButton("Rock", self)
        self.rock_button.clicked.connect(lambda: self.play_round("Rock"))
        
        self.paper_button = QPushButton("Paper", self)
        self.paper_button.clicked.connect(lambda: self.play_round("Paper"))
        
        self.scissors_button = QPushButton("Scissors", self)
        self.scissors_button.clicked.connect(lambda: self.play_round("Scissors"))
        
        self.score_label = QLabel(f"Score: You {self.user_score} - Computer {self.computer_score}", self)
        
        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        layout.addWidget(self.rock_button)
        layout.addWidget(self.paper_button)
        layout.addWidget(self.scissors_button)
        layout.addWidget(self.score_label)
        
        self.setLayout(layout)
        
    def play_round(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)
        
        if result == "Win":
            self.user_score += 1
            message = "You win!"
        elif result == "Lose":
            self.computer_score += 1
            message = "You lose!"
        else:
            message = "It's a tie!"
        
        self.result_label.setText(f"You chose {user_choice}, computer chose {computer_choice}. {message}")
        self.score_label.setText(f"Score: You {self.user_score} - Computer {self.computer_score}")
        
        self.ask_play_again()

    def determine_winner(self, user, computer):
        if user == computer:
            return "Tie"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Paper" and computer == "Rock") or \
             (user == "Scissors" and computer == "Paper"):
            return "Win"
        else:
            return "Lose"
    
    def ask_play_again(self):
        reply = QMessageBox.question(self, 'Play Again', 'Do you want to play another round?', 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if reply == QMessageBox.No:
            self.close()

def main():
    app = QApplication(sys.argv)
    game = RockPaperScissorsGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
