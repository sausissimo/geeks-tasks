data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

code = list(element for element in data if element.isdigit())
designations = list(element for element in data if element.isalpha() or element == "O!")

operators = {
}

operators[designations[0]] = code[0], '0700', '0500'
operators[designations[1]] = code[1], '0999', '0555'
operators[designations[2]] = code[2], '0222', '0777'

for keys, values in operators.items():
    print(str(keys) + ': ' + str(values))
