k = ["a","b","c","d","e","f","g","h","i","j"]
l = len(k)


for i in range(0,l):
    if k[i-1] < k[i]:
        print("k[i-1] < k[i]", k[i-1],"<",k[i])
        i -= 1
        print(i)

for j in range(0,l):
    print("*"*30)
    print(i)
    if k[i] > k[j]:
        print("k[i] < k[j]", k[i],"<",k[j])
        k[i],k[j] = k[j],k[i]
        print(k)
    print(k)
    
