from turtle import Turtle

GAME_BOUNDARY = 275
COLLISION_DISTANCE = 10
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
  def __init__(self):
    self.body = []
    self.create_snake()
    self.head = self.body[0]

  def create_snake(self):
    for i in range(3):
      self.add_segment(STARTING_POSITIONS[i])

  def add_segment(self, position):
    t = Turtle("square")
    t.color("white")
    t.penup()
    t.goto(position)
    self.body.append(t)
  
  def extend(self):
    self.add_segment(self.body[-1].position())
    
  def move(self):
    for seg_num in range(len(self.body) - 1, 0, -1):
      new_x = self.body[seg_num - 1].xcor()
      new_y = self.body[seg_num - 1].ycor()
      self.body[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)
  
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)

  def has_collided_with_wall(self):
    if self.head.xcor() > GAME_BOUNDARY or self.head.xcor() < -GAME_BOUNDARY or self.head.ycor() > GAME_BOUNDARY or self.head.ycor() < -GAME_BOUNDARY:
      return True
    return False
  
  def has_collided_with_tail(self):
    for segment in self.body[1:]:
      if self.head.distance(segment) < COLLISION_DISTANCE:
        return True
    return False
  
  def has_collided(self):
    if self.has_collided_with_wall() or self.has_collided_with_tail():
      return True
    return False
  
  def reset(self):
    for segment in self.body:
      segment.goto(1000, 1000)
      
    self.body.clear()
    self.create_snake()
    self.head = self.body[0]
