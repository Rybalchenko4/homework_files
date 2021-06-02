def hmporc():
    person = int(input('Введите количество персон: '))

    for dish in list:
        print(dish[0],':')
    for ingridient, weight, unit in dish[1]:
        print(f' {ingridient}, {weight*person}, {unit}')