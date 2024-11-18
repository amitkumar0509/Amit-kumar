import sys
a="amit@123"
print(sys.getsizeof(a))
b = bytes(a, 'utf-8')
print(sys.getsizeof(b))

