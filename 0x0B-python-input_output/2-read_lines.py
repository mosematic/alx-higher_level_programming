#!/usr/bin/python3
'''
read_lines function
'''


def read_lines(filename="", nb_lines=0):
    '''
    Reads n lines of a txt file and prints it
    '''
    i = 0
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        for line in f:
            i += 1
            print(line, end='')
            if nb_lines == i:
                break
