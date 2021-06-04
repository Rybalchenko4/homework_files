with open('recipes.txt') as file:
    list_0 = []
    list_1 = []
    list_2 = []
    for line in file:
        if '|' in line:
            list_1.append(line.strip().split('|'))
        else:
            if len(line) > 1:
                list_0.append(line.strip())
            else:
                pass
        
    print(list_0)
    print(list_1)
    print(list_2)