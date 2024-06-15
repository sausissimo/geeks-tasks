print("Здравствуйте!")
while True:
    time = input("Пожалуйста, укажите время суток: ")

    if time.lower() == 'стоп' or time.lower() == 'выход':
        print("\nДо свидания!")
        break

    elif time.lower() == 'утро':
        print("\nДоброе утро!\n")
    elif time.lower() == 'день':
        print("\nДобрый день!\n")
    elif time.lower() == 'вечер':
        print("\nДобрый вечер!\n")
    elif time.lower() == 'ночь':
        print("\nДоброй ночи!\n")

    else:
        print("\nИзвините, это не похоже на время суток...\n")