import argparse
import importlib

from utils import read_input


def main():
    parser = argparse.ArgumentParser(description='Run Advent of Code solution')
    parser.add_argument('--year', '-y', type=int, required=True, help='Year (e.g., 2024)')
    parser.add_argument('--day', '-d', type=int, required=True, help='Day (1-25)')
    args = parser.parse_args()

    input_path = f'{args.year}/inputs/day{args.day}.txt'
    input_lines = read_input(input_path)

    module = importlib.import_module(f'{args.year}.day{args.day}')
    module.main(input_lines)


if __name__ == '__main__':
    main()
