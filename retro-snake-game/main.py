import time
from turtle import Screen, Turtle

from food import Food
from score_board import ScoreBoard
from snake import GAME_BOUNDARY, Snake


class RetroSnakeGame():
  def __init__(self):
    self.screen = Screen()
    self.setup_screen()
    self.setup_boundaries()
    self.snake = Snake()
    self.food = Food()
    self.score_board = ScoreBoard()
    self.setup_listeners()
    self.game_is_on = True

  def setup_screen(self):
    self.screen.setup(width=600, height=600)
    self.screen.bgcolor("black")
    self.screen.title("Retro Snake Game")
    self.screen.tracer(0)

  def setup_listeners(self):
    self.screen.listen()
    self.screen.onkey(self.snake.up, "Up")
    self.screen.onkey(self.snake.down, "Down")
    self.screen.onkey(self.snake.left, "Left")
    self.screen.onkey(self.snake.right, "Right")
    self.screen.onkey(self.restart_game, "space")

  def setup_boundaries(self):
    tim = Turtle()
    tim.pensize(1)
    tim.color("white")
    tim.penup()
    tim.goto(x=(-GAME_BOUNDARY + 5), y=(GAME_BOUNDARY - 5))
    tim.pendown()
    tim.hideturtle()

    for _ in range(4):
      tim.forward(GAME_BOUNDARY * 2 - 10)
      tim.right(90)
    
    self.screen.update()

  def restart_game(self):
    self.score_board.reset()
    self.snake.reset()
    self.game_is_on = True
    self.play()

  def update_snake_and_screen(self):
    self.screen.update()
    time.sleep(0.1)
    self.snake.move()

  def detect_collision_with_food(self):
    if self.snake.head.distance(self.food) < 20:
      self.score_board.increment_score()
      self.food.refresh()
      self.snake.extend()
  
  def detect_game_end(self):
    if self.snake.has_collided():
      self.game_is_on = False
      self.score_board.game_over()

  def play(self):
    while self.game_is_on:
      self.update_snake_and_screen()
      self.detect_collision_with_food()
      self.detect_game_end()
    
    self.screen.exitonclick()

game = RetroSnakeGame()
game.play()
