character=['sharukh','salman','akshay','govinda']
toplist=['1','2','3','4']
# my_dict={}
# for character,toplist in zip(character,toplist):
#     my_dict[toplist]=character
# print(my_dict)


# other method in simple

my_dict={toplist: character for character,toplist in zip(character,toplist) }
print(my_dict)
#now we