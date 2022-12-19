import os

with open('input.txt', encoding="utf8") as file:
    for line in file:
        points = int(line.split()[-1])
        if points <= 3 and points >=3:
            name = " ".join(line.split()[:-1])
            print(name)

file.close()