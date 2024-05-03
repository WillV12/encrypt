import os


def main():
    file_name = input("\nPlease enter a file name:\n")
    key = input("\nPlease enter a key:\n")
    while key.isdigit() is False:
        print("Please write a number...\n")
        key = input("Please enter a key")
    else:
        key = int(key)
    while True:
        choice = input("Encrypt or Decrypt (1 or 2)")

        if choice == "1":
            encrypt(file_name, key)
            break
        elif choice == "2":
            decrypt(file_name, key)


def encrypt(file_name=None, key=0):
    if os.path.isfile(file_name) is True:
        file = open(file_name, 'r')
        text = file.read()
        file.close()
        encrypted = [chr(ord(word) + key) for word in text]
        string_txt = ""
        for item in encrypted:
            string_txt += item
        print(string_txt)
        file = open(file_name, 'w', encoding="utf-8")
        file.write(string_txt)
        file.close()
    else:
        print("Not a valid file")


def decrypt(file_name=None, key=0):
    if os.path.isfile(file_name) is True:
        file = open(file_name, 'r', encoding="utf-8")
        text = file.read()
        file.close()
        encrypted = [chr(ord(word) - key) for word in text]
        string_txt = ""
        for item in encrypted:
            string_txt += item
        file = open(file_name, 'w', encoding="utf-8")
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
