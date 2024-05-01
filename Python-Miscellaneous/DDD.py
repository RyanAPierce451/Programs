my_list = ['keyboard', 'mouse', 'led', 'monitor', 'headphones', 'dvd']
for i in range(0, len(my_list), 4):
    print ("".join(my_list[i:i+4]))