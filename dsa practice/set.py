# SET FUNCTIONS

s = {1, 2, 3}

# Add
s.add(4)
s.update([5, 6])

# Remove
s.remove(2)        # Error if not present
s.discard(10)      # No error
s.pop()            # Remove random element

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("Final Set:", s)