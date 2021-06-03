with open('recipes.txt') as file:
    for line in file:
        if '|' in line:
            print(line.strip())