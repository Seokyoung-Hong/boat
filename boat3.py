from random import *

global time

# boat = [0,0,0,0,0,0]
time = [1,2,7,9]
counting = 10000
progress = []
ending = []
x=0
c=0
ending_count = 0
progress_count = 0


while len(progress) !=108:
    boat = [0,0,0,0,0,0]
    pro = []
    while x==0:
        a=randint(0,3)
        b=randint(0,3)

        if a!=b and boat[a] == boat[4] and boat[b] == boat[4]:
            # print('a = %d' % a)
            # print('b = %d' % b)
            # print('boat[4] = %d' % boat[4])
            boat[4] = (boat[4]-1)*(-1)
            boat[a] = boat[4]
            # print("time[a],time[b] = %d %d" %(time[a],time[b]))

            if boat[b] == 0:
                boat[b] = boat[4]

                if a>b:                    
                    boat[5] += time[a]
                else :
                    boat[5] += time[b]
                
                pro.append(time[a]+time[b])
            
            else :
                boat[5] += time[a]
                pro.append(time[a])
            # print(boat[5])
            # pro.append(boat[5])
            
            # print("boat[a],boat[b] = %d %d" %(boat[a],boat[b]))
            # print('pro =',pro)

        else :
            continue
        y=0
        for i in range(4):
            if boat[i] != 1:
                y+=1
        if y==0:
            if boat[5] not in ending:
                ending.append(boat[5])
            # ending.sort()
            # print(ending)
            break
    if pro not in progress :
        progress.append(pro)
    # print('progress = ',progress)
    k = ending_count
    j = progress_count
    ending_count = len(ending)
    progress_count = len(progress)
    if(k!=ending_count):
        print("count ending_%d" % ending_count )
        
    if(j!=progress_count):
        print("count progress_%d" % progress_count )
ending.sort()
print(ending)

        
