# Conway's Game of Life (Python 3)
Conway's Game of Life implemented in Python 3 as a CLI game/simulation.

## Dependencies
Python 3.5+ is required as the code was written with type checking in mind. Other then that, no other dependencies are required, everything has been implemented using Python's standard library.

GNU Make is an optional dependency for optimizing workflows with this project.

## Project Structure
```
test.py [unit tests to ensure requirements compliance]
  /-\
   |
  \-/
life.py [core data classes as well as object oriented logic for changing simulation state]
  /-\
   |
  \-/
game.py [WIP wrapper script to turn life.py into a fully functional CLI tool]
```

## Test Suite
Unit tests using all the examples found on [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns) can be found implemented in `test.py`, which may be executed as:
```
python3 test.py
```
Or with project dependency checks included as:
```
make test
```

## CLI Wrapper
```bash
$ python3 game.py --help
```
```
usage: game.py [-h] [-si | -if IN_FILE] [-so | -of OUT_FILE]
               [-sg [STARTING_GENERATION]] [-eg [ENDING_GENERATION] | -ng
               [NUMBER_GENERATIONS]] [-v]

Simulate Conway's Game of Life from the command line.

optional arguments:
  -h, --help            show this help message and exit
  -si, --stdin          Use stdin instead of a file to get initial state
                        (default)
  -if IN_FILE, --in-file IN_FILE
                        Read initial state from a file.
  -so, --stdout         Use stdout instead of a file to output final state
                        (default)
  -of OUT_FILE, --out-file OUT_FILE
                        Save final state to a file.
  -sg [STARTING_GENERATION], --starting-generation [STARTING_GENERATION]
                        Starting generation number (default: 0).
  -eg [ENDING_GENERATION], --ending-generation [ENDING_GENERATION]
                        Ending generation number (default: 1).
  -ng [NUMBER_GENERATIONS], --number-generations [NUMBER_GENERATIONS]
                        Number of Generations (default option) (default: 1).
  -v, --verbose         Verbose output (disabled by default)
```
