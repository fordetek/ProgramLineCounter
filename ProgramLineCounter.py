"""
Name: footballstats.py
Description: This program stores teams and there winning and losing score
to which mulitple calculations can be used to give a number of statistics,
it achives this by optaining user inputted information about the names
of the teams and the win and lose scores
Author: Michael Forde
"""
# this imports glob
import glob

# this self-defined function opens a file and reads all its lines but only counts them if they dont contain a comment
# or a new line
def fileLineCount(name):
    filehandle = open(name, 'r')
    count = 0
    for line in filehandle:
        if line.startswith('#'):
            continue
        if line.startswith('\n'):
            continue
        count += 1

    return(count)

# this self-defined function gets given a pathname and locates all the .py files in a given pathname and calls out the
# fileLineCount function to read every file in that file directory and adds them together
def directoryLineCount(path):
    pyfiles = glob.glob('%s%s' % (path, '*.py'))
    directoryLineCount = 0
    for file in pyfiles:
        fileLineCount(file)
        directoryLineCount = directoryLineCount + fileLineCount(file)

    print(directoryLineCount)

# this askes the user for the file directory they want to count the lines in
path = input('Enter the pathname of the directory you want to count python lines of: ')
print(directoryLineCount(path))