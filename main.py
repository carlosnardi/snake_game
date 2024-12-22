from turtle import Turtle, Screen 
from snake import NewSnake

screen = Screen()
screen.title("Snake Game")
screen.screensize(canvwidth=400,canvheight=400,bg="black")

snake = NewSnake()
#snake.grow(10)


screen.listen()
screen.onkey(fun=snake.move_forward,key="w")
screen.onkey(fun=snake.turn_left,key="a")
screen.onkey(fun=snake.turn_right,key="d")



screen.mainloop()