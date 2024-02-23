import unittest
from main import Cell, Wall,Player,DisjointSet
class TestMaze(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(10, 10,2)

    def test_maze_initialization(self):
        self.assertEqual(len(self.maze.cells), 10, "Maze should have 10 rows")
        self.assertEqual(len(self.maze.cells[0]), 10, "Each row in the maze should have 10 cells")

    #def test_maze_generation(self):
       # self.maze.generate()

class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell = Cell(0, 0)

    def test_initial_walls(self):
        self.assertTrue(all(self.cell.walls.values()), "Początkowo wszystkie ściany powinny być obecne")

    def test_remove_wall(self):
        self.cell.remove_wall(Cell(0, 1), Wall.BOTTOM)
        self.assertFalse(self.cell.walls[Wall.BOTTOM], "Powinno usunąć dolną ścianę")
        self.assertTrue(self.cell.walls[Wall.TOP], "Pozostałe ściany powinny pozostać nietknięte")

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(10, 10)
        self.player = Player(0, 0)

    def test_initial_position(self):
        self.assertEqual(self.player.x, 0)
        self.assertEqual(self.player.y, 0)

    def test_move(self):
        self.player.move(Wall.RIGHT, self.maze)
class TestDisjointSet(unittest.TestCase):
    def setUp(self):
        self.set = DisjointSet(10)

    def test_initial_parents(self):
        for i in range(10):
            self.assertEqual(self.set.find(i), i, "Initially, each element should be its own parent")

    def test_union_and_find(self):
        self.set.union(0, 1)
        self.assertEqual(self.set.find(1), self.set.find(0), "Elements 0 and 1 should be in the same set after union")

if __name__ == '__main__':
    unittest.main()

