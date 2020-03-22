def covid19(r,d):
    # r = infaction ratio, d = total days
    p=1
    d1 = 0
    while d1 < d:
        p = p+p*r
        d1 += 5
        print(d1)
        print(p)
  
    
    
print(covid19(0.625,30))


###################################################################################
'''
def play(psn,flag):
    snake_begin=-1
    snake_end=-1
    while(snake_begin<=snake_end):
        snake_begin=random.randint(1,99)
        snake_end=random.randint(1,99)
    print("Snake from", snake_begin, "to",snake_end)
    r = random.randint(1,6)
    print("Dice rolled: ",r)
    if psn ==0:
        if r==1 or r==6:
            psn=1
    else:
        psn=psn+r
    print("Position=",psn)
    #input()
    if psn==snake_begin and flag==0:
        print("Bitten by snake")
        psn=snake_end
        flag=1
    if psn>=100:
        print("you won")
        return
    play(psn,flag)

position=0
play(position,0)
'''
