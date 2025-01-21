import time
from turtle import Screen

from player import Player
from scene import Scene
from score_board import ScoreBoard
from traffic_manager import TrafficManager


class TurtleCrossing():
  def __init__(self):
    self.screen = Screen()
    self.setup_screen()
    self.scene = Scene()
    self.player = Player()
    self.score_board = ScoreBoard()
    self.traffic_manager = TrafficManager()
    self.setup_listeners()
    self.game_is_on = True
    self.count = 0
  
  def setup_screen(self):
    self.screen.setup(width=600, height=600)
    self.screen.bgcolor("light gray")
    self.screen.title("Retro Turtle Crossing Game")
    self.screen.tracer(0)
  
  def setup_listeners(self):
    self.screen.listen()
    self.screen.onkey(self.player.move, "Up")
  
  def determine_level(self):
    if self.player.has_crossed():
      self.score_board.increment_level()
      self.traffic_manager.increase_speed()
      self.player.reposition()
  
  def manage_traffic(self):
    self.count += 1

    if self.count == 6:
      self.traffic_manager.create_car()
      self.count = 0
      
  def check_for_collision(self):
    for car in self.traffic_manager.cars:
      if self.player.distance(car) < 20:
        self.game_is_on = False
        self.score_board.game_over()

  def play(self):
    while self.game_is_on:
      time.sleep(0.1)
      self.screen.update()
      self.manage_traffic()
      self.traffic_manager.move_cars()
      self.check_for_collision()
      self.determine_level()
    
    self.screen.exitonclick()

game = TurtleCrossing()
game.play()
