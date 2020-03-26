import matplotlib.pyplot as plt
import random
def play():
    amt=0
    for i in range(0,100):
        r=random.randint(1,6)
        amt=amt+r
    return amt

l=[]
for j in range(0,100):
    s=0
    for i in range(0,100):
        s=s+play()
    l.append(s)
x=[]
y=[]
for each in list(set(l)):
    x.append(each)
    y.append(l.count(each))
plt.plot(x,y,'ro')
plt.show()

        
'''
import random
dict_age = {}
dict_age["A"] = 20
dict_age["B"] = 10
dict_age["C"] = 40
dict_age["D"] = 30


l=list(dict_age.values())
print(l)

dict1={}
l_name=dict_age.keys()
print(l_name)
i=0
prev=0
for each in dict_age:
    print("each",each)
    dict1[each]=prev+l[i]
    prev=dict1[each]
    print(prev,prev)
    i=i+1
print(dict1)

r=random.randint(0,sum(dict_age.values()))
print("Hi",sum(dict_age.values()))
print(r)
for each in dict1:
    print("each",each)
    if r<dict1[each]:
        print("www",dict1[each])
        print("Give all money to", each)
        break
'''
