#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Filename: mygrep.py
Author: Simon Dahlberg

licence: GPL

This is my grep program.
"""
from optparse import OptionParser
import re

VERSION_MAJOR ='0'
VERSION_MINOR ='1'
VERSION_EXTRA ='alpha-0001'

VERSION='%s.%s-%s' % (VERSION_MAJOR, VERSION_MINOR, VERSION_EXTRA)

VERBOSITY = 1

KEYWORDS = ['if', 'else', 'elif', 'for', 'def', 'with', 'while', 'self']

def v_print(msg, v=1):
    if VERBOSITY >= v:
        print msg

def set_cfont(color):
    

    print '\033[1;%sm' % fg[color]

def cprfx(color):
    fg = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenda': '35',
        'cyan': '36',
        'white': '37',
        }
    
    return '\033[1;%sm' % fg[color]

def main():
    global VERBOSITY
    
    usage = '%prog [options] <PATTERN> <FILE>'
    version = '%%prog    %s' % VERSION
    parser = OptionParser(usage=usage, version=version)

    parser.add_option('-v', '--verbosity',
                      action='store', dest='verbosity',
                      choices=['0', '1', '2'], default='1',
                      help='verbosity of output. 0 = minimal, 1 = normal, 2 = all')

    options, args = parser.parse_args()

    VERBOSITY = int(options.verbosity)

    if len(args) != 2:
        parser.error('Incorrect number of arguments')

    pattern = args[0]
    filename = args[1]

    set_cfont('white')
    v_print('Grepping file "%s" using pattern "%s"' % (filename, pattern), 2)

    set_cfont('green')
    if pattern[0] != '^':
        pattern = '.*' + pattern[1:]

    with open(filename) as f:
        for line in f:
            if re.match(pattern, line):
                ls = line.split(' ')
                for word in ls:
                    if word in KEYWORDS:
                        set_cfont('white')
                        print word,
                        set_cfont('green')
                    else:
                        set_cfont('green')
                        print word,
    
if __name__ == '__main__':
    main()
    
