filepath = "D:\\TestPath\\grocery_list.txt"
useCase = ''
user = ''
pw = ''

def addPassword():
    useCase = input("Which service do you want to store this password for?\n")
    user = input("Please enter your username.\n")
    pw = input("Please enter your password.\n")
    lines = [useCase + '\n', user + '\n', pw + '\n']
    file = open(filepath, 'a')
    file.writelines(lines)

addPassword()

with open(filepath, 'r') as fr:
    info = fr.read().splitlines()
    print(info)