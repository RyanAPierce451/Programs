print('What single topping pizza would you like to order')
pizza_size = input("Type which size you'd like: S M L ")

if pizza_size == 'S':
    print('Small One Topping: $4.99') 
else:
    if pizza_size == 'M':
        print('Medium One Topping: $5.99')    
    else:
        print('Large One Topping: $6.99')
