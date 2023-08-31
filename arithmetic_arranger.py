import re


def arithmetic_arranger(problems, solutions=False):
  num1 = list()
  num2 = list()
  num3 = list()
  longest = list()
  operator = list()
  count = 0
  arranged_problems = ''

  #Uses regular expressions to separate the 2 numbers and operator into 3 different lists
  for x in problems:
    if re.search('[a-zA-Z]', x): #returns error if there are letters in the argument
      return "Error: Numbers must only contain digits."
      
    num1.append(int(re.findall('([0-9]+)\s.\s[0-9]+', x)[0]))
    operator.append(re.findall('[0-9]+\s(.)\s[0-9]+', x)[0])
    num2.append(int(re.findall('[0-9]+\s.\s([0-9]+)', x)[0]))
    count += 1

  for x in range(0, count):
    #Adds or subtracts numbers in lists according to their operator and puts them in a third list
    if '-' in operator[x]:
      num3.append(num1[x] - num2[x])
    elif '+' in operator[x]:
      num3.append(num1[x] + num2[x])
    else: #returns error if incorrect operand is given.
      return "Error: Operator must be '+' or '-'."

    #Finds the longest number between the operators and creates a new list
    longest.append(max(len(str(num1[x])), len(str(num2[x]))))

    if longest[x] > 4: #returns error if any of the numbers are greater than 4 digits
      return "Error: Numbers cannot be more than four digits."
  
  if count > 5: #returns error if there are too many problems.
    return "Error: Too many problems."
  
  #Adds first line to arithmetic_arranger
  for x in range(0, count):
    arranged_problems += (((2 + longest[x] - len(str(num1[x]))) * ' ') +
                          str(num1[x]))
    if x == (count - 1):
      arranged_problems += ('\n')
    else:
      arranged_problems += ('    ')

  #Adds second line to arithmetic_arranger
  for x in range(0, count):
    arranged_problems += (operator[x] +
                          ((1 + longest[x] - len(str(num2[x]))) * ' ') +
                          str(num2[x]))
    if x == (count - 1):
      arranged_problems += ('\n')
    else:
      arranged_problems += ('    ')

  #Adds third line to arithmetic_arranger
  for x in range(0, count):
    arranged_problems += ((longest[x] + 2) * '-')
    if solutions == True:
      if x == (count - 1):
        arranged_problems += ('\n')
      else:
        arranged_problems += ('    ')
    else:
      if x != (count - 1):
        arranged_problems += ('    ')

  #Adds fourth line to arithmetic_arranger if the second argument is set to True
  if solutions == True:
    for x in range(0, count):
      arranged_problems += (((2 + longest[x] - len(str(num3[x]))) * ' ') +
                          str(num3[x]))
      if x != (count - 1):
        arranged_problems += ('    ')

  return arranged_problems
