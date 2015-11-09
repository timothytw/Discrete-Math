'''
Validates if the string of digits complies with UPC format
UPC format: 3x1 + x2 + 3x3 + ... + 3(2x+1)... is congruent to 0 (mod 10)
Multiply 3 to the oddth placed-digit and add those to the other digits
Note: The 1st digit is the left most digit of the string
If the (summation + n) modulo 10 is 0, then n is the check digit

Format has to be 11 digits

Given: 12300000000, 1 is x1, 2 is x2, 3 is x3... etc 
Therefore, 123 is evaluated as 3(1)+2+3(3)+0+3(0)...+3(0) = 14
( 14 + (6) ) mod 10 = 0 ; therefore, 6 is the check digit 

Will return -1 if no number is found which means the string of digits is not valid
'''
# check if using python2/3
def getStringOfDigits():
   try:
      stringOfDigits = raw_input("Enter Code: ")
   except NameError:
   # python3 input() is the python2 raw_input()
      stringOfDigits = input("Enter Code: ") 
   return stringOfDigits

def checkDigits(stringOfDigits):
   return len(stringOfDigits) == 11

def getSum(stringOfDigits):  
   sum = 0
   for index in range(len(stringOfDigits)):
      # index starts at 0 but format starts at x1
      if (index+1) % 2 != 0:
      # multiply 3 to the oddth placed-digit
        sum+=3*int(stringOfDigits[index])
      else:
         sum+=int(stringOfDigits[index])
   return sum 

def findCheckDigit(sumOf11Digits):
   for i in range(0,9):
      if ((sumOf11Digits+i) % 10) == 0:
         return i
   return -1 

def main():
   stringOfDigits = getStringOfDigits() 
   if checkDigits(stringOfDigits):
      print(findCheckDigit(getSum(stringOfDigits)))
   else:
      print("Not 11 digits")

main()


