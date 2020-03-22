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
print(next_pernutation(a))            
'''

# Function to compute the previous permutation 
def prevPermutation(str): 
      
    # Find index of the last element 
    # of the string 
    n = len(str) - 1
  
    # Find largest index i such that  
    # str[i ? 1] > str[i] 
    i = n 
    while (i > 0 and str[i - 1] <= str[i]): 
        i -= 1
  
    # if string is sorted in ascending order 
    # we're at the last permutation 
    if (i <= 0): 
        return False
  
    # Note - str[i..n] is sorted in  
    # ascending order 
  
    # Find rightmost element's index  
    # that is less than str[i - 1] 
    j = i - 1
    while (j + 1 <= n and 
           str[j + 1] <= str[i - 1]): 
        j += 1
  
    # Swap character at i-1 with j 
    str = list(str) 
    temp = str[i - 1] 
    str[i - 1] = str[j] 
    str[j] = temp 
    str = ''.join(str) 
  
    # Reverse the substring [i..n] 
    str[::-1] 
      
    return True, str

print(prevPermutation(["a","b","c","d"]))
