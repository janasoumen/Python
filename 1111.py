def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)
            print(newli)
            print(seen)

    return newli

li=[]
li= list(map(int, input ().split ()))
x = removeDuplicate(li)

for i in x:
    print(i,end=" ")


'''
s = input().lower()
print(type(s))
vow = {"a","e","i","o","u"}

for el in vow:
    for i in range(len(s)):
        if i < len(s)-1:
            if s[i] == s[i+1] and s[i] == el:
                s = s.replace(s[i], '', 1)
print(s)
        
'''
