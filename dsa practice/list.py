# LIST ALL FUNCTIONS

arr = [1, 2, 3, 4]

# Add elements
arr.append(5)          # Add at end
arr.insert(1, 10)      # Insert at index

# Remove elements
arr.pop()              # Remove last
arr.remove(10)         # Remove specific value
# arr.clear()          # Remove all elements

# Searching
print(2 in arr)        # Check existence

# Other functions
print(len(arr))        # Length
print(arr.count(2))    # Count occurrences
arr.sort()             # Sort list
arr.reverse()          # Reverse list

print("Final List:", arr)