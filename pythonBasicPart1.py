#Python basic (Part -I) [150 exercises with solution]
#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#https://www.tutorialspoint.com/python3/python_dictionary.htm
#https://docs.python.org/3/tutorial/

from __future__ import print_function
##############################################################################################################################
'''1. Write a Python program to print the following string in a specific format (see the output). 
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky.
Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def printStr():
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star,\n\t How I wonder what you are")

#print(printStr())

##############################################################################################################################
'''2. Write a Python program to get the Python version you are using. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyVer():
    import sys
    print("Python version: ",sys.version)
    print("Python version in detail: ",sys.version_info)

#print (pyVer())

##############################################################################################################################
'''3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import datetime
def pyDate():
    time = datetime.datetime.now()
    print("Date and Time: ",time.strftime("%Y-%m-%d %H:%M:%S"))

#print(pyDate())
    
##############################################################################################################################
'''4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
Sample Output :
r = 1.1
Area = 3.8013271108436504'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
from math import *
def pyMath(r):
    area = pi * r**2
    print("Area of circle: ",area)

#print(pyMath(2))

##############################################################################################################################
#5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyStr():
    first = input("Enter first name:")
    last = input("Enter last name:")
    print(last + " " + first)
#print(pyStr())

##############################################################################################################################
'''6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyToList():
    i = input("Please enter comma-separated numbers:")
    l = []
    for j in i:
        l.append(j)
    print("List: ", l)
    tup = tuple(l)
    print("Tuple: ", tup)
#print(pyToList())

#//Another way to write python programm//
    
def py2List():
    v = input("Please enter comma-separated numbers:")
    lst = v.split(",")
    tup = tuple(lst)
    print("List: ", lst)
    print("Tuple: ", tup)
    
#print(py2List())    

##############################################################################################################################
'''7. Write a Python program to accept a filename from the user and print the extension of that. 
Sample filename : abc.java
Output : java'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyStr():
    a = "soumen jana.java"
    indx = a.split(".")
    print ("This is my file extention: " + "." + indx[1])    

#print(pyStr())

##############################################################################################################################
'''8. Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyColor():
    color_list = ["Red","Green","White" ,"Black"]
    Len = len(color_list)
    print("First color: ", color_list[0])
    print("Last color: ", color_list[Len-1])

#print(pyColor())

##############################################################################################################################
'''9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyExam():
    exam_st_date = (11, 12, 2014)
    print('The examination will start from : %i/%i/%i' % exam_st_date)


##############################################################################################################################
'''10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
Sample value of n is 5
Expected Result : 615'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyInt():
    a = int(input("Enter a number: "))
    n1 = int('%a' %a)   #if int() not declare. Python will take as string. In this case it will print 555555 instead if 615
    n2 = int('%a%a' %(a,a))
    n3 = int('%a%a%a' %(a,a,a))
    print("Expected Result: ", n1+n2+n3)

#print(pyInt())

##############################################################################################################################
'''11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyAbs(a):
    print(abs.__doc__)
    
#print(pyAbs(123))

##############################################################################################################################
'''12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import calendar
def pyCal(y,m):
    return(calendar.month(y,m))
    
#print(pyCal(2020,1))

##############################################################################################################################
'''13. Write a Python program to print below sample string.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyPrint():
    print('''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
''')
    
#print(pyPrint())

##############################################################################################################################
'''14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
from datetime import *
def pyDOB():
    dt1 = date(1983,3,3)
    dt2 = date.today()
    dif_dt = dt2-dt1
    #print(type(dif_dt))
    print("My Age in Days: ",dif_dt)

#print(pyDOB())

##############################################################################################################################
'''15. Write a Python program to get the volume of a sphere with radius 6.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
from math import *
def pyVol(r):
    v = 4/3 * pi * r**3
    print("Volume of a sphere is: ",v)

#print(pyVol(3))

    
##############################################################################################################################
'''16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return
double the absolute difference.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyDiff(n):
    if n <= 17:
        return 17-n
    else:
        return(n-17)*2
    
#print(pyDiff(22))
#print(pyDiff(17))
#print(pyDiff(16))


##############################################################################################################################
'''17. Write a Python program to test whether a number is within 100 of 1000 or 2000.''' 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyNearThousand(n):
    return((abs(1000-n) <= 100) or (abs(2000-n) <= 100))

#print(pyNearThousand(0))
#print(pyNearThousand(400))
#print(pyNearThousand(4000))
#print(pyNearThousand(900))

##############################################################################################################################
'''18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of
their sum. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySum(x,y,z):
    sum = x + y +z
    if x == y and y == z:
        sum = sum * 3
    return sum
    
#print(pySum(1,1,1))
#print(pySum(1,1,2))


##############################################################################################################################
'''19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string
already begins with "Is" then return the string unchanged. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyStrCheck(txt):
    spl = txt.split(" ")
    if spl[0] != "is":
        return ("is " + txt)
    return txt
    
#print(pyStrCheck("this your no?"))
#print(pyStrCheck("is this your car?"))


#////////////////Other way to write code for this////////////////

def pyStrCheck2(txt):
    if len(txt) >=2 and txt[:2] == "is":
        return txt
    return ("is " + txt)

#print(pyStrCheck("is this you?"))
#print(pyStrCheck("this WB team?"))


##############################################################################################################################
'''20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyNonInt(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result

#print(pyNonInt("hi", 4))
    

##############################################################################################################################
'''21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate
message to the user.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyEvenOdd(n):
    if n%2 == 0:
        return (str(n) + " is Even number")
    return (str(n) + " is Odd number")

#print(pyEvenOdd(99))
#print(pyEvenOdd(90))


##############################################################################################################################
'''22. Write a Python program to count the number 4 in a given list. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyCountFromList(l):
    count = 0
    for i in l:
        if i == 4:
            count = count + 1
    return count

#print(pyCountFromList([1,4,4,5,4,4]))
#print(pyCountFromList([4,2,2,5,2,4]))

#//Other way to do//

def pyCountFromList1(l, n):
    return l.count(n)

#print(pyCountFromList1([1,4,4,5,4,4], 4))
#print(pyCountFromList1([1,2,2,5,2,4], 4))

##############################################################################################################################
'''23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyCh(st, n):
    if len(st) < 2:
        return st * n
    return st[:2] * n

#print(pyCh('abcdef', 2))
#print(pyCh('pip', 3))


##############################################################################################################################
'''24. Write a Python program to test whether a passed letter is a vowel or not. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def pyIsVow(char):
    vowel = "aeiou"
    return char in vowel

#print (pyIsVow("c"))
#print (pyIsVow('u'))

#//////////////////////////Other way to do this////////////////////////

def pyIsVowel(s):
    l = ['a','e','i','o','u']
    for i in l:
        return s[0] in l
    
#print (pyIsVowel("epple"))
#print (pyIsVowel("ppleo"))


#//////////////////////////Other way to do this//////////////////////////
        
def pyIsVo(s):
    l = ['a','e','i','o','u']
    if s[0] in l:
        return ("Vowel")
    return ("Consonant")

#print (pyIsVo("ennnnnn"))
#print (pyIsVo("znnnnnn"))

#//////////////////////////Other way to do this//////////////////////////
def pyIsV(s):
    l = ['a','e','i','o','u']
    for val in l:
        if s[0] == val:
            return "This is Vowel"
    return "This is not vowel"

#print (pyIsV("lnnnnnn"))
#print (pyIsV("annnnnn"))


##############################################################################################################################
'''25. Write a Python program to check whether a specified value is contained in a group of values. 
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyValCheck(n):
    l = [1,2,3,4,5]
    return n in l

#print(pyValCheck(-1))
#print(pyValCheck(4))
#print(pyValCheck(10))

#//////////////////////////Other way to do this//////////////////////////
def pyIsGrpMember(grp_lst, n):
    for val in grp_lst:
        if n == val:
            return True
    return False

#print (pyIsGrpMember([1,2,3,4,5,6,7,8,9], 11))
#print (pyIsGrpMember([1,2,3,4,5,6,7,8,9], 6))

##############################################################################################################################
'''26. Write a Python program to create a histogram from a given list of integers.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyHistogram(lst):
    for num in lst:
        print (num * "*")
    
#print (pyHistogram([1,2,3,4,5,6,7,8,9]))

#//////////////////////////Other way to do this//////////////////////////
def pyHistogram2(lst):
    for num in lst:
        (output, t) = ("", num)
        while (t > 0):
            (output, t) = (output + "*", t - 1)
        print (output)

#print (pyHistogram2([1,2,3,4,5,6]))
#print (pyHistogram2([6,5,4,3,2,1]))


##############################################################################################################################
'''27. Write a Python program to concatenate all elements in a list into a string and return it. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyLstToStr(lst):
    string = ""
    for ele in lst:
        string += str(ele)
    #print (type(string))
    return string

lst1 = [1,2,3,4,5]
lst2 = ["Hi"," ","Soumen"]
#print (pyLstToStr(lst1))
#print (pyLstToStr(lst2))
#print (pyLstToStr(["This is ",2]))

##############################################################################################################################
'''28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any
numbers that come after 237 in the sequence. 
Sample numbers list :

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
def pyEven(numbers):
    Even = []
    for ele in numbers:
        if ele % 2 == 0 and ele <= 237:
            Even.append(ele)
    return "Even numbers are: {}".format(Even)

#print (pyEven(numbers))

##############################################################################################################################
'''29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output : {'Black', 'White'}'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
color_list_1 = set(["White", "Pink", "Red"])
color_list_2 = set(["Red", "Blue", "Black"])

def pySetNotMatch():
    set3 = set()
    for color in color_list_1:
        if color not in color_list_2:
            set3.add(color)
    return set3
            
#print(pySetNotMatch())

#//////////////////////////Other way to do this//////////////////////////

def pySetNotMatch2():
    print (color_list_1.difference(color_list_2))


#print(pySetNotMatch2())

##############################################################################################################################
'''30. Write a Python program that will accept the base and height of a triangle and compute the area.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyArea(b, h):
    A = (b*h)/2
    return "Area of triangle: {}".format(A)

#print(pyArea(10, 5))

##############################################################################################################################
'''31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyGCD(a, b):
    (num, lst) = (1, [])
    while num <= a and num <= b:
        if a % num == 0 and b % num == 0:
            lst.append(num)
        num += 1
    print("Common dividers are: ", lst)
    return "Greatest common divisor: {}".format(max(lst))

#print (pyGCD(400, 480))
        
##############################################################################################################################
'''32. Write a Python program to get all Prime numbers from given range.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyPrime(start, end):
    lst = []
    for val in range(start,end + 1):
        if val > 1:
            for i in range(2, val):
                if val % i == 0:
                    break
            else:
                lst.append(val)
    return (lst)
                
#print (pyPrime(2,30))

###################### Another way to do ######################

def PrimeNumber():
    for i in range(100):
        #print(50*'-')
        f=0
        for j in range(2,i):
            if(i%j==0):
                f=1
                #print(50*'*')
                break
        if (f==0):
            print(i)
            
#print (PrimeNumber())
            
##############################################################################################################################
'''32. Write a Python program to Multiply all numbers in the lis.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyMultiply(lst1):
    result = 1
    for i in lst1:
        result *= i
    return result

#print(pyMultiply([1,2,3,4,5]))

##############################################################################################################################
'''32. Write a Python program to get the least common multiple (LCM) of two positive integers.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
lst = []
def pyLCM(a, b):
        for i in pyPrime(2,100):             #// Called pyPrime(start, end) function//
            if a%i == 0 and b%i == 0:
                lst.append(i)
                (a,b) = (a//i,b//i)
                pyLCM(a,b)
                break
        else:
            lst.append(a)
            lst.append(b)
        #print (lst)
        return "LCM of {} and {} is: {}".format (a,b, pyMultiply(lst))    #//Called pyMultiply(lst1) function//

#print (pyLCM(901,601))

#//////////////////////////Other way to do this//////////////////////////

def pyLcm(x, y):
   if x > y:
       (z, z) = (x, y)
   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1
   return "LCM of {} and {} is: {}".format(x,y,lcm)

#print(pyLcm(9, 6))

##############################################################################################################################
'''33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySum(x, y, z):
    if x == y or  y== z or x == z:
        sum1 = 0
    else:
        sum1 = x + y + z
    return "Sum of three number: {}".format (sum1)

#print(pySum(10, 20, 30))
#print(pySum(10, 10, 30))
#print(pySum(10, 20, 20))
#print(pySum(10, 20, 10))
#print(pySum(10, 10, 10))


##############################################################################################################################
'''34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySUM(x, y):
    sum1 = x + y
    if sum1 in range(15,21):
        return "Sum of two given integer is: 20"
    return "Sum of two given integer is: {}".format (sum1)

#print (pySUM(10, 5))
#print (pySUM(10, 7))
#print (pySUM(10, 10))
#print (pySUM(10, 11))
#print (pySUM(1, 5))
#print (pySUM(10, 22))


##############################################################################################################################
'''35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.''' 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyInt(x, y):
    dif = max(x, y) - min(x, y)
    sum1 = x + y
    if sum1 == 5 or dif == 5 or x == y:
        return True
    return False

#print (pyInt(2, 2))
#print (pyInt(3, 2))
#print (pyInt(2, 6))

 
#############################################################################################################################
'''36. Write a Python program to add two objects if both objects are an integer type. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyIntCheck(x, y):
    if type(x) == int and type(y) == int:
        sum1 = x + y
        return "Sum of two object: {}".format (sum1)
    return "not a integer type"

#print (pyIntCheck(10, 10))
#print (pyIntCheck("hi", "soumen"))
#print (pyIntCheck(10, "hi"))

#//////////////////////////Other way to do this//////////////////////////

def pyIntCheck(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Enter both objects as integer type")
    return "Sum of two object: {}".format (x + y)

#print (pyIntCheck(10, 10))
#print (pyIntCheck("hi", "soumen"))
#print (pyIntCheck(10, "hi"))


##############################################################################################################################
'''37. Write a Python program to display your details like name, age, address in three different lines. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyAdd():
    (name, age, address) = ("Soumen", 35, "bangalore")
    return "Name: {}\nAge: {}\nAddress: {}".format(name, age, address)

#print (pyAdd())                            

##############################################################################################################################
'''38. Write a Python program to solve (a + b)^2 whole square. (a + b)^2 = a^2 + b^2 + 2ab
 Test Data : a = 4, a = 3
Expected Output : (4 + 3) ^ 2) = 49'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyMath1(a, b):
    result = ((a*a) + 2*a*b + (b*b))
    return "({} + {})^2 = {}".format (a, b, result)
#print (pyMath1(4, 4))
    
##############################################################################################################################
'''39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. 
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyLoan(amt, rate, year):
    future_value = amt*((1+(0.01*rate))**year)
    return "Total: {}".format (round(future_value))

#print (pyLoan(1400000, 10.5, 5))

##############################################################################################################################
'''40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import math 
def pyCoordinate():
    (coord1, coord2) = ([2, 4], [3,2])
    distance = math.sqrt (((coord1[0] - coord2[0])**2) + ((coord1[1] - coord2[1])**2))
    return "Distance is: {}".format(distance)

#print (pyCoordinate())
    
##############################################################################################################################
'''41. Write a Python program to check whether a file exists. Check whether the specified path is an existing file '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import os
def pyFileExists():
    path = 'D:\\Python SVN\\Python\\aa.py'
    isFile = os.path.isfile(path)      #// if aa.py not present in the path, "os.path.isfile" function will return False //
    #isFile = os.path.isfile('aa.py')
    return isFile

#print (pyFileExists())

##############################################################################################################################
'''42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyOSType():
    import struct
    return(struct.calcsize("P") * 8)   #//https://docs.python.org/2/library/struct.html//

#print (pyOSType())
    
##############################################################################################################################
'''43. Write a Python program to get OS name, platform and release information. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyOSName():
    import platform, os
    print("OS Name: ",os.name)
    print("Platform: ",platform.system())
    return "OS Release: {}".format (platform.release())

#print (pyOSName())

##############################################################################################################################
'''44. Write a Python program to locate Python site-packages.''' 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySitePack():
    import site; 
    return site.getsitepackages()

#print(pySitePack())

##############################################################################################################################
'''45. Write a python program to call an external command in Python. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyExtCommand():
    from subprocess import call
    call(["ls", "-l"])

#print (pyExtCommand())

##############################################################################################################################
'''46. Write a python program to get the path and name of the file that is currently executing. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyPath():
    import os       #//https://stackoverflow.com/questions/37863476/why-would-one-use-both-os-path-abspath-and-os-path-realpath//
    return "Current File Name : {}".format (os.path.realpath(__file__))

#print (pyPath())

##############################################################################################################################
'''47. Write a Python program to find out the number of CPUs using. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyCPU():
    import multiprocessing
    return "number of CPUs: {}".format(multiprocessing.cpu_count())

#print (pyCPU())

##############################################################################################################################
'''48. Write a Python program to parse a string to Float or Integer. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyStrToFloat():
    s = "123.321"
    f = float(s)
    i = int(f)
    return "From string {}, we got interger valie as {} and float value as {}".format(s, i, f)

#print (pyStrToFloat())

##############################################################################################################################
'''49. Write a Python program to list all files in a directory in Python. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
from os import listdir
from os.path import isfile, join
def pyFilesInDir():
    files = []
    for f in listdir('D:\Python SVN\Python'):
        if os.path.isfile(f):
            files.append(f)
    return files
                                 
#print(pyFilesInDir())

##############################################################################################################################
'''50. Write a Python program to print without newline or space. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyNoSpace():
    for i in range(1,10):
        print("*", end="")

#print(pyNoSpace())

##############################################################################################################################
'''51. Write a Python program to determine profiling of Python programs. 
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed.
These statistics can be formatted into reports via the pstats module.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import cProfile
def pyExample():
    print(2**100)
    
#cProfile.run('pyExample()')

##############################################################################################################################
'''52. Write a Python program to print to stderr.''' 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
#from __future__ import print_function
import sys
def pyEprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    #print(*args, **kwargs)

#pyEprint("abc", "efg", "xyz", sep="--")

##############################################################################################################################
'''53. Write a python program to access environment variables. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import os
def pyEnVeriable(*values):
    for i in values:
        print(i, end = "\n#------------------------------------------------------#\n")
    
#pyEnVeriable(os.environ,os.environ['HOME'],os.environ['path'])    

##############################################################################################################################
'''54. Write a Python program to get the current username '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

import getpass, socket    #//https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo///
def pyGetUser():
    return "User Name: {}\nHost Name: {}".format (getpass.getuser(), socket.gethostname())

#print(pyGetUser())

##############################################################################################################################
'''55. Write a Python to find local IP addresses using Python's stdlib '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import socket
def pyGetIP():
    print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

#print(pyGetIP())

##############################################################################################################################
'''56. Write a Python program to get height and width of the console window. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyTerminalSize():
    import fcntl, termios, struct  #//This is for Linux//
    th, tw, hp, wp = struct.unpack('HHHH',fcntl.ioctl(0, termios.TIOCGWINSZ,struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

#print('Number of columns and Rows: ',pyTerminalSize())

##############################################################################################################################
'''57. Write a program to get execution time for a Python method. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyExeTine():
    import time
    str_time = time.time()
    out = [i**2 for i in range(10000)]
    print (out)
    end_time = time.time()
    tot_time = str_time - end_time
    print ("Time taken: ",tot_time)
    
#print (pyExeTine())

##############################################################################################################################
'''58. Write a python program to sum of the first n positive integers. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySum(n):
    sum_num = (n*(n+1))/2
    return sum_num

#print (pySum(10))
   

##############################################################################################################################
'''59. Write a Python program to convert height (in feet and inches) to centimeters. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyConvert(feet, inch):
    return "{} feet = {} Centimeter\n{} inch = {} Centimeter".format(feet, round(30.48*feet), inch, round(2.54*inch))


#print(pyConvert(9, 9))

##############################################################################################################################
'''60. Write a Python program to calculate the hypotenuse of a right angled triangle.''' 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyHypotenuse(a, b):
    c = sqrt(a**2 + b**2)
    return "Hypotenuse of triangle is {}".format(c)

#print(pyHypotenuse(10, 11))

##############################################################################################################################
'''61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyFromFeet(n):
    return "{} Feet = {} inch {} yars {} mile".format (n, 12*n, round((0.333333*n),2), round((0.00018939375*n),2))
    
#print(pyFromFeet(1000))

#//////////////////////////Other way to do this//////////////////////////

#d_ft = int(input("Input distance in feet: "))
#d_inches = d_ft * 12
#d_yards = d_ft / 3.0
#d_miles = d_ft / 5280.0

#print("The distance in inches is %i inches." % d_inches)
#print("The distance in yards is %.2f yards." % d_yards)
#print("The distance in miles is %.2f miles." % d_miles)


##############################################################################################################################
'''62. Write a Python program to convert all units of time into seconds. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySecConv():
    days = int(input("Enter days: ")) *3600*24
    hours = int(input("Enter hours: ")) *3600
    minutes = int(input("Enter minute: ")) * 60
    seconds = int(input("Enter seconds: "))
    times = days + hours + minutes + seconds
    return "Total time in seconds {}".format(times)

#print(pySecConv())

##############################################################################################################################
'''63. Write a Python program to get an absolute file path.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyAbsPath():
    from os.path import abspath
    return (abspath('a.py'))
    #//https://stackoverflow.com/questions/37863476/why-would-one-use-both-os-path-abspath-and-os-path-realpath//

#print(pyAbsPath())

##############################################################################################################################
'''64. Write a Python program to get file creation and modification date/times.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyFileCreateTime():
    import os, time
    print("File creation time: %s" % time.ctime(os.path.getctime('a.py')))
    print("file modification time: %s" % time.ctime(os.path.getmtime('a.py')))
    #//https://www.tutorialspoint.com/python/time_ctime.htm//
    #//ctime() converts a epoch time to a string representing local time//

#print(pyFileCreateTime())
    
##############################################################################################################################
'''65. Write a Python program to convert seconds to day, hour, minutes and seconds.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySecToDay(sec):
    #//1 day = 24 hrs =  1440 min = 86400 sec//
    days = sec // 86400 #//86400 sec = 1day//
    sec = sec % 86400
    hrs = sec // 3600   #//3600 sec = 1 hrs//
    sec = sec % 3600
    mins = sec // 60    #//60 sec = 1 min//
    sec = sec % 60
    #print("out put: %d:%d:%d:%d" % (days, hrs, mins, sec))
    return "Output: %d days %d hrs %d min %d sec" % (days, hrs, mins, sec)

#print (pySecToDay(1234565))

##############################################################################################################################
'''66. Write a Python program to calculate body mass index.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyBMI(w, h):
    BMI = round(float(w)/float(h*h),2)
    return "Your body mass index is: {}".format(BMI)

#print (pyBMI(85, 5.8))

##############################################################################################################################
'''67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg)
and atmosphere pressure.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyKpa(kpa):
    psi = float(kpa)/6.89476        #//1 psi = 6.89476 kilopascal//
    mmHg = float(kpa)/0.133322      #//1 mmhg = 0.133322 kilopascal//
    atm = float(kpa)/101.325        #//1 atm =  101.325 kilopascal//

    print ("%.2f kpa = %.2f psi" %(kpa, psi))
    print ("%.2f kpa = %.2f mmHg" %(kpa, mmHg))
    print ("%.2f kpa = %.2f atm" %(kpa, atm))

#print (pyKpa(12.35))   

##############################################################################################################################
'''68. Write a Python program to calculate the sum of the digits in an integer.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySumInt(string):
    sum = 0
    for digit in string:
        sum = sum + int(digit)
    return sum
        
#print (pySumInt('22222'))

##############################################################################################################################
'''69. Write a Python program to sort three integers without using conditional statements and loops. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySort(x, y, z):
    tuple1 = (x,y,z)
    middle = sum(tuple1) - (max(tuple1)+min(tuple1))
    print ("Sorted order is: ",max(tuple1),middle,min(tuple1))

#print (pySort(1,7,3))
    
##############################################################################################################################
'''70. Write a Python program to sort files by date. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import glob,os
def pySortFiles():                                      #//https://www.geeksforgeeks.org/python-list-sort//
    files = glob.glob('*.py')                           #//glob.glob() module generates lists of files matching given patterns//
    files.sort(key=os.path.getmtime, reverse=False)     #//list_name.sort(key=…, reverse=…)//
    print("File Type before .join(): ",type(files))     #//.join() will convert from list to string//
    files = "\n".join(files)            
    print("Files are:\n%s\nFile type after .join(): %s"%(files, type(files)))
    
#print(pySortFiles())

##############################################################################################################################
'''71. Write a Python program to get a directory listing, sorted by creation date.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

def pyDirSortByDate():
    #Relative or absolute path to the directory
    dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

    #all entries in the directory w/ stats
    data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))

    data = ((os.stat(path), path) for path in data)

    # regular files, insert creation date
    data = ((stat[ST_CTIME], path)
               for stat, path in data if S_ISREG(stat[ST_MODE]))

    for cdate, path in sorted(data):
        print(time.ctime(cdate), os.path.basename(path))

#print (pyDirSortByDate())

##############################################################################################################################
'''72. Write a Python program to get the details of math module.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import math

def pyMathModule(mod):
    mod_ls = dir(mod)
    return mod_ls

#print(pyMathModule(math))

##############################################################################################################################
'''73. Write a Python program to calculate midpoints of a line. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyMidPoint():
    (x1,y1,x2,y2) = (2,4,5,7)
    x_mid_point = (x1+x2)/2
    y_mid_point = (y1+y2)/2
    print("Mid point of x-coordinate: ", x_mid_point)
    print("Mid point of y-coordinate: ", y_mid_point)

#print(pyMidPoint())

##############################################################################################################################
'''74. Write a Python program to hash a word.
    The ord() function in Python accepts a string of length 1 as an argument and returns the unicode code point representation
    #of the passed argument. For example ord('B') returns 66 which is a unicode code point value of character 'B'.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyHashAword():
    soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
     
    word=input("Input the word be hashed: ")
     
    word=word.upper()
    print(word)
     
    coded=word[0]
     
    for a in word[1:len(word)]:
        i=65-ord(a)
        print(i)
        coded=coded+str(soundex[i]) 
    print("The coded word is: "+coded)

##############################################################################################################################
'''75. Write a Python program to get the copyright information.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import sys
def pyCopyright():
    print("\nPython Copyright Information")
    print(sys.copyright)

#print(pyCopyright())

##############################################################################################################################
'''76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments)
passed to a script. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyScriptName():
    print('Name of the script',sys.argv[0])
    print("Number of arguments:",len(sys.argv))
    print("Argument List:",str(sys.argv))
    
#print(pyScriptName())

##############################################################################################################################
'''77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyPlatform():
    if sys.byteorder == "little":
        return "Little-endian platform."    #//intel, alpha//
    else:
        return "Big-endian platform."       #//motorola, sparc//
    
#print(pyPlatform())

##############################################################################################################################
'''78. Write a Python program to find the available built-in modules. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyBuiltInModule():
    import sys
    import textwrap
    module_name = ', '.join(sorted(sys.builtin_module_names))
    return textwrap.fill(module_name, width=70)
    
#print (pyBuiltInModule())

##############################################################################################################################
'''79. Write a Python program to get the size of an object in bytes. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySizeInByte(x):
    return "{} byte".format(sys.getsizeof(x))

#print(pySizeInByte("123456789"))
#print(pySizeInByte("ascnfahd"))

##############################################################################################################################
'''80. Write a Python program to get the current value of the recursion limit. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyRecursionLimit():
    return "Current value of the recursion limit: {}".format(sys.getrecursionlimit())

#print(pyRecursionLimit())

##############################################################################################################################
'''81. Write a Python program to concatenate N strings.''' 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyConcatenateString():
    l = ["I","am","from","Kodiak"]
    company = " ".join(l)
    return company

#print(pyConcatenateString())

##############################################################################################################################
'''82. Write a Python program to calculate the sum over a container. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pySunOfList():
    l = [10,20,30]  
    s = sum(l)
    return "Sum of the container: {}".format(s)
#print(pySunOfList())

##############################################################################################################################
'''83. Write a Python program to test whether all numbers of a list is greater than a certain number. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyGreaterNum(n):
    l = [1,2,4,7,8,9,12]
    if max(l) < n:
        return True
    return False
#print (pyGreaterNum(100))
#print (pyGreaterNum(200))

##############################################################################################################################
'''84. Write a Python program to count the number occurrence of a specific character in a string. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyOccurChar(x):
    s = "jsdajhsasj;lak;akd;ska;dk;ska;dks;"
    return "Number of times '{}' occurs in string: {} ".format(x, s.count(x))

#print(pyOccurChar(';'))

##############################################################################################################################
'''85. Write a Python program to check if a file path is a file or a directory. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyIsDir(p):
    if os.path.isdir(p):
        return "This is a dir"
    elif os.path.isfile(p):
        return "This is a file"
    else:
        return "There is no such file of dir"

#print(pyIsDir("lib"))

##############################################################################################################################
'''86. Write a Python program to get the ASCII value of a character. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyASSCII(ch):
    return "ASCII value of a char '{}' is: {}".format(ch, ord(ch))
    
#print (pyASSCII('@'))
#print (pyASSCII('a'))

##############################################################################################################################
'''87. Write a Python program to get the size of a file.''' 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyFileSize(f):
    file_size = os.path.getsize(f)*0.001
    print ("Size of a file is: %.2f kb" %file_size)
    return "Size of a file is: {} kb".format(file_size)

#print(pyFileSize('pythonBasicPart1.py'))

##############################################################################################################################
'''88. Given variables x=30 and y=20, write a Python program to print t "30+20=50". '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyDoThis(x, y):
    print("%d+%d=%d"%(x,y,x+y))

#print(pyDoThis(y=30, x=20))
    
##############################################################################################################################
'''89. Write a Python program to perform an action if a condition is true. Given a variable name,
if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''90. Write a Python program to create a copy of its own source code. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''91. Write a Python program to swap two variables. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''92. Write a Python program to define a string containing special characters in various forms. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''93. Write a Python program to get the identity of an object. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''94. Write a Python program to convert a byte string to a list of integers. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''95. Write a Python program to check if a string is numeric. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


'''96. Write a Python program to print the current call stack. 


97. Write a Python program to list the special variables used within the language. 


98. Write a Python program to get the system time. 

Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.


99. Write a Python program to clear the screen or terminal. 


100. Write a Python program to get the name of the host on which the routine is running. 


101. Write a Python program to access and print a URL's content to the console. 


102. Write a Python program to get system command output. 


103. Write a Python program to extract the filename from a given path. 


104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process. 
Note: Availability: Unix.


105. Write a Python program to get the users environment. 


106. Write a Python program to divide a path on the extension separator. 


107. Write a Python program to retrieve file properties. 


108. Write a Python program to find path refers to a file or directory when you encounter a path name. 


109. Write a Python program to check if a number is positive, negative or zero. 


110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. 


111. Write a Python program to make file lists from current directory using a wildcard. 


112. Write a Python program to remove the first item from a specified list. 


113. Write a Python program to input a number, if it is not a number generate an error message. 


114. Write a Python program to filter the positive numbers from a list. 


115. Write a Python program to compute the product of a list of integers (without using for loop). 


116. Write a Python program to print Unicode characters. 


117. Write a Python program to prove that two string variables of same value point same memory location. 


118. Write a Python program to create a bytearray from a list. 


119. Write a Python program to display a floating number in specified numbers. 


120. Write a Python program to format a specified string to limit the number of characters to 6. 


121. Write a Python program to determine if variable is defined or not. 


122. Write a Python program to empty a variable without destroying it. 

Sample data: n=20
d = {"x":200}
Expected Output : 0
{}



123. Write a Python program to determine the largest and smallest integers, longs, floats. 


124. Write a Python program to check if multiple variables have the same value. 


125. Write a Python program to sum of all counts in a collections? 


126. Write a Python program to get the actual module object for a given object. 


127. Write a Python program to check if an integer fits in 64 bits. 


128. Write a Python program to check if lowercase letters exist in a string. 


129. Write a Python program to add leading zeroes to a string. 


130. Write a Python program to use double quotes to display strings. 


131. Write a Python program to split a variable length string into variables. 


132. Write a Python program to list home directory without absolute path. 


133. Write a Python program to calculate the time runs (difference between start and current time) of a program. 


134. Write a Python program to input two integers in a single line. 


135. Write a Python program to print a variable without spaces between values. 
Sample value : x =30
Expected output : Value of x is "30"


136. Write a Python program to find files and skip directories of a given directory. 


137. Write a Python program to extract single key-value pair of a dictionary in variables. 


138. Write a Python program to convert true to 1 and false to 0. 


139. Write a Python program to valid a IP address. 


140. Write a Python program to convert an integer to binary keep leading zeros. 
Sample data : 50
Expected output : 00001100, 0000001100


141. Write a python program to convert decimal to hexadecimal. 
Sample decimal number: 30, 4
Expected output: 1e, 04


142. Write a Python program to find the operating system name, platform and platform release date. 
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic


143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system. 


144. Write a Python program to check if variable is of integer or string. 


145. Write a Python program to test if a variable is a list or tuple or a set. 


146. Write a Python program to find the location of Python module sources. 
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic


147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user. 


148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers. 
Note: Do not use built-in functions.


149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. 


150. Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values. 
'''

##############################################################################################################################
'''151. Write a python program to concatenate two given list using insert() method.
(list1, list2)=([1,3,5,7], [2,4,6,8])
out put: [2, 4, 6, 8, 1, 3, 5, 7]'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyInsert():
    (list1, list2)=([1,3,5,7], [2,4,6,8])
    for i in range(len(list2)-1,-1,-1):
            list1.insert(0,list2[i])
    return list1

#print(pyInsert())


##############################################################################################################################
'''152. Write a python function in an optimal way. Will take an integer as input (between 0-456789) & return the total number
of digits the number.
Ex: if I input 2222 it should return 4 '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def count(x):
    if x == 0:
        return 0
    return 1 + count(x//10)
  
#print(count(12222))

##############################################################################################################################
'''153. Write a function to compress a given string using the counts of repeated characters.Ex:'aaBbBccddd' > a2b3c2d3.
If the compressed string did not become smaller than the original string then return the original one. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def count(x):
    lc_x = x.lower()
    dicts = {ch:lc_x.count(ch) for ch in lc_x}
    out = ["" + key + str(value) for key, value in dicts.items()] 
    result = "".join(out)
    if len(x) > len(result):
        return result
    return x
    
#print(count('#avdrfav#drfavdrf#'))
#print(count('abcdef'))

#//////////////////////////Other way to do this//////////////////////////

def pyStrCount(x):
    lst, x = [], x.lower()
    s = set(x)
    if len(s) == len(x):
        return x
    for i in s:
        lst.append(i + str(x.count(i)))
    return ''.join(lst)

#print(pyStrCount("AbcD*"))
#print(pyStrCount("A**aabb*BCDccdd"))

#//////////////////////////Other way to do this//////////////////////////

def strCount(x):
    lc = x.lower()
    s = set([ch for ch in lc])
    if len(s) != len(x):
        for ch in s:
            count = lc.count(ch)
            print ("%c%d"%(ch,count),end="")
        return "\n"
    else:
        return x

#print(strCount("AbcD*"))
#print(strCount("A**aabb*BCDccdd"))

#//////////////////////////Other way to do this//////////////////////////

def fstrComp_1(stng):
    sRes = ""
    cont = 1        
    for i in range(len(stng)):
        
        if not stng[i] in sRes:
            stng = stng.lower()
            n = stng.count(stng[i])
            if  n > 1: 
                cont = n
                sRes += stng[i] + str(cont)
            else:
                sRes += stng[i]
      
    print(sRes)
    
#fstrComp_1("aaabdH")


##############################################################################################################################
'''154. Write a function to compress a given string is Palindrome or not'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def pyPalindrome1(str):
  hf = int(len(str)/2)
  for i in range(0,hf):
    if str[i] != str[len(str)-(i+1)]:
      return "Not Palindrome"
  return "Palindrome"
      
#print(pyPalindrome1('acbbaabca'))
#print(pyPalindrome1('acbb1bbca'))

#////////////////Other way to write code for this////////////////

def pyPalindrome2(x):
  rev = "".join(reversed(x))
  if x != rev:
    return False
  return True
 
#print(pyPalindrome2("aba"))
#print(pyPalindrome2("babbbba"))

#////////////////Other way to write code for this////////////////

def pyPalindrome(x):
  r = ""
  for i in x:
    r = i + r
  if r != x: return "Not Palindrome"
  return "Palindrome"

#print(pyPalindrome("aba"))
#print(pyPalindrome("babbbba"))

##############################################################################################################################
'''155. Write a function where input and output as below
input = [1,1,0,0,1,3,5,0,0,0,5]
output = [[1, 1], [1, 3, 5], [5]]'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def f2DimensionLst(numLst):
    lst = [[]]
    for i in numLst :
        if i:         
            lst[-1].append(i)
        elif not i and lst[-1]:
            lst.append([])
            
    if not lst[-1]:
        lst.pop()
                    
    print(lst)
    
#f2DimensionLst([1,0,0,0,1,3,5,0,0,0,5])

#////////////////Other way to write code for this////////////////

def nonZeroList3(input):
  l, out = [], []
  #print(len(input))
  for i in range(len(input)):
    #print(i)
    if input[i] != 0:
      l.append(input[i])
      if i == len(input)-1:
        out.append(l)
    else:
      if l != []:
        out.append(l.copy())
        l.clear()
  return out

#print(nonZeroList3([1,1,0,0,1,3,5,0,0,0,5]))

#////////////////Other way to write code for this////////////////

def nonZeroList1(x):
  l, out = [], []
  for i in x:
    if i != 0:
      l.append(str(i))
      flag = 0
    elif i == 0 and flag != 1:
      out.append(l)
      flag = 1
      l = []
  print(out + l)
#print(nonZeroList1([1,1,0,0,1,3,5,0,0,0,5]))

#////////////////Other way to write code for this////////////////

def nonZeroList2(input):
  l, out = [], []
  for i in input:
    if i != 0:
      l.append(i)
    else:
      if l != []:
        out.append(l.copy())
        l.clear()
  return out

#print(nonZeroList2([1,1,0,0,1,3,5,0,0,0,5]))

##############################################################################################################################
'''156. Write python script take user input of feature bit and check if the bit position is Enabled or Disabled'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def FeatureBit():
    a = input("Enter Feature Bits: ")        #Enter feature bits: 0011100111111111100011001000001001100000000111011
    x = int(input("enter Bit position: "))   #Enter Bit position. e.g. 3
    a = a[::-1]
    for i in range(len(a)):
        if i == x:
            if int(a[i])==1:
                print(a[i]+" Enabled")
            else:
                print(a[i]+" Disabled")

#print(FeatureBit())

##############################################################################################################################
'''157. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''158. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''159. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''160. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''161. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''162. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#


##############################################################################################################################
'''163. '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
