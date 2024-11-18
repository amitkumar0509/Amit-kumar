nums=[1,2,3,4,5,6,7,8,10]
# my_list=[]
# for n in nums:
#      if n%2==0:
#       my_list.append(n)
# print(my_list)

# my_list=[]
# for letter in 'abcd':
#     for nums in range(4):
#         my_list.append((letter,nums))
# print(my_list)
my_list=[(letter,nums) for letter in 'abcd' for nums in range(4)]
print(my_list)
    
    