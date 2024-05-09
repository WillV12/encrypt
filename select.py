import os

import keyboard
from time import sleep


class Selector:

    def select1(self):
        return "\n\n>Encrypt\nDecrypt\nRead\nWrite\nHelp\nQuit"

    def select2(self):
        return "\n\nEncrypt\n>Decrypt\nRead\nWrite\nHelp\nQuit"

    def select3(self):
        return "\n\nEncrypt\nDecrypt\n>Read\nWrite\nHelp\nQuit"

    def select4(self):
        return "\n\nEncrypt\nDecrypt\nRead\n>Write\nHelp\nQuit"

    def select5(self):
        return "\n\nEncrypt\nDecrypt\nRead\nWrite\n>Help\nQuit"

    def select6(self):
        return "\n\nEncrypt\nDecrypt\nRead\nWrite\nHelp\n>Quit"

    def iterate(self, select):

        if keyboard.is_pressed("down") and select == self.select1():
            return self.select2()
        elif keyboard.is_pressed("down") and select == self.select2():
            return self.select3()

        elif keyboard.is_pressed("down") and select == self.select3():
            return self.select4()

        elif keyboard.is_pressed("down") and select == self.select4():
            return self.select5()

        elif keyboard.is_pressed("down") and select == self.select5():
            return self.select6()

        elif keyboard.is_pressed("up") and select == self.select6():
            return self.select5()

        elif keyboard.is_pressed("up") and select == self.select5():
            return self.select4()

        elif keyboard.is_pressed("up") and select == self.select4():
            return self.select3()

        elif keyboard.is_pressed("up") and select == self.select3():
            return self.select2()

        elif keyboard.is_pressed("up") and select == self.select2():
            return self.select1()

        elif keyboard.is_pressed("shift") and select == self.select1():
            return 1
        elif keyboard.is_pressed("shift") and select == self.select2():
            return 2
        elif keyboard.is_pressed("shift") and select == self.select3():
            return 3
        elif keyboard.is_pressed("shift") and select == self.select4():
            return 4
        elif keyboard.is_pressed("shift") and select == self.select5():
            return 5
        elif keyboard.is_pressed("shift") and select == self.select6():
            return 6


    def help(self):
        try:
            os.system("cls")
            with open("Help.txt", "r") as title:
                for line in range(14):
                    print(title.readline())
                    sleep(.1)
        except FileNotFoundError:
            print("File not found")

    def get_input(self):
        file_name = input("\nPlease enter a file name:\n")

        key = input("\nPlease enter a key:\n")
        while key.isdigit() is False:
            print("Please write a number...\n")
            key = input("Please enter a key")
        else:
            key = int(key)

        length = input("\nNumber of lines:\n")
        while length.isdigit() is False:
            print("Please write a number...\n")
            length = input("\nNumber of lines:\n")
        else:
            length = int(length)

        return file_name, key, length

    def alt_get_input(self):
        file_name = input("\nPlease enter a file name:\n")
        length = input("\nNumber of lines:\n")
        while length.isdigit() is False:
            print("Please write a number...\n")
            length = input("\nNumber of lines:\n")
        else:
            length = int(length)

        return file_name, length



