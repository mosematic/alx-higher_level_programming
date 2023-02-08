#!/usr/bin/python3
'''
read_file function
'''


def read_file(filename=""):
    '''
    Reads a text file (UTF8) and prints to stdout
    '''
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
