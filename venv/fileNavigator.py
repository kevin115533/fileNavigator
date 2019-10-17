"""
File: File Navigator
This program allows a user to input lines of text into a file and then navigate the file by line number
"""

def main():
    fileName = input("Enter the name of your file: ")
    file = open(fileName + ".txt", 'w')



main()

