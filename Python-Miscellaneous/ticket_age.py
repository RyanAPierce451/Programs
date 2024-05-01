age = int(input('How old are you '))

if age < 13:
    print('Children tickets cost: $6')
elif  age >= 13 and age < 64:
    print('Adult tickets cost: $8')
else:
    print('Senior discount tickets cost: $7')
