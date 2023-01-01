import time

def DigitSum(i):
    # Compute sum of digits
    digitSum = 0
    while i > 0 :
        rem = i % 10
        digitSum = digitSum + rem
        i = i // 10     
    # Check if sum of digits is divisible by 3
    return (digitSum)

def checkFour(i):
    st = str(i)
    n = len(st)
    # Empty string
    if (n == 0):
        return False
    # If there is single digit
    if (n == 1):
        return ((st[0] - '0') % 4 == 0)
    # If number formed by last two digits is divisible by 4.
    last = (int)(st[n - 1])
    second_last = (int)(st[n - 2])
 
    return ((second_last * 10 + last) % 4 == 0)

def checkEight(i):
    num = str(i)[-3:]
    
    return(int(num) % 8 == 0)

def checkEleven(i):
    st = str(i)
    n = len(st)
    # Compute sum of even and odd digit
    # sums
    oddDigSum = 0
    evenDigSum = 0
    for i in range(0,n) :
        # When i is even, position of digit is odd
        if (i % 2 == 0) :
            oddDigSum = oddDigSum + ((int)(st[i]))
        else:
            evenDigSum = evenDigSum + ((int)(st[i])) 
    return ((oddDigSum - evenDigSum) % 11 == 0)

tic = time.perf_counter()
i = 10
upTo = input("Number to check to: ")
while(i <= int(upTo)):
    divisions = str(i) + " - "
    if(i % 2 == 0):
        divisions = divisions + "2"
    if(DigitSum(i) % 3 == 0):
        divisions = divisions + ", 3"
    if(("2" in divisions) & ("3" in divisions)):
        divisions = divisions + ", 6"
    if(checkFour(i)):
        divisions = divisions + ", 4"
    if(int(str(i)[-1]) == 0 or int(str(i)[-1]) == 5):
        divisions = divisions + ", 5"
    if(checkEight(i)):
        divisions = divisions + ", 8"
    if(DigitSum(i) % 9 == 0):
        divisions = divisions + ", 9"
    if(int(str(i)[-1]) == 0):
        divisions = divisions + ", 10"
    if(checkEleven(i)):
        divisions = divisions + ", 11"
    if(("3" in divisions) & ("4" in divisions)):
        divisions = divisions + ", 12"
    
    print(divisions)

    i += 1

toc = time.perf_counter()
print(f"Time taken: {toc - tic:0.4f} seconds")