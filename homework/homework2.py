print("\nДобро пожаловать!")

def checkIfOven(day, month):
    if month == 3 :
        if day >= 21 and day <= 31 :
            #print("\nВы овен, соболезную.")
            return True
    elif month == 4 :
        if day >= 1 and day <= 20 :
            #print("\nВы овен, соболезную.")
            return True
    else :
        #print("\nНеверный ввод, попробуйте ещё раз.")
        return False

def checkIfTelec(day, month):
    if month == 4 :
        if day >= 21 and day <= 30 :
            return True
    elif month == 5 :
        if day >= 1 and day <= 21 :
            return True
    else :
        return False

def checkIfBliznecy(day, month):
    if month == 5 :
        if day >= 22 and day <= 31 :
            return True
    elif month == 6 :
        if day >= 1 and day <= 21 :
            return True
    else :
        return False

def checkIfRak(day, month):
    if month == 6 :
        if day >= 22 and day <= 30 :
            return True
    elif month == 7 :
        if day >= 1 and day <= 22 :
            return True
    else :
        return False

def checkIfLev(day, month):
    if month == 7 :
        if day >= 23 and day <= 31 :
            return True
    elif month == 8 :
        if day >= 1 and day <= 21 :
            return True
    else :
        return False

def checkIfDeva(day, month):
    if month == 8 :
        if day >= 22 and day <= 31 :
            return True
    elif month == 9 :
        if day >= 1 and day <= 23 :
            return True
    else :
        return False

def checkIfVesy(day, month):
    if month == 9 :
        if day >= 24 and day <= 30 :
            return True
    elif month == 10 :
        if day >= 1 and day <= 23 :
            return True
    else :
        return False

def checkIfScorpion(day, month):
    if month == 10 :
        if day >= 24 and day <= 31 :
            return True
    elif month == 11 :
        if day >= 1 and day <= 22 :
            return True
    else :
        return False

def checkIfStrelec(day, month):
    if month == 11 :
        if day >= 23 and day <= 30 :
            return True
    elif month == 12 :
        if day >= 1 and day <= 22 :
            return True
    else :
        return False

def checkIfKozerog(day, month):
    if month == 12 :
        if day >= 23 and day <= 31 :
            return True
    elif month == 1 :
        if day >= 1 and day <= 20 :
            return True
    else :
        return False

def checkIfVodoley(day, month):
    if month == 1 :
        if day >= 21 and day <= 31 :
            return True
    elif month == 2 :
        if day >= 1 and day <= 19 :
            return True
    else :
        return False

def checkIfRyba(day, month):
    if month == 2 :
        if day >= 20 and day <= 28 :
            return True
    elif month == 3 :
        if day >= 1 and day <= 20 :
            return True
    else :
        return False


def checkZodiac():
    try:
        day = int(input("\nВведите день рождения: "))
        month = int(input("Введите месяц рождения: "))
        if checkIfOven(day, month):
            print("\nВы овен, соболезную.")
        elif checkIfTelec(day, month):
            print("\nВы телец, соболезную.")
        elif checkIfBliznecy(day, month):
            print("\nВаш знак - близнецы, соболезную.")
        elif checkIfRak(day, month):
            print("\nВы - рак, соболезную.")
        elif checkIfLev(day, month):
            print("\nВы - лев. Сильнее волка и тигра, но выступаете в цирке.")
        elif checkIfDeva(day, month):
            print("\nВы - дева, завидую.")
        elif checkIfVesy(day, month):
            print("\nВы - весы, без обид.")
        elif checkIfScorpion(day, month):
            print("\nВы - скорпион, поздравляю.")
        elif checkIfStrelec(day, month):
            print("\nВы телец, соболезную.")
        elif checkIfKozerog(day, month):
            print("\nВы - козерог, соболезную.")
        elif checkIfVodoley(day, month):
            print("\nВы - водолей, соболезную.")
        elif checkIfRyba(day, month):
            print("\nВы - рыба, буль-буль-буль")
        else:
            print("\nНеверный ввод, попробуйте ещё раз.")
    except:
        print(" ne pravilno")




while True:
    prompt = input('\nПожалуйста, введите "да" для продолжения работы программы или "нет" для выхода.\n')
    if prompt.lower() == 'да':
        checkZodiac()
    elif prompt.lower() == 'нет':
        break

