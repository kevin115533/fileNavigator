"""
File: File Navigator
This program allows a user to input lines of text into a file and then navigate the file by line number
"""

def main():
    fileName = input("Enter the name of your file: ")
    file = open(fileName + ".txt", 'w')
    wordList = []
    word = input("Enter a string or hit Enter to quit: ")

    while word != "":
        wordList = wordList + [word]
        word = input("Enter a string or hit Enter to quit: ")

    for x in range(len(wordList)):
        file.write(str(x + 1) + " " + wordList[x] + "\n")

    file = open(fileName + ".txt", 'r')
    textLines = file.readlines()
    lineNum = input("Enter a line number you want to print or press 0 to quit: ")
    while lineNum != "0":
        print(textLines[int(lineNum) - 1])
        lineNum = input("Enter a line number you want to print or press 0 to quit: ")

    file.close()
main()

