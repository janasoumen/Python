import re
file = open("featureSet.txt")

#feature = re.compile(r"(\w)*")
bit = re.compile(r'((\d){1,2})-((\w)*)')


for line in file:
    #mo1 = feature.search(line)
    mo2 = bit.search(line)
    print(mo2.group(0))
    
    #bit = re.compile(r'\d\d')
    #print(bit)

