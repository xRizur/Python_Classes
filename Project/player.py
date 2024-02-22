import pygame
from maze import Wall
RED = (255, 0, 0)
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, maze):
        if direction == Wall.TOP and not maze.cells[self.x][self.y].walls[Wall.TOP]:
            self.y -= 1
        elif direction == Wall.BOTTOM and not maze.cells[self.x][self.y].walls[Wall.BOTTOM]:
            self.y += 1
        elif direction == Wall.LEFT and not maze.cells[self.x][self.y].walls[Wall.LEFT]:
            self.x -= 1
        elif direction == Wall.RIGHT and not maze.cells[self.x][self.y].walls[Wall.RIGHT]:
            self.x += 1

    def draw(self, screen, cell_size):
        player_x = self.x * cell_size + cell_size // 2
        player_y = self.y * cell_size + cell_size // 2
        pygame.draw.circle(screen, RED, (player_x, player_y), cell_size // 3)
