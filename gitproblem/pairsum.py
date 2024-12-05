"""Finding All Pairs of Elements in an Array that Add Up to a Given Sum
Difficulty: Medium
Topics: Arrays, Hashing
Description: Write a program to find all pairs of elements in an array whose sum equals a specified target.
Example:
Input: array = [1, 2, 3, 4, 5], target = 5
Output: [(1, 4), (2, 3)]
Explanation: Pairs that sum up to 5 are (1, 4) and (2, 3)."""

arr = [1,2,3,4,5]
sum  = int(input("enter sum value :"))
pair = []
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        if arr[i]+arr[j] == sum:
            pair.append((arr[i],arr[j]))
print(pair)