import queue

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

    print(str(hit) + "\n" + str(pf))



#--------------- main
refString = [1,2,3,4,1,2,5,1,2,3,4,5]
check=[0]*3
q1 = queue.Queue(3)
FIFO(refString,check,q1)
