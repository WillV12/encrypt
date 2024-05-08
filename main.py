import os


def main():
    file_name = input("\nPlease enter a file name:\n")

    key = input("\nPlease enter a key:\n")
    length = int(input("\nNumber of lines:\n"))
    while key.isdigit() is False:
        print("Please write a number...\n")
        key = input("Please enter a key")
    else:
        key = int(key)
    while True:
        choice = input("Encrypt or Decrypt (1 or 2)")

        if choice == "1":
            encrypt(file_name, key, length)
            break
        elif choice == "2":
            decrypt(file_name, key, length)
            break


def encrypt(file_name=None, key=0, length=0):
    if os.path.isfile(file_name) is True:
        file = open(file_name, 'r')
        encrypted = []
        for iteration in range(length):
            text = file.readline()
            escapes = ''.join([chr(char) for char in range(1, 32)])
            translator = str.maketrans('', '', escapes)
            text = text.translate(translator)
            text = text.strip(" ")
            text = text.split(" ")
            for word in text:
                for letter in word:
                    encrypted.append(chr(ord(letter)+key))
                encrypted.append(" ")
            if iteration < length - 1:
                encrypted.append("\n")
        string_txt = ""
        for item in encrypted:
            string_txt += item
        file.close()
        file = (open(file_name, "w", encoding="utf-8"))
        file.write(string_txt)
        file.close()
    else:
        print("Not a valid file")


def decrypt(file_name=None, key=0, length=0):
    if os.path.isfile(file_name) is True:
        file = open(file_name, 'r', encoding="utf-8")
        encrypted = []
        for iteration in range(length):
            text = file.readline()
            escapes = ''.join([chr(char) for char in range(1, 32)])
            translator = str.maketrans('', '', escapes)
            text = text.translate(translator)
            text = text.strip(" ")
            text = text.split(" ")
            for word in text:
                for letter in word:
                    encrypted.append(chr(ord(letter) - key))
                encrypted.append(" ")
            if iteration < length - 1:
                encrypted.append("\n")
        string_txt = ""
        for item in encrypted:
            string_txt += item
        file.close()
        file = open(file_name, "w")
        file.write(string_txt)
        file.close()
    else:
        print("Not a valid file")


def read_file(file):
    try:
        with open(file, 'r', encoding="utf-8") as file:
            print(file.read())
    except FileExistsError:
        print("Not a valid")


if __name__ == '__main__':
    main()
