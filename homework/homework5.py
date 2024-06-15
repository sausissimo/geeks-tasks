def getSale(homeworkGrade, testGrade, attendanceCount):

    if homeworkGrade >= 70 and homeworkGrade <= 80:
        homework = 3
    elif homeworkGrade >= 50:
        homework = 2
    else:
        homework = 1

    if testGrade >= 80:
        test = 3
    elif testGrade >= 60:
        test = 2
    else:
        test = 1

    if attendanceCount >= 8:
        attendance = 3
    elif attendanceCount >= 6:
        attendance = 2
    else:
        attendance = 1

    if homework == 1 or test == 1:
        return '\nНикакой скидки, сорян :P'
    elif attendance == 1:
        return '\nВаша скидка: ' + str(1000)
    elif attendance == 2:
        return '\nВаша скидка: ' + str(2000)
    elif homeworkGrade > 80 or testGrade > 80 or attendanceCount > 8:
        return "\nНу да, ну да - так я и поверю, что вы столько заработали  ,':)"

    return '\nВаша скидка: ' + str(round(((homework + test + attendance) * 1000 / 3) / 500) * 500)

print('\033[1;37mДобро пожаловать в программу подсчёта скидок Geeks!')

while True:
    print('Пожалуйста, введите соответствующие данные: (или "выход" для выхода)\n')
    try:
        homework = int(input('Баллы за домашние задания: '))
        test = int(input('Баллы за тесты: '))
        attendance = int(input('Количество посещённых уроков: '))
        print(getSale(homework, test, attendance)), print()
    except ValueError:
        print('\n\033[1;31;40mОшибка: программа принимает только числа.\n\033[1;37m')
