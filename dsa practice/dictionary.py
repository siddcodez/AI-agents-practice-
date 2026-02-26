# DICTIONARY FUNCTIONS

d = {"a": 1, "b": 2}

# Add / Update
d["c"] = 3
d.update({"d": 4})

# Access
print(d.get("a"))
print(d.keys())
print(d.values())
print(d.items())

# Remove
d.pop("b")
# d.clear()

print("Final Dict:", d)