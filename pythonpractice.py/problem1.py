# n = 10 
# even_sum = 0
# for i in range(1,n+1):
#     if n % 2 == 0:
#        even_sum +=i
# print(even_sum)
# a  = [1,2,3,4,5]
# b= ["a","b"]
# print(zip(a,b))
# a[0].append(b)
# print(a[0])  # Output: [1, 2, 3, 4,

# [["a","b"],1,2,3,4,5]
list = [1,2,3,4,5,["a","b"]] 
# x = []
# for i in range(len(list)):
#     if i==0:
#         x.append(list[-1]) #x = [["a","b"]]
#         continue
# else:
#     x.append(list[0:len(list)-1])  #x = [["a","b"],2]
# print(x)
      
    
print([list[-1]]+list[:len(list)-1])
#[0][1][2][3][4][5]
# list = [1,2,3,4,5]
# for i in list:
#     print(f"[{i}]",end = "")