import random
from turtle import Turtle

COLOURS = ["chocolate", "sky blue", "green", "olive drab", "deep pink", "yellow", "blue", "green yellow", "violet", "orange red"]
MOVE_DISTANCE = 10
X_START = 300
X_END = -300

class TrafficManager():
  def __init__(self):
    super().__init__()
    self.cars = []
    self.move_speed = MOVE_DISTANCE
  
  def create_car(self):
    car = Car(x_cor=X_START, y_cor=random.randint(-240, 240))
    self.cars.append(car)
  
  def move_cars(self):
    for car in self.cars:
      car.drive(self.move_speed)

  def remove_traffic(self):
    new_cars = []

    for car in self.cars:
      if car.xcor() > -300:
        new_cars.append(car)
    
    self.cars = new_cars

  def increase_speed(self):
    self.move_speed += 5
  
class Car(Turtle):
  def __init__(self, x_cor, y_cor):
    super().__init__()
    self.color(random.choice(COLOURS))
    self.setheading(180)
    self.penup()
    self.shape("square")
    self.shapesize(stretch_wid=1, stretch_len=2)
    self.goto(x_cor, y_cor)
  
  def drive(self, speed):
    self.forward(speed)
