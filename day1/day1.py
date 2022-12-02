import numpy as np

elf1 = [1000, 2000, 3000]
elf2 = [4000]
elf3 = [5000, 6000]
elf4 = [7000, 8000, 9000]
elf5 = [10000]

elves = [elf1, elf2, elf3, elf4, elf5]


elf_totals = [sum(elf) for elf in elves]

max_idx = np.argmax(elf_totals)

print(f"Elf {max_idx + 1} has the most calories with {elf_totals[max_idx]}")




def get_elf_totals(filename):
    lines = open(filename).read().splitlines()

    elf_idx = 1
    elf_calories = 0
    elf_totals = []
    for line in lines:
        if line == "":
            elf_totals.append(elf_calories)
            elf_idx += 1
            elf_calories = 0
            continue

        elf_calories += int(line)

    print(elf_totals)
    return elf_totals


if __name__ == "__main__":
    our_elf_totals = get_elf_totals("day1/our_input.txt")

    max_idx = np.argmax(our_elf_totals)
    print(f"Elf {max_idx + 1} has the most calories with {our_elf_totals[max_idx]}")
