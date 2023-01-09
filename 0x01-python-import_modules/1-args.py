#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    amount = len(sys.argv)

if (amount == 1):
    print('{} argument:\n'.format(amount-1))
elif (amount > 1):
    print('{} arguments:\n'.format(amount-1))
elif (amount == 0):
    print('{} arguments.\n'.format(amount-1))

    for i in range(1, amount):
        val = sys.argv[i]
        if (amount == 1):
            print('{}: {}'.format(i, val))
        elif (amount > 1):
            print('{}: {}'.format(i, val))
