def hello_fun():
    print("hello function")
    
hello_fun()
##execution
def hello_fun():
    return "hello function"
print(hello_fun())
print(len('gnfhh'))

##greeting argument
def hello_fun(greeting):
    return '{} function.'.format(greeting)
print(hello_fun('hi'))
##
def hello_fun(greeting,name="amit"):
    return '{},{}'.format(greeting,name) 
print(hello_fun('hi'))
 #print(hello_fun("hi",name="amit"))
def student_info(*greet,**name):
    print(greet)
    print(name)
student_info('math','arts',name='amit',age=22)

#
def student_info(*greet,**name):
    print(greet)
    print(name)
courses=['math','art']
info={'name':'amit','age':22}
student_info(courses,info)
#as we see the output
def student_info(*greet,**name):
    print(greet)
    print(name)
courses=['math','art']
info={'name':'amit','age':22}
student_info(*courses,**info)
