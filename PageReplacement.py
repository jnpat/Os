import Queue 

def FIFO(refString,check,q1,frame):
    pf = 0
    hit = 0
    for i in range(len(refString)):
        check = [0]*frame
        if q1.qsize() < frame:
            q1.put(refString[i])
            pf += 1
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

    # print("Page hit: " + str(hit) + "\n" + "Page fault: " + str(pf))
    return pf,hit

def Optimal(refString,frame):
    stack = []
    pf = 0
    dis = []
    hit = 0
    for i in range(len(refString)):
        dis = []
        if len(stack) < frame :
            stack.append(refString[i])
            pf += 1 
        else:
            if refString[i] not in stack:
                for j in range(len(stack)):
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
    # print("Page hit: " + str(hit) + "\n" + "Page fault: " + str(pf))
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
        if len(stack) < frame:
            stack.append(refString[i])
            list1.insert(0,refString[i])
            pf += 1
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
    # print("Page hit: " + str(hit) + "\n" + "Page fault: " + str(pf))
    return pf,hit


#--------------- main
for frame in range(12):
    refString1 = [1,2,3,4,1,2,5,1,2,3,4,5]
    refString2 = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    refString3 = [1,2,3,2,1,5,2,1,6,2,5,6,3,1,3,6,1,2,4,3]
    #---------------FIFO
    frame += 1
    check=[0]*frame
    q1 = Queue.Queue(frame)
    print("Fisrt in first out algotrithm\n(Page faults,Page hit): " + str(FIFO(refString2,check,q1,frame)))
    #----------------optimal
    print("\nOptimal algotrithm\n(Page faults,Page hit): " + str(Optimal(refString2,frame)))
    #---------------LRU
    print("\nLeast Recently used algotrithm\n(Page faults,Page hit): " + str(LRU(refString2,frame)))


