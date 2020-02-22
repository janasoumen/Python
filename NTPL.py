'''
==============================================================================================================================================================
1. A positive integer m can be expresseed as the sum of three squares if it is of the form p + q + r where p, q, r ≥ 0, and p, q, r are all perfect squares.
For instance, 2 can be written as 0+1+1 but 7 cannot be expressed as the sum of three squares. The first numbers that cannot be expressed as the sum of
three squares are 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, … (see Legendre's three-square theorem).

Write a Python function threesquares(m) that takes an integer m as input and returns True if m can be expressed as the sum of three squares and False
otherwise. (If m is not positive, your function should return False.)

Legendre's three-square theorem:   n=x**2 + y**2 + z**2     e.g. threesquares(1024) >>> True
==============================================================================================================================================================
'''

import math
def threesquares(m):
    limit = int(math.ceil(m**(1/2.0)))
    # n=x**2 + y**2 + z**2

    for x in range(0,limit+1):
        #print("x is: ", x)
        for y in range(x, limit+1):
            #print("y is: ", y)
            for z in range(y, limit+1):
               #print("z is: ", z)
               if m == (x**2 + y**2 + z**2):
                    print("Val of x={}, y={}, z={}".format(x,y,z))
                    return True

            #print("loop completed.....")
                

    return False
      

#print(threesquares(1024))
#print(threesquares(4))
#print(threesquares(143))

###################################### Alternative way to validate ######################################

def factors(n):
    if n == 0:
        return([0])
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist.append(i)
    return(factorlist)

def square(n):
    return(len(factors(n))%2 == 1)

def threesquares(n):
    for i in range(0,n+1):
        for j in range(i,n+1):
            if square(i) and square(j) and square(n-(i+j)):
                return(True)
    return(False)

#print(threesquares(1024))
'''
==============================================================================================================================================================
2. Write a function repfree(s) that takes as input a string s and checks whether any character appears more than once. The function should return True if there
are no repetitions and False otherwise.
repfree("qwerty!@#2") >>> True
==============================================================================================================================================================
'''
def repfree(s):
    #count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[j] == s[i]:
                #print("Value of i",s[i])
                #print("Value of j",s[j])
                #count += 1
                #print(count)
                return False
        return True
               
        
#print(repfree("zb%78"))
#print(repfree("(7)(a"))
#print(repfree("a)*(?"))
#print(repfree("abracadabra"))


'''
==============================================================================================================================================================
3. A list of numbers is said to be a hill if it consists of an ascending sequence followed by a descending sequence, where each of the sequences is of length
at least two. Similarly, a list of numbers is said to be a valley hill if it consists of an descending sequence followed by an ascending sequence.
You can assume that consecutive numbers in the input sequence are always different from each other.

Write a Python function hillvalley(l) that takes a list l of integers and returns True if it is a hill or a valley, and False otherwise.
	
hillvalley([9,5,4,-1,-2,3,7]) >>> True
==============================================================================================================================================================
'''
def descenByAscen(l):
    for i in range(0,len(l)-1):
        if l[i]<l[i+1]:
            pos=i
            break
    else:
        return False
    for j in range(pos,len(l)-1):
        if l[j]>=l[j+1]:
            return False
    return True
    
def ascenByDescen(l):
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            pos=i
            break
    else:
        return False
    for j in range(pos,len(l)-1):
        if l[j]<=l[j+1]:
            return False
    return True
    
def hillvalley(l):
    if len(l) < 2:
        return False
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return False
    if l[0] > l[1]:
        return descenByAscen(l)
    return ascenByDescen(l)


#print(hillvalley([9,5,4,-1,-2,3,7]))
#print(hillvalley([5,4,3,2,1,0,-1,-2,-3]))

###################################### Alternative way to validate ######################################

def ascending(l):
    if len(l) <= 1:
        return(True)
    else:
        return(l[0] < l[1] and ascending(l[1:]))

def descending(l):
    if len(l) <= 1:
        return(True)
    else:
        return(l[0] > l[1] and descending(l[1:]))

def hill(l):
    for i in range(1,len(l)-1):
        if ascending(l[:i+1]) and descending(l[i:]):
            return(True)
    return(False)

def valley(l):
    for i in range(1,len(l)-1):
        if descending(l[:i+1]) and ascending(l[i:]):
            return(True)
    return(False)

def hillvalley(l):
    return(hill(l) or valley(l))

#print(hillvalley([1,2,3,5,4,3,2,1]))
#print(hillvalley([1,2,3,4,5,3,2,4,5,3,2,1]))
'''
==============================================================================================================================================================
4. Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the first occurrence of each
number. For instance: remdup([7,3,-1,-5,3,7]) >>> [7, 3, -1, -5]
==============================================================================================================================================================
'''
def remdup(l):
    lst = []
    for i in range(len(l)):
        if l[i] not in lst:
            lst.append(l[i])
    return lst
        
#print(remdup([7,3,-1,-5]))


###################################### Alternative way to validate ######################################
def remdup1(l):
    for i in range(len(l)):
        for j in m(i+1, len(l)):
            if l[i] == l[j]:
                l.pop(j)
    print(l)


#print(remdup([3,5,7,5,3,7,10]))
#print(remdup([3,1,3,5]))

'''
==============================================================================================================================================================
5. Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd
numbers in l and even is the sum of squares of all the even numbers in l.
sumsquare([1,3,5]) >>> [35, 0]
==============================================================================================================================================================
'''

def sumsquare(l):
    lst, elst, olst = [], [], []
    for i in l:
        if i%2 == 0:
            i = i**2
            elst.append(i)
        else:
            i = i**2
            olst.append(i)
    eTotal, oTotal = sum(elst), sum(olst)
    lst.append(oTotal)
    lst.append(eTotal)
    return lst

#print(sumsquare([1,3,5]))    
#print(sumsquare([2,4,6]))
#print(sumsquare([-1,-2,3,7]))

'''
==============================================================================================================================================================
6. A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix.
For instance, the matrix transpose([[1,2,3],[4,5,6]]) >>> [[1, 4], [2, 5], [3, 6]]
==============================================================================================================================================================
'''
def transpose(m):
    transpose = []
    for column in range(len(m[0])):
        rowcolumn = []
        for row in range(len(m)):
            rowcolumn.append(m[row][column])
        transpose.append(rowcolumn)
    return transpose
                       

#print(transpose([[1,2,3],[4,5,6]]))
#print(transpose([[3],[6]]))
#print(transpose([[3]]))
'''
==============================================================================================================================================================
7. Write a script to read data (011011000110011110) from file and store in list. Get sum of the list
==============================================================================================================================================================
'''
def readFile():
    with open ("f.txt","w") as myfile:
        myfile.write("011011000110011110");
    myfile.close()

    with open ("f.txt","r") as myfile:
        l=list(myfile.read())
        sum1 = 0
        for i in l:
            sum1 += int(i)
        print(sum1)
    myfile.close()

#print(readFile())

'''
==============================================================================================================================================================
8. Which of the following displays a code which iterates from numbers 1 to 100, displays “fizz” if the number is divisible by a but not b, displays
“buzz” if the number is divisible by b but not a and displays “fizzbuzz” if the number is divisible by both a and b. a and b are inputs taken from the user.
==============================================================================================================================================================
'''
def Fizzbuzz(a,b):

    for i in range(1,11):
        if i%a == 0:
            if i%b != 0:
                print(i,": Fizz")

        if i%b == 0:
            if i%a != 0:
                print(i, ": Buzz")
            else:
                print(i,": Fizzbuzz")

#print(Fizzbuzz(2,3))

'''
==============================================================================================================================================================
9. Given an array A of N numbers (integers), you have to write a program which prints the sum of the elements of array A with the corresponding elements of the reverse of array A.
If array A has elements [1,2,3], then reverse of the array A will be [3,2,1] and the resultant array should be [4,4,4].

Input Format: The first line of the input contains a number N representing the number of elements in array A.
The second line of the input contains N numbers separated by a space. (after the last elements, there is no space)
Output Format: Print the resultant array elements separated by a space. (no space after the last element)
Input:
4
2 5 3 1
Output: 3 8 8 3
Explanation: Here array A is [2,5,3,1] and reverse of this array is [1,3,5,2] and hence the resultant array is [3,8,8,3]
==============================================================================================================================================================
'''
def sunOfElement():
    n = input("Number of elements: ")
    a = input("Enter numbers separated by a space: ").split()

    l = [(int(i)) for i in a]
    r = l[::-1]

    lst_sum = [l[i]+r[i] for i in range(len(l))]

    out = ""
    flag = 1
    for i in lst_sum:
        out += str(i)
        if flag < len(lst_sum):
            out = out + " "
        flag += 1
    #print(out, end="")
    return out
        
#print(sunOfElement())

###################################### Alternative way to validate ######################################

def sunOfElement1():
    N = int(input("Number of elements: "))
    A = [int(i) for i in input("Enter numbers separated by a space: ").split(" ")]
    B = []
    for i in range(len(A)-1, -1,-1):
        B.append(A[i])
    C = []
    for i in range(len(B)):
        C.append(A[i]+B[i])
    for i in range(len(C)):
        if(i==len(C)-1):
            print(C[i])
        else:
            print(C[i],end=" ")

#print(sunOfElement1())
'''
==============================================================================================================================================================
10. Given a list of numbers (integers), find second maximum and second minimum in this list.
Input Format: The first line contains numbers separated by a space.
Output Format: Print second maximum and second minimum separated by a space
Input: 1 2 3 4 5
Output: 4 2
==============================================================================================================================================================
'''
def SecondMaxMin():
    l = [int(j) for j in input("please enter space separated number: ").split()]
    for start in range(len(l)):
        minpos = start
        for i in range(start, len(l)):
            if l[i] < l[minpos]:
                minpos = i
        l[start], l[minpos] = l[minpos], l[start]
    print(l)
    s_min = int(l[1])
    s_max = int(l[-2])


    #print(s_max, s_min, end="")
    return s_max, s_min
    
#print(SecondMaxMin())

'''
==============================================================================================================================================================
11. Write a script to sort a unsorted list using Selection Sort.
==============================================================================================================================================================
'''
def SelectionSort(l):

    print(l)
    for start in range(len(l)):
        #print("\n###1st........ for loop start value: ",start, l[start])
        minpos = start
        #print("\n####1st for loop minpos value: ",minpos, l[minpos])

        
        for i in range(start, len(l)):
            #print("\n@@@second for loop i: ",i, l[i])
            if l[i] < l[minpos]:
                #print("@@@@%d < %d" %(l[i],l[minpos]))
                minpos = i
                #print("@@@@@minpos = ",l[i])
                
        l[start], l[minpos] = l[minpos], l[start]
        #print("\n$$$$$$$$$",l)

    #print("$$$$$$$$$",l)

#print(SelectionSort([100, 20,110,5,200]))


'''
==============================================================================================================================================================
12. Given a list A of numbers (integers), you have to print those numbers which are not multiples of 5.
Input Format: The first line contains the numbers of list A separated by a space.
Output Format: Print the numbers in a single line separated by a space which are not multiples of 5.
Input: 1 2 3 4 5 6 5
Output: 1 2 3 4 6
Explanation: Here the elements of A are 1,2,3,4,5,6,5 and since 5 is the multiple of 5, after removing them the list becomes 1,2,3,4,6.
==============================================================================================================================================================
'''
def function(l):
    #l = input("Enter numbers separated by a space: ").split()
    #l = [int(i) for i in l]    #Commented as directly passing list in function 

    nl = []
    for j in l:
        if j%5 != 0:
            nl.append(j)

    output, count = "", 1
    for i in nl:
        output += str(i)
        if count<len(nl):
          output += " "
          count += 1
        

    return(output)

#print(function([5,10,20,25,30,3,4]))

###################################### Alternative way to validate ######################################

def function1():
    a = [int(x) for x in input("Enter numbers separated by a space: ").split()]
    b = []
    for i in a:
        if(i%5!=0):
            b.append(i)

    for i in range(len(b)):
        if(i==len(b)-1):
            print(b[i],end="")
        else:
            print(b[i],end=" ")
            
#print(function1())
'''
==============================================================================================================================================================
13. You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 )
only. If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.

Input Format: The first line contains a number made up of 0's and 1's.
Output Format: Print 'YES' or 'NO' accordingly without quotes.
Input: 101
Output: YES
Explanation: If you flip the middle digit from 0 to 1 then all the digits will become same. Hence output is YES.
==============================================================================================================================================================
'''
def assignment1():
    l = [int(i) for i in list(input())]
    for i in range(len(l)):
        if l.count(1) == 1 and l[i] == 1:
            l[i] = 0
            print(l)
            return ("1.YES")
            #break
        if l.count(0) == 1 and l[i] == 0:
            l[i] = 1
            print(l)
            return ("2.YES")
            #break
        if l.count(0) == 0 or l.count(1) == 0:
            print(l)
            return("3.YES")
            #break
        elif l.count(0) > 1 and l.count(1) >1:
            print(l)
            return("NO")
            #break
        
#print(assignment1())   

'''
==============================================================================================================================================================
14. Given an integer number n, you have to print the factorial of this number. To know about factorial please click on this link.
Input Format: A number n.
Output Format: Print the factorial of n.
Input: 4     Output: 24
==============================================================================================================================================================
'''
def factorial():
    n = int(input("Enter number to calculate factorial: "))
    j = 0
    ft = 1
    for i in range(n,-1,-1):
        while j<n:
            ft = ft * (n-j)
            j += 1
    return(ft)
    
print(factorial())
'''
==============================================================================================================================================================
15. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
16. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
17. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
18. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
19. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
20. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
21. 
==============================================================================================================================================================
'''

'''
==============================================================================================================================================================
22. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
23. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
24. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
25. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
26. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
27. 
==============================================================================================================================================================
'''

