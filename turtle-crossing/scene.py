from turtle import Turtle

SIDEWALK = "bisque"
SIDEWALK_WIDTH = 70

class Scene():
  def __init__(self):
    self.turtle = Turtle()
    self.turtle.speed(0)
    self.turtle.hideturtle()
    self.draw_sidewalk(-300, 260)
    self.draw_sidewalk(-300, -250)
    self.draw_crossing()
    
  def draw_sidewalk(self, x_cor, y_cor):
    self.turtle.color(SIDEWALK)
    self.turtle.penup()
    self.turtle.goto(x_cor, y_cor)
    self.turtle.pendown()
    self.turtle.begin_fill()
    
    for _ in range(2):
      self.turtle.forward(600)
      self.turtle.right(90)
      self.turtle.forward(10)
      self.turtle.right(90)

    self.turtle.end_fill()
    self.turtle.penup()
  
  def draw_crossing(self):
    self.turtle.color("white")
    self.turtle.goto(-SIDEWALK_WIDTH/2, 230)

    for _ in range(12):
      self.turtle.pendown()
      self.turtle.begin_fill()

      for _ in range(2):
        self.turtle.forward(SIDEWALK_WIDTH)
        self.turtle.right(90)
        self.turtle.forward(20)
        self.turtle.right(90)

      self.turtle.end_fill()
      self.turtle.penup()
      self.turtle.goto(-SIDEWALK_WIDTH/2, self.turtle.ycor() - 40)
