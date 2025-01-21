import os
from turtle import Turtle

from snake import GAME_BOUNDARY

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
HIGH_SCORE_FILE = "snake_high_score.txt"

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.high_score = 0
    self.score = 0
    self.penup()
    self.clear_score_board()
    self.color("white")
    self.hideturtle()
    self.read_high_score()
    self.update_score_board()

  def clear_score_board(self):
    self.clear()
    self.goto(x=0, y=GAME_BOUNDARY + 5)

  def update_score_board(self):
    self.clear_score_board()
    self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

  def increment_score(self):
    self.score = self.score + 1
    self.update_score_board()
    
  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      self.save_high_score()
    
    self.score = 0
    self.update_score_board()
  
  def save_high_score(self):
    with open(HIGH_SCORE_FILE, "w") as file:
      file.write(str(self.high_score))
      
  def read_high_score(self):
    if os.path.isfile(HIGH_SCORE_FILE):
      with open("snake_high_score.txt", "r") as file:
        try:
          contents = file.read()
          score = int(contents)
        except:
          score = 0
        finally: 
          self.high_score = score
  
  def game_over(self):
    self.goto(x=0, y=0)
    self.write("Game Over", False, align=ALIGNMENT, font=FONT)
    self.goto(x=0, y=-20)
    self.write("Press Space to Restart", False, align=ALIGNMENT, font=FONT)
