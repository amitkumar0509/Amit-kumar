
'''

looplist
'''
course=['phy','histry','math','chem']
for item in course:
 print(item)
 
'''
if you have to join the list in output
'''
course=['phy','histry','math','chem']
course_str='-'.join(course)
print(course_str)

'''
if we have to add number with series we use enumerate()

'''
course=['phy','histry','math','chem']
for index,course in enumerate(course,start=1):
    print(index,course)