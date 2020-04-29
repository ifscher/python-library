from random import choice

style = [0, 1, 4, 7]
colors = [30, 31, 32, 33, 34, 35, 36, 37]
back = [40, 41, 42, 43, 44, 45, 46, 47]

texto = 'Look up to the sky'
count = 0

for c in colors:
    if count >= len(style):
        count = 0
    s = style[count]
    print(f'\033[7;{c};{c+10}m {s} \033[m\033[{s};{c}m {texto}\033[m')
    count = count + 1
