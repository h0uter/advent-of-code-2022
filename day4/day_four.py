# FILENAME = "day4/test_input.txt"
FILENAME = "day4/our_input.txt"


def main():
    data = process_input_file(FILENAME)
    subset_count = algo(data)
    print(f"fully containing pairs: {subset_count}")


def process_input_file(filename) -> list[tuple[list[int], list[int]]]:
    lines = open(filename).read().splitlines()
    elf_pair_ranges = []
    for line in lines:
        range_strs = line.split(",")

        elf_pair = []
        for range_str in range_strs:
            start, end = range_str.split("-")
            elf_pair.append(list(range(int(start), int(end) + 1)))

        elf_pair_ranges.append(tuple(elf_pair))

    return elf_pair_ranges


"""
Find the # of lines where one range is fully within another range
"""


def algo(data: list[tuple[list[int], list[int]]]) -> int:
    """counts the number of lines where one range is fully within another range"""
    subset_count = 0

    for pair in data:
        first_elf_range, second_elf_range = pair

        if set(first_elf_range).issubset(set(second_elf_range)):
            subset_count += 1

        elif set(second_elf_range).issubset(set(first_elf_range)):
            subset_count += 1

    return subset_count


if __name__ == "__main__":
    main()
