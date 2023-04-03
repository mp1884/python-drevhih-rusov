from sys import stdout

ноль = nol
целковый = celkoviy
полушка = целковый + целковый
чекушка = полушка * полушка
осьмушка = чекушка * полушка
пудовичок = осьмушка * полушка
медячок = пудовичок * полушка
серебрячок = медячок * полушка
золотничок = серебрячок * полушка
девятичок = золотничок * полушка
десятичок = девятичок * полушка

_цел = [
    'целковый',
    'полушка',
    'чекушка',
    'осьмушка',
    'пудовичок',
    'медячок',
    'серебрячок',
    'золотничок',
    'девятичок',
    'десятичок',
]


def pprint(*args, **kwargs):
    end = '\n'
    if 'end' in kwargs:
        end = kwargs['end']
    sep = ' '
    if 'sep' in kwargs:
        sep = kwargs['sep']
    for args in args:
        stdout.write(str(args))
        stdout.write(sep)

    stdout.write(end)


def счёт():
    pprint('ноль', *_цел)


цел = int
руны = str


def pnum(n):
    if n > десятичок:
        return 'Таких чисел в природе нет'

    b = list(bin(n)[2:])
    b.reverse()

    o = []
    for i in range(len(b)):
        if b[i] == '1':
            o.append(_цел[i])

    o.reverse()

    return ' '.join(o)


def _print(*args, **kwargs):
    for arg in args:
        if type(arg) == float:
            pprint('Дробных чисел в природе нет')
            return

        if type(arg) != int:
            pprint(arg, **kwargs)
            continue

        if arg == ноль:
            pprint('ноль')
        else:
            pprint(pnum(arg), **kwargs)

шизы = 'шизы'
русы = 'русы'

def help(arg):
    if arg == цел or type(arg) == int:
        pprint("Счет древних русов")
    elif arg == float or type(arg) == float:
        pprint("Сказки это все")
    else:
        if arg in ['шизы', 'русы']:
            pprint('Сверхлюди')


# int.__str__ = pnum
print = _print
писать = print
конч = exit