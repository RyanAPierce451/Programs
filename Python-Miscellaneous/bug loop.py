print('(Enter 0 when finished)')
bug_num = int(input('How many bugs this week: '))
bug_total = 0
week = 1
while bug_num != 0:
    print ('Week ',week,' Has a total of ',bug_num,' bugs\n')
    
    week += 1
    print('(Enter 0 when finished)')
    bug_num = int(input('How many bugs this week: '))
    