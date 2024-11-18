class car:
    def __init__(self,name,engine,colour,height):
        self.name = name
        self.engine = engine
        self.colour=colour
        self.height=height

c1=car("mercedes",6,"blue","20feet")
print(c1.name)