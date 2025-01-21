from turtle import Turtle


class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.color("purple")
    self.penup()
    self.setheading(90)
    self.reposition()
    self.speed(0)
  
  def reposition(self):
    self.goto(0, -280)
  
  def move(self):
    self.forward(10)
  
  def has_crossed(self):
    if self.ycor() > 250:
      return True
    return False