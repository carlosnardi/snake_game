from turtle import Turtle

class NewSnake:
  def __init__(self):
    initial_position = [(0,0),(-20,0),(-40,0)]
    self.segments = []
    for position in initial_position:
      self.snake = Turtle(shape="square")
      self.snake.penup()
      self.snake.color("white")
      self.snake.goto(position)
      self.snake.speed('slowest')
      self.segments.append(self.snake)

  def move_forward(self):
    for self.seg in self.segments:
      self.seg.forward(1)
      
  
  def turn_left(self):
    for self.seg in self.segments:
      angle = self.snake.heading()
      self.snake.setheading(angle - 90)

  def turn_right(self):
    for self.seg in self.segments:
      angle = self.snake.heading()
      self.snake.setheading(angle + 90)
    
    
