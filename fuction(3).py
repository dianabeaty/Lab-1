spot1='|'
spot2='*'
spot3 = '-'
print('   y')
print('   ^')
space=1
for y in range (9,1,-1):
    print(y,' '*(space-len(str(y))), spot1+' '*(y-2)+spot2)
print(1, ' *', ' '*11)
print(0,' ',spot3*10, '>x')
print(' ', '   123456789')