def input_num():
    ask = int(input(
        "1 - Добавить пользователя \n2-  Найти пользователя\n3- удалить пользовател\4 - Редактировать пользлователя \n5-Выйти\n"))
    return ask


def input_info():
    fio = input("Введи ФИО человека-  ")
    birth = input("Введи дату рождения  человека-  ")
    tele = input("Введи телефон человека- ")
    info = f"{fio}, {birth}, {tele}\n"
    return info


def input_char():
    char = input("Введите характеристику ")
    return char
