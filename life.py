
from typing import List, NewType
from functools import reduce
from copy import deepcopy


ALIVE_CHAR = "*"
DEAD_CHAR = "."


class Coordinates:
    x = None
    y = None

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)


class Cell:
    coordinates = None
    alive = False

    def __init__(self, coordinates: Coordinates, alive: bool=False):
        self.coordinates = coordinates
        self.alive = alive

    def __str__(self) -> str:
        return ALIVE_CHAR if self.alive else DEAD_CHAR


class Grid:
    contents = None
    width = 0
    height = 0

    def __init__(self, cells: List[List[Cell]]=None, width: int=0, height: int=0):
        if cells is not None:
            self.contents = cells
        elif width > 0 and height > 0:
            self.contents = [
                [
                    Cell(coordinates=Coordinates(x=x, y=y)) for x in range(width)
                ] for y in range(height)
            ]
        else:
            raise ValueError("Neither a matrix of cells nor a width and height were provided.")
        self.width = min(map(lambda row: len(row), self.contents))
        self.height = len(self.contents)
        self.contents = [
            self.contents[row_idx][:self.width]
            for row_idx in range(self.height)
        ]

    def __str__(self) -> str:
        return reduce(
            lambda table, row: table + "\n" + row,
            map(lambda row: reduce(
                    lambda cells, cell: cells + str(cell), row, ""
                ),
                self.contents
            )
        )


GENERATION_FORMAT = '''
    generation = {num}
{table}
'''


class Generation:
    generation_number = None
    grid = None

    def __init__(self, grid: Grid=None, generation_number: int=0):
        if grid is not None:
            self.generation_number = generation_number + 1
            self.grid = self.step(grid=grid, steps=1)
        else:
            raise ValueError("Grid must be provided")

    def step(self, grid: Grid=None, steps: int=1) -> Grid:
        def evaluate_cell(x: int, y: int, max_x: int, max_y: int, alive: bool) -> bool:
            min_x, min_y = 0, 0
            x_minus = x - 1 if (x - 1) > min_x else x
            x_plus = x + 1 if (x + 1) < max_x else x
            y_minus = y - 1 if (y - 1) > min_y else y
            y_plus = y + 1 if (y + 1) < max_y else y
            valid_coordinates = {
                str(Coordinates(x_loop, y_loop))
                for y_loop in range(y_minus, y_plus + 1)
                    for x_loop in range(x_minus, x_plus + 1)
            }
            valid_coordinates = valid_coordinates - {str(Coordinates(x, y))}
            neighbors = list(
                filter(
                    lambda cell: cell.alive,
                    filter(
                        lambda cell: str(cell.coordinates) in valid_coordinates,
                        [
                            cell
                            for row in grid.contents
                                for cell in row
                        ]
                    )
                )
            )
            return len(neighbors) == 3 or (alive and len(neighbors) == 2)
        if grid is None:
            raise ValueError("A grid must be provided")
        if steps < 0:
            raise ValueError("A generation can not be used to calculate its ancestors")
        elif steps == 0:
            return grid
        elif steps == 1:
            result_grid = Grid(cells=deepcopy(grid.contents))
            cell_eval_criteria = {
                'max_x': min(map(lambda row: len(row), grid.contents)),
                'max_y': len(grid.contents)
            }
            for y in range(len(grid.contents)):
                for x in range(len(grid.contents[y])):
                    cell_eval_criteria['x'] = x
                    cell_eval_criteria['y'] = y
                    cell_eval_criteria['alive'] = grid.contents[y][x].alive
                    result_grid.contents[y][x].alive = evaluate_cell(**cell_eval_criteria)
            return result_grid
        else:
            return self.step(grid=self.step(grid=grid, steps=steps-1))

    def __str__(self):
        return GENERATION_FORMAT.format(num=self.generation_number, table=str(self.grid))

if __name__ == '__main__':
    # grid = Grid(width=10, height=10)
    grid = Grid(
        cells=[
            [
                Cell(
                    Coordinates(x,y),
                    True if x == 2 and y > 0 and y < 4 else False
                )
                for x in range(5)
            ]
            for y in range(5)
        ]
    )
    # grid = Grid(
    #     cells=[
    #         [
    #             Cell(
    #                 Coordinates(x,y),
    #                 True if y == 2 and x > 0 and x < 4 else False
    #             )
    #             for x in range(5)
    #         ]
    #         for y in range(5)
    #     ]
    # )
    print(grid)
    generation = Generation(grid)
    print(generation)
    generation = Generation(generation.grid, generation.generation_number)
    print(generation)
