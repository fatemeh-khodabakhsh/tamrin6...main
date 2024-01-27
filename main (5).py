n = input()
numbers = n.split()
target = int(input())
positions = {}

for index, number in enumerate(numbers):
     positions[(int(number))] = index
combinations = {}
for k in positions.keys():
    difference = target - k
    if difference in positions and difference != k:
        sum_of_positions = positions[k] + positions[difference]
        if (difference, k) not in c.keys():
            combinations[(k, difference)] = sum_of_positions
sorted_combinations = sorted(combinations.values())

if not combinations:
    print("Not Found!")
else:
    for combination in sorted_combinations:
        print(combination)
