filepath = "D:\\TestPath\\grocery_list.txt"
useCase = ''
user = ''
pw = ''

import base64
from itertools import cycle

MASTER = input("Enter a master password (remember it):\n")  #Be sure to use the same master every time or else decryption won't work due to different key

def _xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes(d ^ k for d, k in zip(data, cycle(key)))

def encrypt(txt: str, key: str) -> str:
    return base64.b64encode(_xor_bytes(txt.encode("utf-8"), key.encode("utf-8"))).decode("ascii")

def decrypt(token: str, key: str) -> str:
    return _xor_bytes(base64.b64decode(token), key.encode("utf-8")).decode("utf-8", errors="ignore")

def try_decrypt(token: str, key: str) -> str:
    try:
        return decrypt(token, key)
    except Exception:
        return token 

def addPassword():
    useCase = input("Which service do you want to store this password for?\n")
    user = input("Please enter your username.\n")
    pw = input("Please enter your password.\n")
    lines = [
        encrypt(useCase, MASTER) + '\n',
        encrypt(user, MASTER) + '\n',
        encrypt(pw, MASTER) + '\n',
    ]
    file = open(filepath, 'a')
    file.writelines(lines)

def decryptPassword():
    file = open(filepath, 'r')
    lines = file.readlines()
    word = encrypt(input("Which service\'s username and password do you wish to retrieve? "), MASTER)  # String to search for
    for row in lines:
        if row.find(word) != -1:
            num = lines.index(row)
            print("Service: " + try_decrypt(lines[num], MASTER))
            print("Username: " + try_decrypt(lines[num + 1], MASTER))
            print("Password: " + try_decrypt(lines[num + 2], MASTER))
    file.close()

addPassword()
decryptPassword()

with open(filepath, 'r') as fr:
    info = [try_decrypt(x, MASTER) for x in fr.read().splitlines()]
    print(info)
