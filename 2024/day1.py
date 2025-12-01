from collections import Counter


def part1(firsts, seconds):
    firsts.sort()
    seconds.sort()
    return sum(abs(f - s) for f, s in zip(firsts, seconds))


def part2(firsts, seconds):
    second_counts = Counter(seconds)
    return sum(n * second_counts[n] for n in firsts)


def split_firsts_seconds(input_lines):
    numbers = [[int(n) for n in row.split()] for row in input_lines]
    firsts, seconds = [list(l) for l in zip(*numbers)]
    return firsts, seconds


def main(input_lines):
    firsts, seconds = split_firsts_seconds(input_lines)
    print(part1(firsts, seconds))
    print(part2(firsts, seconds))
