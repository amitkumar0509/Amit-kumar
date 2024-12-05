n = int(input("enter number:"))
for i in range(1,n+1):
    if i == 1:
        print("*"*i)
    elif i==n:
        print("* "*n)
    else:
        print("*"+" "*(2*i-3)+"*")