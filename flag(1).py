GREEN = '\u001b[42m'
YELLOW = '\u001b[48;5;226m'
RED = '\u001b[41m'
END = '\u001b[0m'

def draw_line(offset=0, length1=7, length2=9):
    line = " " * length1
    line2 = " " * length2
    print(f"{' ' * offset}{GREEN}{line}{END}{' ' * offset}{YELLOW}{line2}{END}")

def draw_line1(offset=0, length1=7, length2=9):
    line = " " * length1
    line2 = " " * length2
    print(f"{' ' * offset}{GREEN}{line}{END}{' ' * offset}{RED}{line2}{END}")

draw_line()
draw_line()
draw_line1()
draw_line1()