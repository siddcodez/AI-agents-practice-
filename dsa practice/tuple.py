# TUPLE FUNCTIONS

t = (1, 2, 3, 2)

# Access
print(t[0])

# Built-in functions
print(len(t))          # Length
print(t.count(2))      # Count
print(t.index(3))      # Find index

# agar tuple badalni hai to list me change karke badal skte hai
temp = list(t)
temp.append(5)
t = tuple(temp)

print("Final Tuple:", t)