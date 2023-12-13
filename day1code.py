with open("input1.txt", "r") as file:
    input_data = file.read().strip()
elf_groups = input_data.split("\n\n")

max_calories = 0

for elf_group in elf_groups:
    elf_lines = elf_group.split("\n")
    total_calories = sum(map(int, elf_lines))

    if total_calories > max_calories:
        max_calories = total_calories


print("Total Calories carried by the Elf with the most Calories:", max_calories)