import turle
import random

w = 500
h =500
food_size = 10
delay = 100

offsets = {
    "up": (0, 20),
    "down": (0,-20),
    "right": (20, 0)

}


def reset():
    global snake, snake_dir, food_position, pen
    snake = [[0, 0], [0, 20], [0, 40], [0,60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food-position)
    move_snake()

    def move_snake():
        global snake_dir

        new_head = snake [-1].copy()
        new_head[0] = snake[-1][0] + offsets[snake_dir][0]
        neww_heade[1] = snake [-1][1] + offsets[snake_dir][1]
    
