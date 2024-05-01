num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces
i = 0
j = 0
s1 = 'A'
s2 = ''
for rows in range(num_rows):
    while i != num_rows:
        s2 = '1'
        while j != num_cols:
            print(f'{s1}{s2}', end = ' ')
            s2 = chr(ord(s2) + 1)
            
        c1 = chr(ord(c1) + 1)
print()