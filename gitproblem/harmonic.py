n = int(input("Value of n :"))
total = 0.0
for i in range(1,n +1):
    total +=1/i
print("Sum of series is ",total)
#Alternate method 
result = sum(1/i for i in range (1,n+1))
print(f"sum is {result:.8f}")

    