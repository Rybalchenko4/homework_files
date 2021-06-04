with open('recipes.txt') as file:
        
    list_0 = []
    list_1 = []
    for line in file:
        if '|' in line:
            list_1.append(line.strip().split('|')) #ингридиент, количество, еденица измерения
        else:
            if len(line) > 1:
                list_0.append(line.strip())
            else:
                pass

    list_2 = list_0[::2] #название блюда
    list_3 = list_0[1::2] #количество ингридиентов

print(list_1)
print(list_2)
print(list_3)