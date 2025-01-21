from turtle import Turtle

FONT = ("Courier", 16, "normal")
ALIGN = "center"

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("black")
    self.penup()
    self.hideturtle()
    self.goto(-230, 260)
    self.level = 1
    self.display_level()
  
  def display_level(self):
    self.clear()
    self.write("Level: " + str(self.level), align=ALIGN, font=FONT)
  
  def increment_level(self):
    self.level = self.level + 1
    self.display_level()

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER!", align=ALIGN, font=FONT)
