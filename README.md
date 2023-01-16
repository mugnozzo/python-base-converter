# python-base-converter
A python program that will convert a given number from a given base to another given base.

## Requirements
- python 3.x;
- Linux (not tesed on other operative systems).

## Installation
- Clone the repo. If you're new to git, check [this](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository);
- copy (or rename) the `config.def.ini` to `config.ini`.

## Usage
Exec the python script passing the arguments to it (see `./pybc.py --help` for the complete list of arguments):
```
./pybc.py -n <string_to_convert> -s <source_base> -d <destination_base>
```
It takes a number `-n` in a given base `-s` and converts it into base `\d`.

### Alphabets
You can manage the alphabets to use in each base (the source and destination number bases) in the config.ini file.
The default bases are numbers from 0 to 9 followed by letters from A to Z (pay attention when giving the `-n` parameter: in the default alphabet the letters must be uppercase).
If analphabet is set to `ASCII` then it is set to the list of ASCII characters from 32 (space) to 126 (~).

## Missing features
- Improving this README with more instructions.
- accepting a file (or stdin) as input (planned as next update).