#!/usr/bin/python3
if __name__ == '__main__':

    amount = len(argv)

    for i in range(0, amount):

        if (amount == 1):
            print('{} argument:\n{}: {}'.format(amount, i+1, val))
        elif (amount > 1):
            print('{} arguments:\n{}: {}'.format(amount, i+1, val))
        else:
            print('{} arguments.\n'.format(amount))
