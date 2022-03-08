global time


time = [1,2,7,9]

boat = 0
min = 987654321
count=0



def go(a,b):
    placeb.append(time[a])
    placea.pop(placea.index(time[a]))
    placeb.append(time[b])
    placea.pop(placea.index(time[b]))
    placea.sort()
    placeb.sort()

def back(a):
    placea.append(time[a])
    placeb.pop(placeb.index(time[a]))
    placea.sort()
    placeb.sort()

def listcopy(a):
    next = []
    for i in range(len(a)):
        next.append(a[i])
    next.append(5)
    return next



for i in range(0,4):
    for j in range(i+1,4):
        placea = [1,2,7,9]
        placeb = []
        st = 0
        if time[i] in placea and time[j] in placea:
            go(i,j)
            st += time[j]
            for k in range(0,4):
                if time[k] in placeb :
                    back(k)
                    st += time[k]
                    for l in range(0,4):
                        for m in range(l+1,4):
                            if time[l] in placea and time[m] in placea:
                                go(l,m)
                                st += time[m]
                                for o in range(0,4):
                                    if time[o] in placeb:
                                        back(o)
                                        st += time[o]
                                        for p in range(0,4):
                                            for q in range(p+1,4):
                                                if time[p] in placea and time[q] in placea:
                                                    go(p,q)
                                                    st += time[q]
                                                    print(time[i],time[j],time[k],time[l],time[m],time[o],time[p],time[q])
                                                    count+=1
                                                    if st < min:
                                                        min =st
                                                        print(st)
print(count)                                        






# for i in range(0,4):
#     placeb.append(time[i])
#     placea.pop(placea.index(time[i]))
#     print(placea)
#     print(placeb)
