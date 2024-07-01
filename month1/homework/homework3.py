<<<<<<< HEAD
vowels = ["a", "e", "i", "o", "u", "а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
              "б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]

print("Добро пожаловать. Программа принимает слова на латинице и кириллице, затем подсчитывает и выводит на экран:"
      "\n1. Количество строчных и прописных букв в слове;"
      "\n2. Количество гласных и согласных букв в слове;"
      "\n3. Общее количество букв в слове;"
      "\n4. Процентное соотношение гласных и согласных букв в слове."
      "\n\nДля выхода из программы введите 'выход' или 'exit'")


while True :
    word = input("\nВведите слово: ")

    if word == "выход" or word == "exit" :
        print("\nЗавершение работы программы...")
        break

    totalLetterCount = 0

    lowerLetterCount = 0
    upperLetterCount = 0

    vowelCount = 0
    consonantCount = 0

    vowelRatio = 0.0
    consonantRatio = 0.0

    for x in word :
        # в задаче указано считывать строчные и прописные буквы,
        # но о выводе этих данных в консоль ничего не сказано.
        if x.islower() :
            lowerLetterCount += 1
        elif x.isupper() :
            upperLetterCount += 1

        if x in vowels :
            vowelCount += 1
        elif x in consonants :
            consonantCount += 1

        totalLetterCount += 1

    vowelRatio = round(100 / totalLetterCount * vowelCount, 2)
    consonantRatio = round(100 / totalLetterCount * consonantCount, 2)

    print("Количество букв: " + str(totalLetterCount))
    print("Согласных букв: " + str(consonantCount))
    print("Гласных букв: " + str(vowelCount))
=======
vowels = ["a", "e", "i", "o", "u", "а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
              "б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]

print("Добро пожаловать. Программа принимает слова на латинице и кириллице, затем подсчитывает и выводит на экран:"
      "\n1. Количество строчных и прописных букв в слове;"
      "\n2. Количество гласных и согласных букв в слове;"
      "\n3. Общее количество букв в слове;"
      "\n4. Процентное соотношение гласных и согласных букв в слове."
      "\n\nДля выхода из программы введите 'выход' или 'exit'")


while True :
    word = input("\nВведите слово: ")

    if word == "выход" or word == "exit" :
        print("\nЗавершение работы программы...")
        break

    totalLetterCount = 0

    lowerLetterCount = 0
    upperLetterCount = 0

    vowelCount = 0
    consonantCount = 0

    vowelRatio = 0.0
    consonantRatio = 0.0

    for x in word :
        # в задаче указано считывать строчные и прописные буквы,
        # но о выводе этих данных в консоль ничего не сказано.
        if x.islower() :
            lowerLetterCount += 1
        elif x.isupper() :
            upperLetterCount += 1

        if x in vowels :
            vowelCount += 1
        elif x in consonants :
            consonantCount += 1

        totalLetterCount += 1

    vowelRatio = round(100 / totalLetterCount * vowelCount, 2)
    consonantRatio = round(100 / totalLetterCount * consonantCount, 2)

    print("Количество букв: " + str(totalLetterCount))
    print("Согласных букв: " + str(consonantCount))
    print("Гласных букв: " + str(vowelCount))
>>>>>>> 72fa1af35ef8453bc0d68872b64ea025d92cd271
    print("Гласные/Согласные: " + str(vowelRatio) + "% / " + str(consonantRatio) + "%")