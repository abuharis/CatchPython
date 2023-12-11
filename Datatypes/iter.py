#find the combinations
from itertools import product


colors = ["red", "green"]
sizes = ["S", "L", "M"]

combinations = [(color, size) for color in colors
                    for size in sizes]

for item in combinations:
    print(item)

#also this can be done by itertools
combinations = product(colors, sizes)


for item in combinations:
    print(item)