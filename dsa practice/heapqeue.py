import heapq

nums = [3, 1, 4, 2]

heapq.heapify(nums)

heapq.heappush(nums, 0)
print("Smallest:", heapq.heappop(nums))

# Largest element
print("Largest:", heapq.nlargest(1, nums))

print("Final Heap:", nums)