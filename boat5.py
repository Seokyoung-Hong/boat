from tkinter import mainloop


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




placea = [1,2,7,9]
placeb = []



