def encode(password,keys):
    character_check = len(password) * [False]
    list_check = list(password)
    for replace in keys:
        for status, char in enumerate(list_check):
            if character_check[status] == False and replace == char:
                list_check[status] = encrypt_dict[replace]
                character_check[status] = True
    password = ''.join(list_check)
    return password

encrypt_file = 'encrypt_protocol.txt'
crossword_file = 'CROSSWD.txt' 
worst_paswords_file = 'worst_passwords.txt'
worst_passwords_list_improved = []
passwords_strong = [] 
crossword_list = []
encrypt_dict = {}
#Worst_Passwords-File
with open(worst_paswords_file) as file:
    worst_passwords_list_original = file.readlines()
    for i in range(0, len(worst_passwords_list_original)):
        list_improve = str(worst_passwords_list_original[i].strip())
        worst_passwords_list_improved.append(list_improve)
#Crossword-File
with open(crossword_file) as file:
    crossword_list_original = file.readlines()
    for i in range(0, len(crossword_list_original)):
        list_improve = str(crossword_list_original[i].strip())
        crossword_list.append(list_improve)
#Encrypt-File
with open(encrypt_file) as file:
    for i in file:
        (key, val) = i.split(',')
        encrypt_dict[str(key).strip()] = str(val).strip()

for i in range(0,len(worst_passwords_list_improved)):
    if str(worst_passwords_list_improved[i]).lower() in crossword_list or len(worst_passwords_list_improved[i]) < 8:
        if str(worst_passwords_list_improved[i]).lower() in crossword_list and len(worst_passwords_list_improved[i]) < 8:
            worst_passwords_list_improved[i] += '3xPanD'
            reverse = str(worst_passwords_list_improved[i])
            reverse = reverse[::-1]
            passwords_strong.append(reverse)
            continue
        elif str(worst_passwords_list_improved[i]).lower() in crossword_list:
            reverse = str(worst_passwords_list_improved[i])
            reverse = reverse[::-1]
            passwords_strong.append(reverse)
            continue
        elif len(worst_passwords_list_improved[i]) < 8:
            worst_passwords_list_improved[i] += '3xPanD'
            passwords_strong.append(worst_passwords_list_improved[i])
            continue
    else:
        passwords_strong.append(worst_passwords_list_improved[i])

with open('improved_passwords.txt','w') as file:
    for i in passwords_strong:
        password = i
        keys = encrypt_dict.keys()
        file.write(encode(password,keys)+ '\n')   