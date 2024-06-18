data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

# Хотелось бы подметить, что True - не строка, однако ДЗ подразумевает,
# что True должен оказаться в списке со строками,
# поэтому далее я буду относиться к True в этом задании, как к строковой переменной :P
letters = list(element for element in data_tuple if type(element) == str or type(element) == bool)
numbers = list(element for element in data_tuple if type(element) == int or type(element) == float)

letters.remove(True), letters.append(True)
numbers.remove(6.13), numbers.insert(1, 2)

letters.reverse()
letters[1] = "G"
letters[-2] = "c"
numbers.sort()

letters = tuple(letters)
numbers = tuple(element*element for element in numbers)

print(letters)
print(numbers)