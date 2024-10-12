BLACK = '\u001b[40m'
END = '\u001b[0m'
WHITE = '\u001b[48;5;231m'




def draw_patterns(offset=0, length1=3, length2=1, length3=2, length4=5, length5=0, length6=7, number_of=2):
    line1 = " " * length1
    line2 = " " * length2
    line3 = " " * length3
    line4 = " " * length4
    line5 = " " * length5
    line6 = " " * length6
    print(f"{' ' * offset}{WHITE}{line1}{END}{' ' * offset}{BLACK}{line2}{END}{' ' * offset}{WHITE}{line1}{END}"*number_of)
    print(f"{' ' * offset}{WHITE}{line3}{END}{' ' * offset}{BLACK}{line1}{END}{' ' * offset}{WHITE}{line3}{END}"*number_of)
    print(f"{' ' * offset}{WHITE}{line2}{END}{' ' * offset}{BLACK}{line4}{END}{' ' * offset}{WHITE}{line2}{END}"*number_of)
    print(f"{' ' * offset}{WHITE}{line5}{END}{' ' * offset}{BLACK}{line6}{END}{' ' * offset}{WHITE}{line5}{END}"*number_of)
    print(f"{' ' * offset}{WHITE}{line2}{END}{' ' * offset}{BLACK}{line4}{END}{' ' * offset}{WHITE}{line2}{END}"*number_of)
    print(f"{' ' * offset}{WHITE}{line3}{END}{' ' * offset}{BLACK}{line1}{END}{' ' * offset}{WHITE}{line3}{END}"*number_of)
    print(f"{' ' * offset}{WHITE}{line1}{END}{' ' * offset}{BLACK}{line2}{END}{' ' * offset}{WHITE}{line1}{END}"*number_of)

draw_patterns()