# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

from shutil import copyfile
import sys


def check_user_inputs(arguments_list):
    if len(arguments_list) == 1:
        print("copy [source] [destination]")
    elif len(arguments_list) == 3:
        print("No destination provided")
    elif len(arguments_list) == 4:
        copy_file(arguments_list[2], arguments_list[3])


def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dst: dst.write(src.read())
    except Exception:
        print("File copy error!")


check_user_inputs(sys.argv)