import encrypt
import select
from time import sleep
import os


def main():
    title = select.Selector()
    choice = title.iterate()
    while True:
        if choice == 1:
            file_name, key, length = title.get_input()
            user_file = encrypt.Encryption(file_name, key, length)
            os.system("cls")
            user_file.encrypt()
            print("Your file has been encrypted")
            sleep(3)

        elif choice == 2:
            file_name, key, length = title.get_input()
            user_file = encrypt.Encryption(file_name, key, length)
            user_file.decrypt()
            print("Your file has been decrypted")
            sleep(3)

        elif choice == 3:
            file_name, length = title.alt_get_input()
            user_file = encrypt.Encryption(file_name, length=length)
            user_file.read_file()

        elif choice == 4:
            title.help()

        elif choice == 5:
            os.system("cls")
            print("Thanks for stopping by")
            sleep(3)
            break






if __name__ == '__main__':
    main()
