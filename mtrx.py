import sys
sys.setrecursionlimit(10000)
def lexicographic(l):
    #Find the largest x such that P[x]<P[x+1].
    pos = len(l)-2
    for i in range(len(l)):
        if l[pos] > l[pos+1]:
            pos -= 1
    #return pos
    #(If there is no such x, P is the last permutation.)
    #Find the largest y such that P[x]<P[y].
    #Swap P[x] and P[y].
    for j in range(pos, len(l)):
        if l[j] > l[pos+1]:
            l[j],l[pos+1] = l[pos+1], l[j]
            break
    #Reverse P[x+1 .. n].
    l[pos+1:]=reversed(l[pos+1:])

    s = "".join(l)
    print(s)
    return lexicographic(l)


        
#print(lexicographic(["f","j","a","d","b","i","h","g","e","c"]))
print(lexicographic(["a","b","c","d","e","f","g","h","i","j"]))


