from turtle import Turtle

class NewSnake:
  def __init__(self):
    self.snake = Turtle()
    self.snake.shape("square")
    self.snake.shapesize(stretch_wid=1,stretch_len=2)
    self.snake.fillcolor("white")
    # self.snake.tiltangle()

  def grow(self, size): #  need to study more
    self.snake.shapesize(stretch_wid=1,stretch_len=size)
    
  def move_forward(self):
    self.snake.forward(10)

  def turn_left(self):
    self.snake.left(90)

  def turn_right(self):
    self.snake.right(90)
    
