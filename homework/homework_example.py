day = int(input("\nВведите день рождения: "))
month = int(input("Введите месяц рождения: "))

if month == 3:
    if day >= 1 and day <= 20:
            print("\nВы - рыба, буль-буль-буль")
    elif day >= 21 and day <= 31 :
            print("\nВы овен, соболезную.")
if month == 4:
    if day >= 1 and day <= 20:
        print("\nВы овен, соболезную.")
    elif day >= 21 and day <= 30 :
        print('телец')




else:
    print("\nНеверный ввод, попробуйте ещё раз.")

