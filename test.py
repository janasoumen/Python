def factorial(n):
    if n >= 1:
        return (n * factorial(n-1))

print(factorial(4))

'''
num = input("Enter a number: ")
def recur_factorial(n):
    if n == 1:
       return n
    elif n < 1:
       return ("NA")
    else:
       return n*recur_factorial(n-1)
print (recur_factorial(int(num)))
'''

'''
a = input("Enter Feature Bits: ")     #Enter feature bits: 001000001001100000000111011
b = bin(int(a, 16))
print(b)
x = int(input("enter Bit position: "))   #Enter Bit position. e.g. 3
a = a[::-1]
for i in range(len(a)):
    if i == x:
        if int(a[i])==1:
            print(a[i]+" Enabled")
        else:
            print(a[i]+" Disabled")
    
'''




