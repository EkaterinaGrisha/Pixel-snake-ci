import sys
import pygame
from src.game import SnakeModel

CELL = 24
MARGIN = 2
BG = (25, 25, 30)

def draw_cell(surface, img, x, y):
    px = x * (CELL + MARGIN) + MARGIN
    py = y * (CELL + MARGIN) + MARGIN
    if img:
        surface.blit(img, (px, py))
    else:
        pygame.draw.rect(surface, (200,200,200), pygame.Rect(px, py, CELL, CELL))

def load_assets():
    head = pygame.image.load('assets/snake_head.png').convert_alpha()
    body = pygame.image.load('assets/snake_body.png').convert_alpha()
    food = pygame.image.load('assets/food.png').convert_alpha()
    # scale to cell size
    head = pygame.transform.scale(head, (CELL, CELL))
    body = pygame.transform.scale(body, (CELL, CELL))
    food = pygame.transform.scale(food, (CELL, CELL))
    return head, body, food

def main():
    pygame.init()
    model = SnakeModel(width=20, height=15, init_length=4)
    width_px = model.width * (CELL + MARGIN) + MARGIN
    height_px = model.height * (CELL + MARGIN) + MARGIN
    screen = pygame.display.set_mode((width_px, height_px))
    clock = pygame.time.Clock()
    head_img, body_img, food_img = load_assets()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    model.set_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    model.set_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    model.set_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    model.set_direction(1, 0)
        model.step()
        if not model.alive:
            print('Game over')
            pygame.time.wait(1000)
            pygame.quit(); sys.exit()

        screen.fill(BG)
        # draw food
        if model.food:
            fx, fy = model.food
            draw_cell(screen, food_img, fx, fy)
        # draw snake
        for i, (x,y) in enumerate(model.snake):
            img = head_img if i==0 else body_img
            draw_cell(screen, img, x, y)

        pygame.display.flip()
        clock.tick(6)

if __name__ == '__main__':
    main()
