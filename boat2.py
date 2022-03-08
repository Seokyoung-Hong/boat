global boat
global time

boat = [0,0,0,0,0,0]
time = [1,2,7,9]
def go(boat,t):
    for a in range(4):
        for b in range(a,4):
            if boat[a]==0 and boat[b] ==0:
                boat[a],boat[b],boat[4] = 1,1,1
                boat[5] += time[b]
                
                
                x=0
                for c in range(4):
                    if boat[c] != 1:
                        x=1
                if x==0:
                    if boat[5] < t:
                        t = boat[5]
                    return t
                print(t)
                back(boat,t)

def back(boat,t):
    for i in range(4):
        if boat[i] == 1:
            boat[i] =0
            boat[4] =0
            boat[5] += time[i]
            go(boat,t)




print(go(boat,987654321))
