#!/usr/bin/python3
def safe_print_division(a, b):
    x = 0
    try:
        x = a / b
        str = '{} {}'.format('Inside result:', x)
    except ZeroDivisionError:
        str = 'None'
    finally:
        print('{}'.format(str))
    return str
