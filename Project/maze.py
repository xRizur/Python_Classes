import random
import pygame
from enum import Enum
WHITE = (255, 255, 255)

class Wall(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {Wall.TOP: True, Wall.RIGHT: True, Wall.BOTTOM: True, Wall.LEFT: True}
        self.visited = False

    def remove_wall(self, other, wall):
        self.walls[wall] = False
        if wall == Wall.TOP:
            other.walls[Wall.BOTTOM] = False
        elif wall == Wall.RIGHT:
            other.walls[Wall.LEFT] = False
        elif wall == Wall.BOTTOM:
            other.walls[Wall.TOP] = False
        elif wall == Wall.LEFT:
            other.walls[Wall.RIGHT] = False

class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell(x, y) for y in range(height)] for x in range(width)]

    def generate(self):
        sets = DisjointSet(self.width * self.height)
        # zapelnienie listy scian
        walls = []
        for x in range(self.width):
            for y in range(self.height):
                if x > 0:
                    walls.append(((x, y), (x - 1, y)))
                if y > 0:
                    walls.append(((x, y), (x, y - 1)))
        # losowe usuwanie scian az do momentu, kiedy wszystkie komorki beda polaczone
        # Za pomoca algorytmu kruskala
        # 1. Losowo wybierz sciane
        # 2. Jesli komorki oddzielone przez sciane naleza do roznych zbiorow, usun sciane i polacz zbiory
        # 3. Powtarzaj kroki 1 i 2 az wszystkie komorki beda polaczone
        while walls:
            wall = random.choice(walls)
            walls.remove(wall)

            cell1, cell2 = wall
            set1 = sets.find(cell1[0] * self.height + cell1[1])
            set2 = sets.find(cell2[0] * self.height + cell2[1])

            if set1 != set2:
                sets.union(set1, set2)
                if cell1[0] == cell2[0]:
                    if cell1[1] > cell2[1]:
                        self.cells[cell1[0]][cell1[1]].remove_wall(self.cells[cell2[0]][cell2[1]], Wall.TOP)
                    else:
                        self.cells[cell1[0]][cell1[1]].remove_wall(self.cells[cell2[0]][cell2[1]], Wall.BOTTOM)
                else:
                    if cell1[0] > cell2[0]:
                        self.cells[cell1[0]][cell1[1]].remove_wall(self.cells[cell2[0]][cell2[1]], Wall.LEFT)
                    else:
                        self.cells[cell1[0]][cell1[1]].remove_wall(self.cells[cell2[0]][cell2[1]], Wall.RIGHT)
            
            # Usuniecie scian przy koncu, umozliwienie wyjscia z kadej strony
            goal_x, goal_y = self.width - 1, self.height - 1
            self.cells[goal_x][goal_y].remove_wall(self.cells[goal_x - 1][goal_y], Wall.LEFT)
            self.cells[goal_x][goal_y].remove_wall(self.cells[goal_x][goal_y - 1], Wall.TOP) 
    def draw(self, screen, cell_size):
        for x in range(self.width):
            for y in range(self.height):
                cell = self.cells[x][y]
                cell_x, cell_y = x * cell_size, y * cell_size

                if cell.walls[Wall.TOP]:
                    pygame.draw.line(screen, WHITE, (cell_x, cell_y), (cell_x + cell_size, cell_y))
                if cell.walls[Wall.RIGHT]:
                    pygame.draw.line(screen, WHITE, (cell_x + cell_size, cell_y), (cell_x + cell_size, cell_y + cell_size))
                if cell.walls[Wall.BOTTOM]:
                    pygame.draw.line(screen, WHITE, (cell_x, cell_y + cell_size), (cell_x + cell_size, cell_y + cell_size))
                if cell.walls[Wall.LEFT]:
                    pygame.draw.line(screen, WHITE, (cell_x, cell_y), (cell_x, cell_y + cell_size))
