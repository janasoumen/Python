#Python Dictionary [ 40 exercises with solution]
#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#https://docs.python.org/3/tutorial/

##############################################################################################################################
'''1. Write a python scripit to print out put as shown from two string 'abc' and 'xyz'
[['ax', 'ay', 'az'], ['bx', 'by', 'bz'], ['cx', 'cy', 'cz']'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
def pyListComp1():
    #print ([x+y for x in 'abc' for y in 'xyz'])       

    l = []
    for i in 'abc':
        m = []
        for j in 'xyz':
            m.append(i+j)
        l.append(m)
    return l

#print (pyListComp1())

##############################################################################################################################
