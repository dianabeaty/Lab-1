GREEN = '\u001b[42m'
RED = '\u001b[41m'
END = '\u001b[0m'

def draw_linefor1(offset=0, length=65):
    line = " " * length
    print(f"{' ' * offset}{GREEN}{line}{END}")

def draw_linefor2(offset=0, length=71):
    line = " " * length
    print(f"{' ' * offset}{RED}{line}{END}")

file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
file.close()
answer = []
for i in list:
    if (0 <= i <= 5) or (-5 <= i <= 0):
        answer.append(float(i))

number_of = len(answer)
the_numbers_are_zero_to_five = 0
for i in answer:
    if 0 <= i <= 5:
        the_numbers_are_zero_to_five += 1

the_numbers_are_five_to_zero = 0
for i in answer:
    if -5 <= i <= 0:
        the_numbers_are_five_to_zero += 1

print(f'Всего: {number_of}')
print('\u001b[32m')
print(f'Числа от 0 до 5: {the_numbers_are_zero_to_five}')
print('\u001b[31m')
print(f'Числа от 0 до -5: {the_numbers_are_five_to_zero}')
draw_linefor1()
draw_linefor2()