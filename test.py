
import unittest

from life import Grid, Generation, Cell, Coordinates


class TestStillLifesGameOfLife(unittest.TestCase):

    def test_block(self):
        print("")
        print("Block Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (x in [1, 2] and y in [1, 2])
                        else False
                    )
                    for x in range(4)
                ]
                for y in range(4)
            ]
        )
        print(grid)
        generation = Generation(grid)
        print(generation)
        self.assertEqual(str(grid), str(generation.grid))

    def test_beehive(self):
        print("")
        print("Beehive Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (x in [2, 3] and y in [1, 3])
                            or (x in [1, 4] and y in [2])
                        else False
                    )
                    for x in range(6)
                ]
                for y in range(5)
            ]
        )
        print(grid)
        generation = Generation(grid)
        print(generation)
        self.assertEqual(str(grid), str(generation.grid))

    def test_loaf(self):
        print("")
        print("Beehive Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (x in [2, 3] and y in [1])
                            or (x in [4] and y in [2, 3])
                            or (
                                (x == 1 and y == 2)
                                or (x == 2 and y == 3)
                                or (x == 3 and y == 4)
                            )
                        else False
                    )
                    for x in range(6)
                ]
                for y in range(6)
            ]
        )
        print(grid)
        generation = Generation(grid)
        print(generation)
        self.assertEqual(str(grid), str(generation.grid))

    def test_boat(self):
        print("")
        print("Boat Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (x in [1, 2] and y in [1])
                            or (x in [1, 3] and y in [2])
                            or (x == 2 and y == 3)
                        else False
                    )
                    for x in range(5)
                ]
                for y in range(5)
            ]
        )
        print(grid)
        generation = Generation(grid)
        print(generation)
        self.assertEqual(str(grid), str(generation.grid))

    def test_tub(self):
        print("")
        print("Tub Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (x in [1, 3] and y in [2])
                            or (y in [1, 3] and x in [2])
                        else False
                    )
                    for x in range(5)
                ]
                for y in range(5)
            ]
        )
        print(grid)
        generation = Generation(grid)
        print(generation)
        self.assertEqual(str(grid), str(generation.grid))

class TestOscillatorsGameOfLife(unittest.TestCase):

    def test_blinkers(self):
        print("")
        print("Blinker Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (x == 2 and y > 0 and y < 4)
                            or (y == 2 and x > 5 and x < 9)
                        else False
                    )
                    for x in range(10)
                ]
                for y in range(5)
            ]
        )
        print(grid)
        generation = Generation(grid)
        print(generation)
        generation2 = Generation(generation.grid, generation.generation_number)
        print(generation2)
        self.assertEqual(str(grid), str(generation2.grid))

    def test_toads(self):
        print("")
        print("Toad Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (y == 2 and x > 1 and x < 5)
                            or (y == 3 and x > 0 and x <  4)
                            or (x == 8 and y > 1 and y < 5)
                            or (x == 9 and y > 2 and y < 6)
                        else False
                    )
                    for x in range(12)
                ]
                for y in range(7)
            ]
        )
        print(grid)
        generation = Generation(grid)
        print(generation)
        generation2 = Generation(generation.grid, generation.generation_number)
        print(generation2)
        self.assertEqual(str(grid), str(generation2.grid))

    def test_beacon(self):
        print("")
        print("Beacon Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (y in [1, 2] and x in [1, 2])
                            or (y in [3, 4] and x in [3, 4])
                        else False
                    )
                    for x in range(12)
                ]
                for y in range(6)
            ]
        )
        print(grid)
        generation = Generation(grid)
        print(generation)
        generation2 = Generation(generation.grid, generation.generation_number)
        print(generation2)
        self.assertEqual(str(grid), str(generation2.grid))

    def test_pulsar(self):
        print("")
        print("Pulsar Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (y in [2, 7, 9, 14] and x in [4, 5, 6, 10, 11, 12])
                            or (y in [4, 5, 6, 10, 11, 12] and x in [2, 7, 9, 14])
                        else False
                    )
                    for x in range(17)
                ]
                for y in range(17)
            ]
        )
        print(grid)
        generation = Generation(grid)
        print(generation)
        generation2 = Generation(generation.grid, generation.generation_number)
        print(generation2)
        generation3 = Generation(generation2.grid, generation2.generation_number)
        print(generation3)
        self.assertEqual(str(grid), str(generation3.grid))

    def test_i_column(self):
        print("")
        print("I-Column Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (y in [3, 6, 8, 9, 11, 14] and x in [4, 5, 6])
                            or (y in [4, 5, 12, 13] and x in [5])
                        else False
                    )
                    for x in range(11)
                ]
                for y in range(18)
            ]
        )
        print(grid)
        generation = Generation(grid)
        for i in range(14):
            print(generation)
            generation = Generation(generation.grid, generation.generation_number)
        print(generation)
        self.assertEqual(str(grid), str(generation.grid))


if __name__ == '__main__':
    unittest.main()
