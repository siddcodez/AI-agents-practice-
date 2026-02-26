from collections import Counter

c = Counter("aabbccc")

print(c)
print(c["c"])              # Frequency of 'c'
print(c.most_common(1))    # Most common element

# Update
c.update("aa")

print("Updated Counter:", c)