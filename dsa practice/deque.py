from collections import deque

dq = deque([1, 2, 3])

# Add
dq.append(4)
dq.appendleft(0)

# Remove
dq.pop()
dq.popleft()

# Other
dq.extend([5, 6])
dq.rotate(1)

print("Final Deque:", dq)