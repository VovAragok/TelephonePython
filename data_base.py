def write_info(info):
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(info)


def find_info(char):
    with open("data.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()
        count = 0
        for line in lst:
            if char in line:
                count += 1
                print(f"{count } {line.strip()}")


def delete_info(char):
    with open("data.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()

    found_users = []
    for line in lst:
        if char in line:
            found_users.append(line.strip())

    print("Найденные пользователи:")
    for i, user in enumerate(found_users, start=1):
        print(f"{i}. {user}")

    user_num = int(input("Введите номер пользователя, которого вы хотите удалить (или '0' для отмены): "))
    if user_num == 0:
        return

    user_to_delete = found_users[user_num - 1]
    lst.remove(user_to_delete + '\n')

    with open("data.txt", "w", encoding="utf-8") as file:
        file.writelines(lst)

    print("Пользователь успешно удален.")



def edit_info(char):
    with open("data.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()

    found_users = []
    for line in lst:
        if char in line:
            found_users.append(line.strip())

    print("Найденные пользователи:")
    for i, user in enumerate(found_users, start=1):
        print(f"{i}. {user}")

    user_num = int(input("Введите номер пользователя, чьи параметры вы хотите отредактировать (или '0' для отмены): "))
    if user_num == 0 or user_num > len(found_users):
        return

    user_to_edit = found_users[user_num - 1].split(", ")
    new_info = input("Введите новые параметры пользователя через запятую (ФИО, Дата рождения, Телефон): ")
    new_info = new_info.split(", ")
    if len(new_info) != 3:
        print("Некорректный ввод параметров. Параметры пользователя не были изменены.")
        return

    user_to_edit[0], user_to_edit[1], user_to_edit[2] = new_info[0], new_info[1], new_info[2]
    found_users[user_num - 1] = ", ".join(user_to_edit)

    with open("data.txt", "w", encoding="utf-8") as file:
        file.writelines(lst)

    print("Параметры пользователя успешно отредактированы.")