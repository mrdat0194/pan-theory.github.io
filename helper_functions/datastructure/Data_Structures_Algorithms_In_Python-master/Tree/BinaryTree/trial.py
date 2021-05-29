from collections import deque

q= deque()
q.append((20,0))
q.append((15,1))
print(q)
print(q.popleft())
