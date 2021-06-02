cook_book = []

with open('recipes.txt'):
    pass
    
def hmporc():
    person = int(input('Введите количество персон: '))

    for dish in cook_book:
        print(dish[0],':')
    for ingridient, weight, gramm in dish[1]:
        print(f' {ingridient}, {weight*person}, {gramm}')