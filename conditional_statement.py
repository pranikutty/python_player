#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      16ece018
#
# Created:     21/10/2017
# Copyright:   (c) 16ece018 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    x = int(input("Please enter an integer: "))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

if __name__ == '__main__':
    main()
