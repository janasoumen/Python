import turtle
from random import randint

turtle.bgcolor("black")
seurat = turtle.Turtle()
width = 5
height = 7
dot_distance = 25
seurat.setpos(-250,250)

seurat.penup()
list_color = ["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]

'''
for i in range(5):
    seurat.forward(50)
    seurat.right(144)
turtle.done()
'''
def spiral(r,c):

#def spiral(r,c,mtrx):
#r = End row, c = End column, mtrx = matrix
    r0 = 0     # Starting index of row
    c0 = 0     # Starting index of column
    f = 0

    while r0 < r and c0 < c:
        if f==1:
            seurat.right(90)
  
        col = randint(1,10)
        seurat.color(list_color[col])
        # Printing the first row from the remaining rows
        for i in range(c0, c):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(mtrx[r0][i],end= " ")
        r0 += 1
        f=1
                     
        seurat.right(90)
        col = randint(1,10)
        seurat.color(list_color[col])       
        # Printing the last column from the remaining column
        for i in range(r0,r):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(mtrx[i][c-1], end=" ")
        c -= 1
        
        seurat.right(90)
        col = randint(1,10)
        seurat.color(list_color[col])
        # Printing the last row from remaining rows
        if r0 < r:  
             for i in range(c-1, c0-1, -1):
                 seurat.dot()
                 seurat.forward(dot_distance)
                 #print(mtrx[r-1][i], end=" ")
                 
             r -= 1
                     
        seurat.right(90)
        col = randint(1,10)
        seurat.color(list_color[col])
        if c0 < c:
            # Printing the first column from the remaining column
            for i in range(r-1,r0-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(mtrx[i][c0], end=" ")
            c0 += 1
'''             
mtrx = []
count = 1
for i in range(4):
    l = []
    for j in range(4):
        l.append(count)
        count += 1
    mtrx.append(l)
    #print(l)
#print(mtrx)
'''
spiral(20,20)
turtle.done()
