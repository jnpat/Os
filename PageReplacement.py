import queue 
import matplotlib.pyplot as plt

def FIFO(refString,check,q1,frame):
    pf = 0
    hit = 0
    for i in range(len(refString)):
        check = [0]*frame
        if q1.qsize() < frame and refString[i] not in q1.queue:
            q1.put(refString[i])
            pf += 1
        elif  refString[i] in q1.queue:
            hit +=1
        else:
            for j in range(q1.qsize()):
                if refString[i] != q1.queue[j]:
                    check[j] = 1 
            if 0 not in check:
                q1.get()
                q1.put(refString[i])
                pf += 1
            else:
                hit += 1
    return pf,hit

def Optimal(refString,frame):
    stack = []
    pf = 0
    dis = []
    hit = 0
    for i in range(len(refString)):
        dis = []
        if len(stack) < frame and refString[i] not in stack :
            stack.append(refString[i])
            pf += 1 
        elif refString[i] in stack:
            hit +=1
        else:
            if refString[i] not in stack:
                for j in range(len(stack)):
                    if findDistance(stack[j],refString[i:])==None:
                        dis.append((j,len(refString)+1))
                    else:
                        dis.append((j,findDistance(stack[j],refString[i:])))
                dis.sort(key = lambda x: x[1],reverse=True)
                for k in range(len(dis)):
                    if dis[k][1] == None:
                        dis.sort(key = lambda x: x[1])
                stack.pop(dis[0][0])
                stack.insert(dis[0][0],refString[i])
                pf +=1
                
            else:
                hit += 1
    return pf,hit

def findDistance(find,l):
    for i in range(len(l)):
        if find == l[i]:
            return i
    
def LRU(refString,frame):
    stack = []
    list1 = []
    pf = 0 
    hit = 0
    for i in range(len(refString)):
        dis = []
        if len(stack) < frame and refString[i] not in stack: 
            stack.append(refString[i])
            list1.insert(0,refString[i])
            pf += 1
        elif refString[i] in stack:
            hit += 1
            list1.insert(0,refString[i])
        else:
            if refString[i] not in stack:
                for j in range(len(stack)):
                    dis.append((j,findDistance(stack[j],list1)))
                dis.sort(key = lambda x: x[1],reverse=True)
                for k in range(len(dis)):
                    if dis[k][1] == None:
                        dis.sort(key = lambda x: x[1])
                stack.pop(dis[0][0])
                stack.insert(dis[0][0],refString[i])
                list1.insert(0,refString[i])
                pf +=1
                
            else:
                hit += 1
                list1.insert(0,refString[i])
    return pf,hit

def plotgraph(pf1,pf2,pf3,frame):
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    for x in range(len(frame)):
        x1.append(frame[x])
        y1.append(pf1[x])

        y2.append(pf2[x])

        y3.append(pf3[x])

    plt.plot(x1,y1, label = "FIFO")
    plt.plot(x1,y2, label = "OPTIMAL")
    plt.plot(x1,y3, label = "LRU")

    plt.xlabel('Number of frame')
    plt.ylabel('Number Of Pagefaults')
    plt.title('PageReplacement')
    plt.legend()

    plt.show()    


# --------------- main
refString1 = [1,2,3,4,1,2,5,1,2,3,4,5]
refString2 = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
refString3 = [1,2,3,2,1,5,2,1,6,2,5,6,3,1,3,6,1,2,4,3]
refString4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
refString5 = [1,2,4,1,2,3,1,2,4,1,2,3,1,2,4]
refString6 = [1,5,6,3,5,1,1,5,7,6,5,1,1,5,6,5,6,]
pf_FIFO = []
pf_Optimal = []
pf_LRU = []
f = []
for frame in range(7):
    #---------------FIFO
    frame += 1
    f.append(frame)
    check=[0]*frame
    q1 = queue.Queue(frame)
    pf1 = FIFO(refString6,check,q1,frame)
    pf_FIFO.append(pf1[0]) 
    # #----------------optimal
    pf2 = Optimal(refString6,frame)
    pf_Optimal.append(pf2[0])
    #---------------LRU
    pf3 = LRU(refString6,frame)
    pf_LRU.append(pf3[0])

plotgraph(pf_FIFO,pf_Optimal,pf_LRU,f)
print(pf_FIFO)
print(pf_Optimal)
print(pf_LRU)
print(f)
