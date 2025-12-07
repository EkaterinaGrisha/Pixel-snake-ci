import unittest
from src.game import SnakeModel

class TestSnakeModel(unittest.TestCase):

    def test_initial_state(self):
        model = SnakeModel(width=10, height=8, init_length=3)
        state = model.get_state()
        self.assertTrue(state['food'] is not None)
        self.assertEqual(len(state['snake']), 3)
        self.assertTrue(state['alive'])

    def test_step_and_growth(self):
        model = SnakeModel(width=6, height=6, init_length=2)
        # put food directly in front of head
        head = model.snake[0]
        model.direction = (1, 0)
        model.food = (head[0] + 1, head[1])
        model.step()
        # should have grown by 1
        self.assertEqual(len(model.snake), 3)

    def test_wall_collision(self):
        model = SnakeModel(width=4, height=4, init_length=1)
        model.snake = [(3,1)]  # head at right edge
        model.direction = (1,0)
        model.step()
        self.assertFalse(model.alive)

    def test_self_collision(self):
        model = SnakeModel(width=5, height=5, init_length=4)
        # create a scenario where head collides with body
        model.snake = [(2,2),(1,2),(1,3),(2,3)]
        model.direction = (0,-1)  # move up into (2,1) no collision yet
        model.step()
        # now set direction left then down to collide
        model.set_direction(-1,0)
        model.step()
        model.set_direction(0,1)
        model.step()
        self.assertFalse(model.alive)

if __name__ == '__main__':
    unittest.main()
