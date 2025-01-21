import random
from turtle import Turtle

from snake import GAME_BOUNDARY


class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.color("purple")
    self.speed(0)
    self.refresh()
  
  def refresh(self):
    random_x = random.randint(-GAME_BOUNDARY + 15, GAME_BOUNDARY - 15)
    random_y = random.randint(-GAME_BOUNDARY + 15, GAME_BOUNDARY - 15)
    self.goto(random_x, random_y)
