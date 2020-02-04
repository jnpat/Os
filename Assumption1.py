import random
import matplotlib.pyplot as plt


def random1(n,a,b,c):
    process = []
    process1 = []
    process2 = []
    process3 = []
    i = int(a*n)
    j = int(b*n)+i
    for x in range(n):
        if x<i:
            process1.append((x,random.randint(2,8)))
        elif x<j and x>i:
            process2.append((x,random.randint(20,30)))
        else :
            process3.append((x,random.randint(35,40)))
    
    process = process1 + process2 + process3
    
    FCFS(process)
    RR(process)
    SJF(process)

  
def FCFS(p):
    # turn = []
    wait = [(0,0)]
    n = len(p)
    time = 0
    for x in range(n):
        if x == 0:
            time += p[x][1]
            # turn.append((p[x][0],p[x][1]))
            wait.append((p[x][0]+1,time))
        else:
            time += p[x][1]
            # turn.append((p[x][0],time))
            wait.append((p[x][0]+1,time))
    wait.pop()
    print("First Come First Served (FCFS) \n")
    # print("Turn Around Time : " + str(turn) + "\n")
    print("Waiting Time : " + str(wait) + "\n")
    

def SJF(p):
    turn = []
    n = len(p)
    time = 0
    p.sort(key = lambda x: x[1])
    print(str(p)+"\n")
    for x in range(n):
        if x == 0:
            time += p[x][1]
            turn.append((p[x][0],p[x][1])) 
        else:
            time += p[x][1]
            turn.append((p[x][0],time))
    print(turn)
    # print("Shortest-Job-First(SJF) : " + str(p) + "\n")
    

def RR(p):
    qT = 5
    n = len(p)
    L = p[n-1][1]
    L = L/qT+1
    processRR = []
    for y in range(L):
        for x in range(n):
            if (p[x][1]-1)/qT==y:
                processRR.append(p[x])               
    # print("Round Robin (RR) : " + str(processRR) + "\n")
    
# main
print("----- Assumption1 -----\n")
random1(60,0.7,0.2,0.1)
# print("----- Assumption2 -----\n")
# random1(40,0.5,0.3,0.2)
# print("----- Assumption3 -----\n")
# random1(20,0.4,0.4,0.2)