import Queue 

def FIFO(refString,check,q1):
    pf = 0
    hit = 0
    for i in range(len(refString)):
        check = [0]*3
        if q1.qsize()<3:
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

    print("Page hit: " + str(hit) + "\n" + "Page fault: " + str(pf))

def Optimal(refString):
    stack = []
    pf = 0
    dis = []
    hit = 0
    for i in range(len(refString)):
        dis = []
        check = 0
        if len(stack) < 3 :
            stack.append(refString[i])
            pf += 1 
        else:
            if refString[i] not in stack:
                for j in range(len(stack)):
                    dis.append((j,finddistance(stack[j],refString[i:])))
                dis.sort(key = sortSecond, reverse=True)
                for k in range(len(dis)):
                    if dis[k][1] == None:
                        dis.sort(key = sortSecond)
                print(dis)
                print(stack)
                stack.pop(dis[0][0])
                stack.insert(dis[0][0],refString[i])
                print(stack)
                pf +=1
                
            else:
                hit += 1
    print(pf)
    print(hit)

def finddistance(find,l):
    for i in range(len(l)):
        if find == l[i]:
            return i
    
def sortSecond(val): 
    return val[1]   

#--------------- main
refString = [1,2,3,4,1,2,5,1,2,3,4,5]
refString1 = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
ref = [1,2,3,2,1,5,2,1,6,2,5,6,3,1,3,6,1,2,4,3]
#---------------FIFO
check=[0]*3
q1 = Queue.Queue(3)
FIFO(refString1,check,q1)
#----------------optimal
Optimal(ref)
Optimal(refString1)

