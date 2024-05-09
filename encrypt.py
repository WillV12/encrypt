import os
from time import sleep


class Encryption:

    def __init__(self, file_name="", key=0, length=0):
        self.file_name = file_name
        self.key = key
        self.length = length

    def read_file(self):
        try:
            os.system("cls")
            with open(self.file_name, 'r', encoding="utf-8") as file:
                for line in range(self.length):
                    print(file.readline())
                    sleep(.15)
                input("press enter to continue")
        except FileExistsError:
            print("Not a valid file")

    def write_file(self):
        try:
            os.system("cls")
            with open(self.file_name, "w", encoding="utf-8") as file:
                text = input("Text:\n")
                file.write(text)
            print("Data written to file")
        except FileNotFoundError:
            print("Invalid target file")

    def dir(self):
        os.system("dir")

    def encrypt(self):
        if os.path.isfile(self.file_name) is True:
            with open(self.file_name, 'r', encoding="utf-8") as file:
                encrypted = []
                for iteration in range(self.length):
                    text = file.readline()
                    escapes = ''.join([chr(char) for char in range(1, 32)])
                    translator = str.maketrans('', '', escapes)
                    text = text.translate(translator)
                    text = text.strip(" ")
                    text = text.split(" ")
                    for word in text:
                        for letter in word:
                            encrypted.append(chr(ord(letter) + self.key))
                        encrypted.append(" ")
                    if iteration < self.length - 1:
                        encrypted.append("\n")
                string_txt = ""
                for item in encrypted:
                    string_txt += item
            with open(self.file_name, 'w', encoding="utf-8") as file:
                file.write(string_txt)
        else:
            print("Not a valid file")

    def decrypt(self):
        if os.path.isfile(self.file_name) is True:
            with open(self.file_name, 'r', encoding="utf-8") as file:
                encrypted = []
                for iteration in range(self.length):
                    text = file.readline()
                    escapes = ''.join([chr(char) for char in range(1, 32)])
                    translator = str.maketrans('', '', escapes)
                    text = text.translate(translator)
                    text = text.strip(" ")
                    text = text.split(" ")
                    for word in text:
                        for letter in word:
                            encrypted.append(chr(ord(letter) - self.key))
                        encrypted.append(" ")
                    if iteration < self.length - 1:
                        encrypted.append("\n")
                string_txt = ""
                for item in encrypted:
                    string_txt += item
            with open(self.file_name, 'w', encoding="utf-8") as file:
                file.write(string_txt)
        else:
            print("Not a valid file")
