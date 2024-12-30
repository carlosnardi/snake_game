from turtle import Screen 
from snake import NewSnake
import time

screen = Screen()
screen.title("Snake Game")
screen.screensize(canvwidth=400,canvheight=400,bg="black")
screen.tracer(0)

snake = NewSnake()

game_is_on = True

while game_is_on:
  snake.move_forward()  
  screen.update()
  time.sleep(0.1)
  screen.listen()
  screen.onkey(fun=snake.turn_left,key="a")
  screen.onkey(fun=snake.turn_right,key="d")



  
screen.mainloop()
