time = [1,2,7,9]

def move(b,t,c):
    x=0
    for i in range(4):
        if b[i] == 0:
            x+=1
    if(x==0):
        print(b[5])
        if t>b[5]:
            t=b[5]
        print(t)
        boat = [0,0,0,0,0,0]
        
        if(c==271):
            return 0
        c+=1
        move(boat,t,c)


    if(b[4])==0:
        for i in range(4):
            if b[i]==0:
                b[i] = 1
                for j in range(i,4):
                    if b[j]==0:
                        b[j]=1
                        b[5]+=time[j]
                        return(move(b,t,c))
    
    else:
        for i in range(4):
            if b[i] ==1:
                b[i] = 0
                b[4] = 0
                b[5] += time[i]
                return(move(b,t,c))


boat = [0,0,0,0,0,0]
minute = 987654
count=0
move(boat, minute, count)