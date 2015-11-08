# Validates if the string of ints complies with UPC format
def checkDigits(stringOfInts):
   return len(stringOfInts) == 11

def getSum(stringOfInts):  
   sum = 0
   for index in range(len(stringOfInts)):
      if (index+1) % 2 != 0:
        sum+=3*int(stringOfInts[index])
      else:
         sum+=int(stringOfInts[index])
   return sum 

def findCheckDigit(sumOf11Digits):
   for i in range(0,9):
      if ((sumOf11Digits+i) % 10) == 0:
         return i
   return -1 

def main():
   # use str to save space
   stringOfInts = str(input("Enter Code: "))
   if checkDigits(stringOfInts):
      print(findCheckDigit(getSum(stringOfInts)))

main()




