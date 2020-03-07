
def isPrime(n):
   flg = 0
   for i in range(2,n-1):
      if n%i == 0:
         return 0
   return 1
#print(isPrime(n))

def nextPrime(n):
   n += 1
   while True:
      if not isPrime(n):
         n += 1
      else:
         return n
   
#print(nextPrime(n))

val = int(input("Enter a integar number: "))
def isSemiPrime(val):
   for i in range(2, val):
      if isPrime(i):
         if i*nextPrime(i) == val:
            return True
   else:
      return False

print(semiPrime(val))
