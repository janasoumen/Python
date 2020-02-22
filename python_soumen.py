def list(l):
    if len(l) < 3 or len(l)==3:
        return l
    elif len(l) == 4:
        return l[1:4]
    elif len(l)>4 and len(l)%2 != 0:
        x = (len(l)-1)/2
        return l[int(x-1):int(x+2)]
    elif len(l)>4 and len(l)%2 == 0:
        x = (len(l)-1)/2
        return l[int(x):int(x+3)]
        


print(list([1,2,2,1,4,1,6,8,9]))


