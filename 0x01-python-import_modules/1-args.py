#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    amount = len(sys.argv)

    for i in range(0, amount):
        val = sys.argv[i]
        if (amount == 1):
            print('{} argument:\n{}: {}'.format(amount, i+1, val))
        elif (amount > 1):
            print('{} arguments:\n{}: {}'.format(amount, i+1, val))
        else:
            print('{} arguments.\n'.format(amount))
