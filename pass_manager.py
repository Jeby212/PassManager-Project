filepath = 'D:\\TestPath\\grocery_list.txt'
useCase = ''
user = ''
pw = ''

with open(filepath, 'a') as fa:
    fa.write('It begins.')

with open(filepath, 'r') as fr:
    print(fr.read())