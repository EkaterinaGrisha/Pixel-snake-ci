import random
from dataclasses import dataclass, field
from typing import List, Tuple

Point = Tuple[int, int]

@dataclass
class SnakeModel:
    width: int = 20
    height: int = 15
    init_length: int = 3
    snake: List[Point] = field(default_factory=list)
    direction: Point = (1, 0)  # moving right by default
    food: Point = None
    alive: bool = True

    def __post_init__(self):
        # center the snake horizontally, vertical middle
        mid_y = self.height // 2
        mid_x = self.width // 2
        self.snake = [(mid_x - i, mid_y) for i in range(self.init_length)]
        self.place_food()

    def place_food(self):
        empty = [(x, y) for x in range(self.width) for y in range(self.height) if (x, y) not in self.snake]
        if not empty:
            self.food = None
            return
        self.food = random.choice(empty)

    def set_direction(self, dx: int, dy: int):
        # prevent reversing directly
        if (dx, dy) == (-self.direction[0], -self.direction[1]):
            return
        self.direction = (dx, dy)

    def step(self):
        if not self.alive:
            return
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        # Check wall collision
        if not (0 <= new_head[0] < self.width and 0 <= new_head[1] < self.height):
            self.alive = False
            return
        # Check self collision
        if new_head in self.snake:
            self.alive = False
            return
        # Move snake
        self.snake.insert(0, new_head)
        if self.food and new_head == self.food:
            self.place_food()
        else:
            self.snake.pop()

    def get_state(self):
        return {
            'snake': list(self.snake),
            'food': self.food,
            'alive': self.alive,
            'direction': self.direction,
            'width': self.width,
            'height': self.height
        }
