with open ("f.txt","w") as myfile:
    myfile.write("0110");
myfile.close()

with open ("f.txt","r") as myfile:
    l=list(myfile.read())
    sum1 = 0
    for i in l:
        sum1 += int(i)
    print(sum1)
myfile.close()
        
        
        
