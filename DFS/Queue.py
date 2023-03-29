# < 연습문제 1> 14p
'''
from collections import deque

def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]

# 적절한 크기 큐 만들어서 붙이고, 꺼내고
queue = [0] * 3
front = -1
rear = -1

rear += 1   # enqueue(1)
queue[rear] = 1

enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
if front != rear:   # 안전장치
    print(dequeue())
# if front != rear:
#     print(dequeue())




q = []
q.append(10)
q.append(20)
q.append(30)
print(q.pop(0))    # 0 넣는 이유 ???
print(q.pop(0))
print(q.pop(0))

q1 = deque()
q1.append(100)
q1.append(200)
q1.append(300)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())

'''

# 선형 큐
'''
size = 10
q = [0] * size
front = rear = -1

def isFull():
    return rear == size - 1

def enqueue(item):
    global rear
    if isFull():
        print('full')
        return
    rear += 1
    q[rear] = item

def isEmpty():
    return front == rear

def dequeue():    # 맨 앞 삭제만 할거니까 파라미터 받을 필요 없음
    global front
    if isEmpty():
        print('empty')
        return
    front += 1
    return q[front]

for i in range(10):
    enqueue(i)

print(q)
print(isEmpty())
print(isFull())
for i in range(10):
    print(dequeue(), end=' ')
print()

print(isEmpty())
print(isFull())
'''
# 원형 큐
'''
size = 10 + 1
cq = [0] * size
front = rear = 0
def isFull():
    return (rear + 1) % size == front

def enqueue(item):
    global rear
    if isFull():
        print('full')
        return
    rear = (rear + 1) % size
    cq[rear] = item

def isEmpty():
    return front == rear

def dequeue():
    global front
    if isEmpty():
        print('empty')
        return
    front = (front + 1) & size
    return cq[front]

for i in range(10):
    enqueue(i)
print(cp)
print(isEmpty())
print(isFull())

enqueue(99)
print(cq)
'''
