from data_base import *
from view import *


def main():
    while True:
        num = input_num()
        if num == 1:
            info = input_info()
            write_info(info)
        if num == 2:
            char = input_char()
            find_info(char)
        if num == 3:
            char = input_char()
            delete_info(char)

        if num == 4:
            char = input_char()
            edit_info(char)

        if num == 5:
            print("выход из программы  ")
            break



main()
