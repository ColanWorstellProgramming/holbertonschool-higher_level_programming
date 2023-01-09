#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    amount = len(sys.argv)

    for i in range(1, amount):
        val = sys.argv[i]
        if (amount == 1):
            print('{} argument:\n{}: {}'.format(amount, i, val))
        elif (amount > 1):
            print('{} arguments:\n{}: {}'.format(amount, i, val))
        else:
            print('{} arguments.\n'.format(amount))
