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

###################################### Alternative way to validate ######################################

def remdup(l):
    return(myremdup(l,[]))

def myremdup(l,s):
    if l == []:
        return([])
    else:
        if l[0] in s:
            return(myremdup(l[1:],s))
        else:
            return([l[0]]+myremdup(l[1:],s+[l[0]]))
        
#print(remdup([3,1,3,5]))

'''
==============================================================================================================================================================
5. Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd
numbers in l and even is the sum of squares of all the even numbers in l.
sumsquare([1,3,5]) >>> [35, 0]
==============================================================================================================================================================
'''

def sumsquare(l):
    lst = []
    elst = []
    olst = []
    for i in l:
        if i%2 == 0:
            i = i**2
            elst.append(i)
        else:
            i = i**2
            olst.append(i)
    eTotal = sum(elst)
    oTotal = sum(olst)
    
    lst.append(oTotal)
    lst.append(eTotal)
    return lst

#print(sumsquare([1,3,5]))    
#print(sumsquare([2,4,6]))

###################################### Alternative way to validate ######################################

def even(n):
    return(n%2 == 0)

def sumsquare(l):
    oddsum = 0
    evensum = 0
    for n in l:
        if even(n):
            evensum += n*n
        else:
            oddsum += n*n
    return([oddsum,evensum])


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

###################################### Alternative way to validate ######################################

def transpose(l):
    outl = []
    for row in l[:1]:
        for i in range(len(row)):
            outl.append([])
    for row in l:
        for i in range(len(row)):
            outl[i].append(row[i])
    return(outl)

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
    #l.sort() #this command sorts the list in ascending order
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

###################################### Alternative way to validate ######################################


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
        if l.count(1) == 1 and l[i] == 1: #if value 1 present in list only one time, replace 1 to 0 and print "Yes"
            l[i] = 0
            print(l)
            return ("1.YES")
            #break
        if l.count(0) == 1 and l[i] == 0: #if value 0 present in list only one time, replace 0 to 1 and print "Yes"
            l[i] = 1
            print(l)
            return ("2.YES")
            #break
        if l.count(0) == 0 or l.count(1) == 0:  #if empty list, print as it is and print "Yes"
            print(l)
            return("3.YES")
            #break
        elif l.count(0) > 1 and l.count(1) >1: #if count of 1 and 0  is more than once then print "No"
            print(l)
            return("NO")
            #break
        
#print(assignment1())

###################################### Alternative way to validate ######################################
def assignment():
    A = input()
    ls = []
    li = str(A)
    for j in li:
        ls.append(int(j))
    count_z = 0
    count_o = 0
    for k in ls:
        if(k==1):
            count_o += 1
        if(k==0):
            count_z += 1

    if((count_o == 1) or (count_z == 1)):
        print("YES")

    else:
        if((count_o == 0) or (count_z == 0)):
            print("NO")
        else:
            print("NO")
#assignment()

'''
==============================================================================================================================================================
14. Given an integer number n, you have to print the factorial of this number. To know about factorial please click on this link.
Input Format: A number n.
Output Format: Print the factorial of n.
Input: 4     Output: 24
==============================================================================================================================================================
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))

def callFactorial(num):
    if num < 0:
        print("Sorry! You have entered a -ve int numbe")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        print("Factorial of {} is {}".format(num,factorial(num)))

#callFactorial(num = int(input("Enter a number: ")))
###################################### Alternative way to validate ######################################

def factorial1():
    n = int(input("Enter number to calculate factorial: "))
    j = 0
    ft = 1
    for i in range(n,-1,-1):
        while j<n:
            ft = ft * (n-j)
            j += 1
    return(ft)
    
#print(factorial1())

###################################### Alternative way to validate ######################################
def factorial2():
    k = int(input("Enter number to calculate factorial: "))
    fac = 1
    for i in range(1,k+1):
        if(k==0):
            break
        fac=fac*i

    print(fac)
#print(factorial2())
    
'''
==============================================================================================================================================================
15. We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:
{'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}

Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not fixed (here they are
'match1', 'match2', 'match3'), nor are the names of the players. A player need not have a score recorded in all matches.
Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. Your function should
return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, and topscore is an integer, the total
score of playername.

The input will be such that there are never any ties for highest total score.
==============================================================================================================================================================
'''
d = {'match1': {'player1': 157, 'player2': 38, 'player3': 10},
     'match2': {'player3': 9, 'player1': 42,'player4': 7000},
     'match3': {'player2': 41, 'player4': 63, 'player3': 910}
     }

def orangecap(d):
    #l = sorted(set(d)) #if key is not a nested key in the dictionary
    l = []  #Here key is a key of dictionary
    for key in d.keys():
        for player in d[key].keys():
            if player not in l:
                l.append(player)
                
    new_dict = {}
    score_sum = 0
    i = 0
    for i in range(len(l)):
        for key in d.keys():
            for player in d[key].keys():
                if player == l[i]:
                    score_sum += d[key][player]
                    new_dict[player]=score_sum
        score_sum = 0
    return (max(new_dict, key=new_dict.get), max(new_dict.values()))

#print(orangecap(d))

###################################### Alternative way to validate ######################################

def orangecap(d):
    total = {}
    for k in d.keys():
        for n in d[k].keys():
            if n in total.keys():
                total[n] = total[n] + d[k][n]
            else:
                total[n] = d[k][n]
                
    maxtotal = -1
    for n in total.keys():
        if total[n] > maxtotal:
            maxname = n
            maxtotal = total[n]

    return(maxname,maxtotal)


d = {"ID1" : {"course":1, "fees": 10, "Duration": 2},
     "ID2" : {"course":1, "fees": 10, 'Duration': 2},
     "ID3" : {"course":1, "fees": 10, 'Duration': 2}
    }

#print(orangecap(d))

'''
==============================================================================================================================================================
16. You are provided with the number of rows (R) and columns (C). Your task is to generate the matrix having R rows and C columns such that all the numbers
are in increasing order starting from 1 in row wise manner.
Input Format: The first line contain two numbers R and C separated by a space.
Output Format: Print the elements of the matrix with each row in a new line and elements of each row are separated by a space.
NOTE: There should not be any space after the last element of each row and no new line after the last row.
Input: 3 3
Output:
1 2 3
4 5 6
7 8 9
Explanation: Starting from the first row, the numbers are present in the increasing order. Since it's a 3X3 matrix, the numbers are from 1 to 9.
==============================================================================================================================================================
'''
def matrix():
    row, col = input("Enter two numbers R and C separated by a space: ").split()
    count = 0
    flag = 0
    for r in range(int(row)):
        for c in range(int(col)):
            count += 1
            if (c==int(col)-1):
                print(count,end="")
            else:
                print(count, end=" ")
                
        if count == (int(row)*int(col)):
            print(end="")
        else:
            print()
#print(matrix())    
###################################### Alternative way to validate ######################################
def matrix1():
    a,b=map(int,input("Enter two numbers R and C separated by a space: ").split())

    count=1
    m = []
    for i in range(1,a+1):
        l = []
        for j in range(1,b+1):
            l.append(count)
            count+=1
        m.append(l)

    for i in range(a):
        for j in range(b):
            if(j==b-1):
                print(m[i][j], end="")
            else:
                print(m[i][j], end=" ")
        if(i!=a-1):
            print()
#matrix()
'''
==============================================================================================================================================================
17. Write a python program to place 10 bins and then throwing 100 balls randomly in these bins
==============================================================================================================================================================
'''
import random
def binsBalls():
    bins={}        #Creare empty dictionary called "bins" 
    for i in range(1,11):
        bins[i]=0  # using this loop append Key and value=0
        
    for i in range(1,101):
        r = random.randint(1,10) #Randomly generate number
        #update privious "bins={...}" value in "r" th position + 1
        bins[r] = bins[r]+1  #Here bins[r] = key and bins[r]+1 = value
        print("r = {} and bins[r] = {}".format(r,bins[r]))
        print(bins)
    return(bins)
#print (binsBalls())

'''
==============================================================================================================================================================
18. Write a python program for bubble sort.
==============================================================================================================================================================
'''
def bubbleSort(l):
    print(l)
    for i in range(len(l)):
        '''
        # By completing this loop we would have got max element on on len(l) position.
        # len(l)-i-1): here using -i because len(l)th elemet is already a max one by end of inner for loop
        # len(l)-i-1): -1 we are using because we are comparing l[j]>l[j+1]. Other wise it will give out of range index
        '''
        for j in range(0, len(l)-i-1):
            '''
            #print(len(l),len(l)-i-1)
            #print(i,j, j+1)
            '''
            if l[j]>l[j+1]:
                '''#print(l[j],l[j+1])'''
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp
            '''#print(l,"\n","*"*20)'''
    return(l)
                               

#print(bubbleSort([9,4,1,6,0,1,-1]))

'''
==============================================================================================================================================================
19. Write a python program for Linear search
==============================================================================================================================================================
'''
import time
def linearSearch(l,x):
    count = 0
    flag = 0
    start_time = time.time()
    for i in l:
        count += 1
        if i == x:
            print("Number found: "+str(i))
            flag = 1
            break
    if flag == 0:
        print("Number not found")
    end_time = time.time()
    print("Total number of iteration: "+str(count))
    print("Total time taken: ",(end_time-start_time))
    
l = []
for i in range(0,100001):
    l.append(i)
#print(linearSearch(l,99999))
    
###################################### Recursive algorithm for linear search an element in a list ######################################
    
import random
def lnrSearch(l,loc,item):
    if loc < 0:
        print("****First If condition****")
        loc = 0
    if l[loc] == item:
        print("****Second If condition****")
        print("Found")
        return
    if loc == len(l)-1:
        print("****Third If condition****")
        print("Not Found")
        return 0
    else:
        print("****Else condition****")
        return lnrSearch(l,loc+1,item)

l = [1,2,3,4,5,6,7,8,9]
#lnrSearch(l,-11,9)

'''
==============================================================================================================================================================
20. Write a python program for Binary search
==============================================================================================================================================================
'''
def binarySearch(l,x):
    count = 0
    flag = 0
    fstpos = 0
    lstpos = len(l)-1
    start_time  = time.time()
    
    while  fstpos <= lstpos and flag == 0:
        count += 1
        midpos = (fstpos+lstpos)//2
        if x == l[midpos]:
            flag == 1
            end_time = time.time()
            print("Number found: "+str(x))
            print("Total number of iteration: "+str(count))
            print("Total time taken: ",(end_time-start_time))
            return
        else:
            if x < l[midpos]:
                lstpos = midpos-1
            else:
                fstpos = midpos+1
    
    return("Number is not present")
            
l = []
for i in range(0,1001):
    l.append(i)
#print(binarySearch(l,899))

'''
==============================================================================================================================================================
21. Arun is working in an office which is N blocks away from his house. He wants to minimize the time it takes him to go from his house to the office.
He can either take the office cab or he can walk to the office. Arun's velocity is V1 m/s when he is walking. The cab moves with velocity V2 m/s but whenever
he calls for the cab, it always starts from the office, covers N blocks, collects Arun and goes back to the office. The cab crosses a total distance of N
meters when going from office to Arun's house and vice versa, whereas Arun covers a distance of 2–√∗N while walking.
Help Arun to find whether he should walk or take a cab to minimize the time.
Input Format: A single line containing three integer numbers N, V1, and V2 separated by a space.
Output Format: Print 'Walk' or 'Cab' accordingly
Constraints: 1<=V1, V2 <=100, 1<=N<=200
Example-1: Input: 5 10 15  Output: Cab
Example-2: Input: 2 10 14  Output: Walk
==============================================================================================================================================================
'''
def cabORwalk():
    import math
    N,V1,V2 = map(int,input().split())
    TV1 = 0
    TV2 = 0
    sqrt = math.sqrt(2)

    if N>=1 and N<=200 and V1>=1 and V2<=100:
        TV1 = (sqrt*N)/V1
        TV2 = (2*N)/V2

    else:
        print("Value out of range")

    if TV1 < TV2:
        print("Walk")
    else:
        print("Cab")
    
#cabORwalk()


'''
==============================================================================================================================================================
22. Given a list A of N distinct integer numbers, you can sort the list by moving an element to the end of the list. Find the minimum number of moves
required to sort the list using this method in ascending order. 
Input Format: The first line of the input contains N distinct integers of list A separated by a space.
Output Format: Print the minimum number of moves required to sort the elements.
Input: 1 3 2 4 5                        Output: 3
Input: 20 3 1 2 6 7 8 21 19 5           Output: 8
Input: 4 1 3 5 6 2 7 9 8                Output: 7
Input: 5 1 3 2 7                        Output: 3
Explanation: In the first move, we move 3 to the end of the list. In the second move, we move 4 to the end of the list, and finally, in the third movement,
we move 5 to the end.
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
23. A semiprime number is an integer which can be expressed as a product of two distinct primes. For example 15 = 3*5 is a semiprime number but 9 = 3*3 is not
Given an integer number N, find whether it can be expressed as a sum of two semi-primes or not (not necessarily distinct).
Input Format: The first line contains an integer N.
Output Format: Print 'Yes' if it is possible to represent N as a sum of two semiprimes 'No' otherwise.
Input: 30  Output: Yes
Input: 123 Output: Yes
Input: 58  Output: No
Input: 158 Output: Yes
Explanation: N = 30 can be expressed as 15+15 where 15 is a semi-prime number (5*3 = 15)
==============================================================================================================================================================
'''
def isPrime(n):
   flg = 0
   for i in range(2,n-1):
      if n%i == 0:
         return False
   return True

def nextPrime(n):
   n += 1
   while True:
      if not isPrime(n):
         n += 1
      else:
         return n

def isSemiPrime(val):
    
    for j in range(2, val//2+1):
        #print("#"*30,j)
        if isPrime(j):
            for k in range(j, val//2+1):
                if val == j*nextPrime(k):
                    #print(">>>This is a SemiPrime number")
                    return True
    #print(">>>NOT a SemiPrime number")
    return False

def distinctPrimes(inp):
    for i in range(0,inp//2+1):
        ans = inp - i
        if isSemiPrime(ans) and isSemiPrime(i):
            print("{}+{}={}".format(ans,i,inp))
            return "Yes"
    else:
        print("{}+{}={}".format(ans,i,inp))
        return "No"    

#inp = int(input("Enter a number to check is Semi Prime: "))
#print(distinctPrimes(inp))

'''
==============================================================================================================================================================
24. The library at the Hogwarts School of Witchcraft and Wizardry has computerized its book issuing process. The relevant information is provided as text
from standard input in three parts: information about books, information about borrowers and information about checkouts. Each part has a specific line format,
described below.

Information about books
Line format: Accession Number~Title

Information about borrowers
Line format: Username~Full Name

Information about checkouts
Line format: Username~Accession Number~Due Date
Note: Due Date is in YYYY-MM-DD format.

You may assume that the data is internally consistent. For every checkout, there is a corresponding username and accession number in the input data, and
no book is simultaneously checked out by two people. 

Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Books. The second section begins
with a line containing Borrowers. The third section begins with a line containing Checkouts. The end of the input is marked by a line containing EndOfInput.

Write a Python program to read the data as described above and print out details about books that have been checked out. Each line should describe to one
currently issued book in the following format:

Due Date~Full Name~Accession Number~Title
Your output should be sorted in increasing order of due date. For books due on the same date, sort in increasing order of full name. If the due date and
full name are both the same, sort based on the accession number, and, finally, the title of the book.

Here is a sample input and its corresponding output.
Sample Input
Books
APM-001~Advanced Potion-Making
GWG-001~Gadding With Ghouls
APM-002~Advanced Potion-Making
DMT-001~Defensive Magical Theory
DMT-003~Defensive Magical Theory
GWG-002~Gadding With Ghouls
DMT-002~Defensive Magical Theory
Borrowers
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Checkouts
SLY2304~DMT-002~2019-03-27
SLY2301~GWG-001~2019-03-27
SLY2308~APM-002~2019-03-14
SLY2303~DMT-001~2019-04-03
SLY2301~GWG-002~2019-04-03
EndOfInput

Sample Output
2019-03-14~Katie Bell~APM-002~Advanced Potion-Making
2019-03-27~Bertram Aubrey~DMT-002~Defensive Magical Theory
2019-03-27~Hannah Abbott~GWG-001~Gadding With Ghouls
2019-04-03~Hannah Abbott~GWG-002~Gadding With Ghouls
2019-04-03~Stewart Ackerley~DMT-001~Defensive Magical Theory

==============================================================================================================================================================
'''
def library():
    # Dictionary to map accession number to title
    books = {}
    # Dictionary to map username to fullname
    borrowers = {}
    # List to store checkout data: accumulate, sort and print
    checkouts = [] 

    # Find the start of Books data
    nextline = input().strip()
    while nextline.find("Books") < 0:
        nextline = input().strip()

    # Read upto start of Borrowers data
    # Skip the line with "Books"
    nextline = input().strip()
    while nextline.find("Borrowers") < 0:
        (accession_number,title) = nextline.split('~')
        books[accession_number] = title
        nextline = input().strip()

    # Read upto Checkout data
    # Skip the line with "Borrowers"
    nextline = input().strip()
    while nextline.find("Checkouts") < 0:
        (username,fullname) = nextline.split('~')
        borrowers[username] = fullname
        nextline = input().strip()

    # Process Checkouts
    # Skip the line with "Checkouts"
    nextline = input().strip()
    while nextline.find("EndOfInput") < 0:
        (username,accession_number,due_date) = nextline.split('~')
        checkoutline = due_date+"~"+borrowers[username]+"~"+accession_number+"~"+books[accession_number]
        checkouts.append(checkoutline)
        nextline = input().strip()

    # Print the output from checkouts
    for checkoutline in sorted(checkouts):
        print(checkoutline)

#library()


'''
==============================================================================================================================================================
25. Write a python code to find next pernutation
==============================================================================================================================================================
'''
import sys
sys.setrecursionlimit(10000)
def next_pernutation(a):
    
    inverse_point = len(a)-2

    while inverse_point>=0 and a[inverse_point]>=a[inverse_point+1]:
            inverse_point -= 1

    if inverse_point < 0:
        return[]

    for i in reversed(range(inverse_point,len(a))):
        if a[i] > a[inverse_point]:
            a[i],a[inverse_point] = a[inverse_point],a[i]
            break
    a[inverse_point+1:] = reversed(a[inverse_point+1:])
    print(a)
    return next_pernutation(a)

#a = [9,1,2,4,3,1,0]
a = ["a","b","c","d"]
#print(next_pernutation(a))   

'''
==============================================================================================================================================================
26. Write a python function spiral(r,c,mtrx) where r=row, c=column and mtrx=list of row*column matrix e.g. 4*4 matrix where row = 4 and column = 4
create below matrix. Out put of the script is given matrix in Spiral Traversing form.
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 14 16

Out put of the python code will be: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
==============================================================================================================================================================
'''
def spiral(r,c,mtrx):     #r = number of row, c = number of column, mtrx = matrix
    
    r0 = 0     # Starting index of row
    c0 = 0     # Starting index of column
    
    while r0 < r and c0 < c:

        # Printing the first row from the remaining rows
        for i in range(c0, c):
            print(mtrx[r0][i],end= " ")
            
        r0 += 1
        # Printing the last column from the remaining column
        for i in range(r0,r):
            print(mtrx[i][c-1], end=" ")

        c -= 1
        # Printing the last row from remaining rows
        if r0 < r:  
             for i in range(c-1, c0-1, -1):
                 print(mtrx[r-1][i], end=" ")
             
        r -= 1
        if c0 < c:
             # Printing the first column from the remaining column
             for i in range(r-1,r0-1,-1):
                 print(mtrx[i][c0], end=" ")
             c0 += 1
     
mtrx = []
count = 1
r = 4; c = 4

for i in range(r):
    l = []
    for j in range(c):
        l.append(count)
        count += 1
    mtrx.append(l)
    #print(l)
#print(mtrx)

#spiral(r,c, mtrx)

'''
==============================================================================================================================================================
27. JOC Assignment 7: Predict the output of the calling function func1() for a given square matrix mx of dimension 70 × 70
==============================================================================================================================================================
'''
import turtle
def func(mx,i):
    n = len(mx)
    tur = turtle.Turtle()
    tur.setpos(i,i)

    for ind in range(i,n-i):
        tur.goto(i,ind)
    for ind in range(i+1,n-i):
        tur.goto(i,n-1-i)
    for ind in range(n-2-i,i,-1):
        tur.goto(n-1-i, ind)       
    for ind in range(n-i-1,i,-1):
        tur.goto(ind,i)



mx = []
count = 1
for i in range(170):
    l = []
    for j in range(170):
        l.append(count)
        count += 1
    mx.append(l)
    #print(l)
#print(mx)


def func1(mx):
    print("#"*20)
    n = len(mx)
    #print(mx)
    i = 0
    while(i<=n-1):
        func(mx,i)
        i=i+10
#func1(mx)


'''
==============================================================================================================================================================
28. Which of the following codes represent a correct version of a board game where the user has to move from block 1 to block 100? The game initialises only
when the user gets a 1 or 6 on the dice and ends once he reaches 100 or gets a number which makes him reach beyond 100 (i.e. the player wins if he is at 99
and gets a 4).
==============================================================================================================================================================
'''
import sys
import random
sys.setrecursionlimit(10000)
def play(psn):
    r = random.randint(1,6)
    print("dice r: ",r)
    if psn == 0:
        print("First IF ###########################")
        if r==1 or r==6:
            print("Nested IF %%%%%%%%%%%%%%%%%%%%%%%%")
            psn = 1
    else:
        print("Else $$$$$$$$$$$$$$$$$$$$$$$$$")
        psn = psn+r
        print("       psn: ",psn)
    print("Position=",psn)
    if psn >= 20:
        print("You won")
        return
    print("Function call: ", psn)
    play(psn)
    
position = 0
#print("Position: ",position)
#play(position)
'''
==============================================================================================================================================================
29. Write a python script for printing "*" as below

             * * * * * * *               

            * * * * * * * * *             

          * * * * * * * * * * *           

        * * * * * * * * * * * * *         

        * * * * * * * * * * * * *         

          * * * * * * * * * * *           

            * * * * * * * * *             

              * * * * * * *  
==============================================================================================================================================================
'''
def func():
    print()
    c=10
    i=3
    while i<=6:
        j=0
        while j<=20:
            if j>=10-i and j<=10+i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j = j+1
        print("\n")
        i = i+1
    i=6
    while i>=3:
        j=0
        while j <=20:
            if j>=10-i and j<=10+i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j=j+1
        print("\n")
        i=i-1
    
#func()

'''
==============================================================================================================================================================
30. Write a python script, A snakes and ladders game with one snake where the snake can change its position during the game and also during any subsequent
plays (a board game where the snakes keep moving). Further, the snake can bite you any number of times.
==============================================================================================================================================================
'''
import random
def play(psn):
    snake_begin=-1
    snake_end=-1
    while(snake_begin<=snake_end):
        snake_begin=random.randint(1,99)
        snake_end=random.randint(1,99)
    print("Snake from", snake_begin, "to",snake_end)
    r = random.randint(1,6)
    print("Dice rolled: ",r)
    if psn ==0:
        if r==1 or r==6:
            psn=1
    else:
        psn=psn+r
    print("Position=",psn)
    print("\n")
    #input()
    if psn==snake_begin:
        print("Bitten by snake")
        psn=snake_end
    if psn>=100:
        print("you won")
        return
    play(psn)

position=0
#play(position)

'''
==============================================================================================================================================================
31. https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/
The preorder traversal of a binary search tree with integer values produces the following sequence: 35, 23, 26, 46, 40, 39, 41, 52. What is the value of the
right child of the root of the tree?
==============================================================================================================================================================
'''



'''
==============================================================================================================================================================
32. Write a python script to find out Longest Common Subsequence (LCS). Refer: https://www.youtube.com/watch?v=sSno9rV8Rhg&t=38s 
==============================================================================================================================================================
'''
############ Longest Common Subsequence (LCS) - Recursion ############ 
def lcs(A,B,i,j):
    if i == len(A) or j == len(B):
        return 0
    elif A[i] == B[j]:
        return 1 + lcs(A,B,i+1,j+1)
    else:
        return max(lcs(A,B,i+1,j),lcs(A,B,i,j+1))


A = "AGGTAB"
B = "GXTXAYB"
print(lcs(A,B,i=0,j=0))

###################################### LCS using Dynamic Programming (Memoization) ######################################



'''
==============================================================================================================================================================
33. With a given list L of integers, write a program to print this list L after removing all duplicate values with original order preserved.
Example: If the input list is 12 24 35 24 88 120 155 88 120 155
Then the output should be 12 24 35 88 120 155
Explanation: Third, seventh and ninth element of the list L has been removed because it was already present.
Input: 12 24 35 24        Output: 12 24 35
==============================================================================================================================================================
'''
def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)   # when item not in set then only append to list
            print(newli)
            print(seen)

    return newli

li=[]
li= list(map(int, input ().split ()))
x = removeDuplicate(li)

for i in x:
    print(i,end=" ")

'''
==============================================================================================================================================================
34. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
35. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
36. 
==============================================================================================================================================================
'''


'''
==============================================================================================================================================================
37. 
==============================================================================================================================================================
'''
