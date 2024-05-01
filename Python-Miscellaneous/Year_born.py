year_born = int(input('What year were you born? '))

if year_born >= 2010:
    print('You were born in Generation Alpha')
elif year_born >= 1995 and year_born <= 2009:
    print('You were born in Generation Z')
elif year_born >= 1981 and year_born <= 1994:
    print('You were born in Generation Y')
elif year_born >= 1964 and year_born <= 1980:
    print('You were born in Generation Y')
elif year_born >= 1946 and year_born <= 1963:
    print('You were born in Generation Y')
elif year_born >= 1901 and year_born <= 1945:
    print('You were born in Generation Y')
else:
    print("You'r too old to still exist")
