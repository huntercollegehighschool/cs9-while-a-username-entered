'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
timesToPrint = int(input('Times to print: '))
timesPrinted = 0

while timesPrinted < timesToPrint:
  timesPrinted += 1
  print('Hunter')