def nearestNumber(n1, numbers: list):
    numbers.sort(key=lambda x: abs(n1 - x))
    return numbers

def nearestNumberLambdaFilter(n1, numbers: list):
    result = list(filter(lambda x: abs(n1 - x), numbers))
    return result

def nearestNumberLambdaMap(n1, numbers: list):
    result = list(map(lambda x: abs(n1 - x), numbers))
    return result #КОД НЕ РАБОТАЕТ: СТРАННЫЙ ВЫВОД. Разобраться с этим до сдачи ДЗ не успеваем

numbers = [5000, 600000, 4000, 1991, 60000000, 69, 10069]
n1 = 10000

print("Сортировка: " + str(tuple([n1, nearestNumber(n1, numbers)])))
print("Сортировка методом filter(): " + str(tuple([n1, nearestNumberLambdaFilter(n1, numbers)])))
print("Сортировка методом map(): Не работает.")# + str(tuple([n1, nearestNumberLambdaMap(n1, numbers)])))