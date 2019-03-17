
import unittest
from typing import List, Union
from copy import deepcopy

from game import read_state, write_state
from life import Grid, Generation, Cell, Coordinates, GridWindow, COMMENT_CHAR


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


class TestSpaceships(unittest.TestCase):

    initial_state_header = "{c} Initial:".format(c=COMMENT_CHAR)
    final_state_header = "{c} Final:".format(c=COMMENT_CHAR)

    def test_glider(self):
        print("")
        print("Glider Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (x == 1 and y == 2)
                            or (x == 2 and y == 3)
                            or (x == 3 and y in [1, 2, 3])
                        else False
                    )
                    for x in range(6)
                ]
                for y in range(6)
            ]
        )
        print(grid)
        initial_glider = GridWindow(grid=grid, x_offset=0, y_offset=0, x_max=5, y_max=5)
        initial_glider_str = str(Grid(cells=initial_glider.contents))
        generation = Generation(grid)
        for i in range(3):
            print(generation)
            generation = Generation(generation.grid, generation.generation_number)
        print(generation)
        final_glider = GridWindow(grid=generation.grid, x_offset=1, y_offset=1, x_max=6, y_max=6)
        final_glider_str = str(Grid(cells=final_glider.contents))
        print("")
        print(self.initial_state_header)
        print(initial_glider)
        print("")
        print(self.final_state_header)
        print(final_glider)
        self.assertEqual(initial_glider_str, final_glider_str)

    def test_lightweight(self):
        print("")
        print("Lightweight Spaceship Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (x == 1 and y == 1)
                            or (x == 4 and y == 1)
                            or (x == 1 and y == 3)
                            or (y == 4 and x in [2, 3, 4, 5])
                            or (x == 5 and y in [2, 3])
                        else False
                    )
                    for x in range(9)
                ]
                for y in range(6)
            ]
        )
        print(grid)
        initial_lwss = GridWindow(grid=grid, x_offset=0, y_offset=0, x_max=7, y_max=6)
        initial_lwss_str = str(Grid(cells=initial_lwss.contents))
        generation = Generation(grid)
        for i in range(3):
            print(generation)
            generation = Generation(generation.grid, generation.generation_number)
        print(generation)
        final_lwss = GridWindow(grid=generation.grid, x_offset=2, y_offset=0, x_max=9, y_max=6)
        final_lwss_str = str(Grid(cells=final_lwss.contents))
        print("")
        print(self.initial_state_header)
        print(initial_lwss)
        print("")
        print(self.final_state_header)
        print(final_lwss)
        self.assertEqual(initial_lwss_str, final_lwss_str)

    def test_midweight(self):
        print("")
        print("Midweight Spaceship Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (x == 3 and y == 1)
                            or (x in [1, 5] and y == 2)
                            or (x == 1 and y == 4)
                            or (x == 6 and y in [3, 4, 5])
                            or (y == 5 and x in [2, 3, 4, 5])
                        else False
                    )
                    for x in range(10)
                ]
                for y in range(9)
            ]
        )
        print(grid)
        initial_mwss = GridWindow(grid=grid, x_offset=0, y_offset=0, x_max=8, y_max=7)
        initial_mwss_str = str(Grid(cells=initial_mwss.contents))
        generation = Generation(grid)
        for i in range(3):
            print(generation)
            generation = Generation(generation.grid, generation.generation_number)
        print(generation)
        final_mwss = GridWindow(grid=generation.grid, x_offset=2, y_offset=0, x_max=10, y_max=7)
        final_mwss_str = str(Grid(cells=final_mwss.contents))
        print("")
        print(self.initial_state_header)
        print(initial_mwss)
        print("")
        print(self.final_state_header)
        print(final_mwss)
        self.assertEqual(initial_mwss_str, final_mwss_str)

    def test_heavyweight(self):
        print("")
        print("Heavyweight Spaceship Test")
        grid = Grid(
            cells=[
                [
                    Cell(
                        Coordinates(x,y),
                        True
                        if (x in [3, 4] and y == 1)
                            or (x in [1, 6] and y == 2)
                            or (x == 7 and y in [3, 4, 5])
                            or (x == 1 and y == 4)
                            or (y == 5 and x in [2, 3, 4, 5, 6])
                        else False
                    )
                    for x in range(11)
                ]
                for y in range(9)
            ]
        )
        print(grid)
        initial_hwss = GridWindow(grid=grid, x_offset=0, y_offset=0, x_max=9, y_max=7)
        initial_hwss_str = str(Grid(cells=initial_hwss.contents))
        generation = Generation(grid)
        for i in range(3):
            print(generation)
            generation = Generation(generation.grid, generation.generation_number)
        print(generation)
        final_hwss = GridWindow(grid=generation.grid, x_offset=2, y_offset=0, x_max=11, y_max=7)
        final_hwss_str = str(Grid(cells=final_hwss.contents))
        print("")
        print(self.initial_state_header)
        print(initial_hwss)
        print("")
        print(self.final_state_header)
        print(final_hwss)
        self.assertEqual(initial_hwss_str, final_hwss_str)


class GameIOTestUtils:

    def create_file(self, path: str, data: List[Union[List[Cell], str]]) -> None:
        with open(path, 'w') as file:
            for line in deepcopy(data):
                if type(line) == str:
                    file.write("{0}\n".format(line))
                else:
                    file.write("{0}\n".format(str(Grid(cells=[line]))))


class TestGameIO(unittest.TestCase):

    test_data = [
        [
            Cell(
                Coordinates(x, y),
                True
                if x == 2 and y > 0 and y < 4
                else False
            )
            for x in range(5)
        ]
        for y in range(5)
    ]

    first_file = '/tmp/cgol_test_1.txt'
    second_file = '/tmp/cgol_test_2.txt'

    def test_file_read(self):
        print("")
        print("Basic File Read Test")
        GameIOTestUtils().create_file(path=self.first_file, data=self.test_data)
        read_grid = read_state(in_file=self.first_file)
        print(read_grid)
        print("=============")
        print(Grid(cells=self.test_data))
        print("")
        self.assertEqual(str(read_grid), str(Grid(cells=self.test_data)))

    def test_file_read_comments(self):
        print("")
        print("Basic File with Comment Read Test")
        data = deepcopy(self.test_data)
        data = ["# Hello, this is a comment"] + data[:2] + ["#..*.."] + data[2:]
        GameIOTestUtils().create_file(path=self.first_file, data=data)
        read_grid = read_state(in_file=self.first_file)
        print(read_grid)
        print("=============")
        print(Grid(cells=self.test_data))
        print("")
        self.assertEqual(str(read_grid), str(Grid(cells=self.test_data)))

    def test_file_write_then_read(self):
        print("")
        print("Basic File Write and Read Back Test")
        generation = Generation(grid=Grid(cells=self.test_data), steps=0)
        write_state(final_state=generation, out_file=self.first_file)
        read_grid = read_state(in_file=self.first_file)
        print(read_grid)
        print("=============")
        print(generation)
        print("")
        self.assertEqual(str(read_grid), str(generation.grid))


if __name__ == '__main__':
    unittest.main()
