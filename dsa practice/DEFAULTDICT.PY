from collections import defaultdict

dd = defaultdict(list)

dd["a"].append(1)
dd["a"].append(2)
dd["b"].append(3)

print(dd)

# Int type example
dd2 = defaultdict(int)
dd2["x"] += 1

print(dd2)