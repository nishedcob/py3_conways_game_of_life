
import sys
import argparse
from copy import deepcopy
from typing import List

from life import Cell, Coordinates, Grid, Generation, ALIVE_CHAR, COMMENT_CHAR


def parse_args() -> dict:
    parser = argparse.ArgumentParser(description="Simulate Conway's Game of Life from the command line.")
    input_parser = parser.add_mutually_exclusive_group(required=False)
    input_parser.add_argument('-si', '--stdin', action='store_true', help="Use stdin instead of a file to get initial state (default)")
    input_parser.add_argument('-if', '--in-file', nargs=1, help="Read initial state from a file.")
    output_parser = parser.add_mutually_exclusive_group(required=False)
    output_parser.add_argument('-so', '--stdout', action='store_true', help="Use stdout instead of a file to output final state (default)")
    output_parser.add_argument('-of', '--out-file', nargs=1, help="Save final state to a file.")
    parser.add_argument('-sg', '--starting-generation', nargs="?", type=int, default=0, const=0, help="Starting generation number (default: 0).")
    generation_parser = parser.add_mutually_exclusive_group(required=False)
    generation_parser.add_argument('-eg', '--ending-generation', nargs="?", type=int, const=1, help="Ending generation number (default: 1).")
    generation_parser.add_argument('-ng', '--number-generations', nargs="?", type=int, const=1, help="Number of Generations (default option) (default: 1).")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Verbose output (disabled by default)")
    return parser.parse_args().__dict__


def build_config(args: dict) -> dict:
    if args['stdin'] or args['in_file'] is None:
        args['in_file'] = 'sys.stdin'
    del args['stdin']
    if args['stdout'] or args['out_file'] is None:
        args['out_file'] = 'sys.stdout'
    del args['stdout']
    if args['number_generations'] is None:
        if args['ending_generation'] is None:
            args['number_generations'] = 1
        else:
            args['number_generations'] = args['ending_generation'] - args['starting_generation']
            args['number_generations'] = 0 if args['number_generations'] < 0 else args['number_generations']
    del args['ending_generation']
    return args


def read_state(in_file: str, **kwargs) -> Grid:
    cell_matrix = []
    def build_cell_matrix(file) -> List[List[Cell]]:
        row_number = 0
        cell_mtrx = []
        for row in file:
            col_number = 0
            cell_mtrx.append([])
            for char in row:
                if char == COMMENT_CHAR or char == '\n':
                    break
                cell_mtrx[len(cell_mtrx) - 1].append(Cell(Coordinates(col_number, row_number), char == ALIVE_CHAR))
                col_number += 1
            row_number += 1
        cell_mtrx = list(filter(lambda row: len(row) != 0, cell_mtrx))
        return cell_mtrx
    if in_file == 'sys.stdin':
        cell_matrix = build_cell_matrix(file=sys.stdin)
    else:
        if type(in_file) == list:
            in_file = in_file[0]
        with open(in_file, 'r') as read_file:
            cell_matrix = build_cell_matrix(file=read_file)
    return Grid(cells=cell_matrix)


def process_state(initial_state: Grid, starting_generation: int, number_generations: int, verbose: bool, **kwargs) -> Generation:
    return Generation(grid=initial_state, generation_number=starting_generation, steps=number_generations, verbose=verbose)


def write_state(final_state: Generation, out_file: str, **kwargs):
    if type(out_file) == list:
        out_file = out_file[0]
    with open(out_file, 'w') as write_file:
        write_file.write(str(final_state))


def main():
    args = parse_args()
    config = build_config(args=deepcopy(args))
    # print(config)
    initial_state = read_state(**config)
    if not config['verbose']:
        print("{comment} generation = {num}".format(comment=COMMENT_CHAR, num=config['starting_generation']))
        print(initial_state)
    final_state = process_state(initial_state=initial_state, **config)
    print(final_state)
    if config['out_file'] != "sys.stdout":
        write_state(final_state=final_state, **config)



if __name__ == '__main__':
    main()
