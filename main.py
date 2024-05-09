import encrypt
import select
from time import sleep
import os


def main():
    title = select.Selector()
    selection = title.select1()
    while True:
        choice = title.iterate(selection)
        os.system("cls")
        with open("Title.txt", "r") as intro:
            print(f"{intro.read()}{selection}")
        print('\033[100A\033[2K', end='')
        sleep(.1)
        if choice == 1:
            os.system("cls")
            file_name, key, length = title.get_input()
            user_file = encrypt.Encryption(file_name, key, length)
            os.system("cls")
            user_file.encrypt()
            print("Your file has been encrypted")
            sleep(3)

        elif choice == 2:
            os.system("cls")
            file_name, key, length = title.get_input()
            user_file = encrypt.Encryption(file_name, key, length)
            user_file.decrypt()
            print("Your file has been decrypted")
            sleep(3)

        elif choice == 3:
            os.system("cls")
            file_name, length = title.alt_get_input()
            user_file = encrypt.Encryption(file_name, length=length)
            user_file.read_file()

        elif choice == 4:
            pass

        elif choice == 5:
            os.system("cls")
            title.help()
            input("press enter to continue")
            continue

        elif choice == 6:
            os.system("cls")
            print("Thanks for stopping by")
            sleep(3)
            break
        elif choice is not None:
            selection = choice
        else:
            continue


if __name__ == '__main__':
    main()
