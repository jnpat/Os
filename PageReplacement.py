import queue

q1 = queue.Queue(3)
# q1.put(1)
# q1.put(2)
# q1.put(3)
# print(q1.queue[0])
# if 3==q1:
#     print(10)
# print(q1.qsize())
# print(q1.get())
# q1.put(4)
# print(q1.get())
# print(q1.get())
# print(q1.get())
# for i in range(len(q1)):
#     q1.get()


refString = [1,2,3,4,1,2,5,1,2,3,4,5]
res = []
pf = 0

# def FIFO(refString,frames):
#     for i in range(len(frames)):
#         if 
# print(q1.qsize())   0 
# print(len(refString))  12

for i in range(len(refString)):
    # print(refString[i])
    check=[0,0,0]
    if q1.qsize()<3:
        # print(refString[i])
        q1.put(refString[i])
        pf += 1
    else:
        for j in range(q1.qsize()):
            if refString[i] != q1.queue[j]:
                check[j] = 1 
        #  if refString[i] != q1.queue[0] and refString[i] != q1.queue[1] and refString[i] != q1.queue[2]:
            # print("-")
            # print(q1.queue[0])
            # print(q1.queue[1])
            # print(q1.queue[2])
                # print(q1.get())
        if 0 not in check:
            q1.get()
            res.append(q1.queue)
            q1.put(refString[i])
            pf += 1
            
            
        
print(res)


print(pf)


