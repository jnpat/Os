import random
import matplotlib.pyplot as plt



def random1(n,a,b,c):
    process = []
    process1 = []
    process2 = []
    process3 = []
    i = int((a/100)*n)
    j = int((b/100)*n)+i
    for x in range(n):
        if x<i:
            process1.append((x,random.randint(2,8)))
        elif x<j and x>=i:
            process2.append((x,random.randint(20,30)))
        else :
            process3.append((x,random.randint(35,40)))
    
    process = process1 + process2 + process3
    plotgraph(FCFS(process),SJF(process),RR(process)) 
    

  
def FCFS(p):
    wait = [(0,0)]
    time = 0
    for x in range(len(p)):
        if x == 0:
            time += p[x][1]
            wait.append((p[x][0]+1,time))
        else:
            time += p[x][1]
            wait.append((p[x][0]+1,time))
    wait.pop()

    print("First Come First Served (FCFS) \n")
    print("Waiting Time : " + str(wait) + "\n")
    return wait
    

def SJF(p):
    wait = []
    time = 0
    p.sort(key = lambda x: x[1])
    for x in range(len(p)):
        if x == 0:
            wait.append((p[x][0],time)) 
        else:
            time += p[x-1][1]
            wait.append((p[x][0],time))
    print("Shortest-Job-First(SJF) \n")
    print("Waiting Time : " + str(wait) + "\n")
    return wait
    

def RR(p):
    qT = 5
    rem = []
    wait = [0]*len(p)
    time = 0

    for i in range(len(p)):
        rem.append(p[i][1])
   
    while(1):
        done = True 

        for i in range(len(p)):
            if(rem[i] > 0):
                done = False
                if(rem[i] > qT):
                    time += qT
                    rem[i] -= qT
                else:
                    time = time + rem[i]
                    wait[i] = (i , time - p[i][1])
                    rem[i] = 0 

        if(done == True):
          break
    print("Round Robin \n")
    print("Waiting Time : " + str(wait) + "\n")
    return wait

def plotgraph(g1,g2,g3):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    for x in range(len(g1)):
        x1.append(g1[x][1])
        y1.append(g1[x][0])

        x2.append(g2[x][1])
        y2.append(g2[x][0])

        x3.append(g3[x][1])
        y3.append(g3[x][0])

    plt.plot(x1,y1, label = "FCFS")
    plt.plot(x2,y2, label = "SJF")
    plt.plot(x3,y3, label = "RR")

    plt.xlabel('Waiting time(ms)')
    plt.ylabel('Number Of Process')
    plt.title('Assumption')
    plt.legend()

    plt.show()    
    
# main
print("----- Assumption1 -----\n")
random1(60,70,20,10)
print("----- Assumption2 -----\n")
random1(40,50,30,20)
print("----- Assumption3 -----\n")
random1(20,40,40,20)