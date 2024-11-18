# Generator expression

nums=[1,2,3,4,5,6,7,8,9,26743]
# def gen_func(nums):
#     for n in nums:
#         yield n*n
# another way

        
my_gen=(n*n for n in nums)
    
for i in my_gen:
    print (i)