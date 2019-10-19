# -*- coding: utf-8 -*-
""""
This script illustrates command line handling
"""

import argparse


def make_parser():
    """Build command line parser"""
    parser = argparse.ArgumentParser(description='Sample CLI application')
    return parser


def set_parser_arguments(parser):
    """Add specific command line arguments to the parser"""
    parser.add_argument('--say-hello', dest='say_hello', action='store_true',
                        help='If given print a message')
    parser.add_argument('--count', dest='count', default=1, type=int,
                        help='Number of repetitions')
    parser.add_argument('filename')


def run():
    """ Main function - parser command line and prints some messages"""
    parser = make_parser()
    set_parser_arguments(parser)
    args = parser.parse_args()
    if args.say_hello:
        for i in range(args.count):
            print('Hello')
    else:
        print('No greetings')
    print('filename: ', args.filename)

if __name__ == '__main__':
    run()