#!/usr/bin/env python3
import os
import sys
import fileinput
import argparse

def searchAndReplace(filepath,search,replace):
    counter = 0

    with fileinput.FileInput(filepath, inplace=True, backup='.bak') as file:
        for line in file:
            if search in line:
                counter+=1
                print(line.replace(search,replace), end='')


    return counter


def main():
    parser = argparse.ArgumentParser(description='Search and replace from a text file.')

    parser.add_argument('filepath', type=str)
    parser.add_argument('search', type=str)
    parser.add_argument('replace', type=str)

    args = parser.parse_args()

    search = args.search
    replace = args.replace

    print("Searching for: " + str(search))
    print("Replacing with: " + str(replace) + "\n")

    file = args.filepath

    totalReplacements = searchAndReplace(file,search,replace)

    print("Total number of occurences (and replacements) made: " + str(totalReplacements))


if __name__ == '__main__':
    main()