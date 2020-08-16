# quick_sort [2,1,4,5,6,3,2,7,8,9,414,52,85,78,63,98,52,14,7,52,1,47,85,21,45,69,]

def quick_sort (a):
     b = len(a) - 1
     for x in range(b):
         for y in range(b-x):
             if a[y] > a[y+1]:

                  a[y],a[y+1] = a[y+1],a[y]

     return True

a = [2,1,4,5,6,3,2,7,8,9,414,52,85,78,63,98,52,14,7,52,1,47,85,21,45,69]

quick_sort(a)
print(a)


# # object programging in python
class Dog:
    def __init__(self,name):
        self.name = name
        print(name)

    def add_one(self,x):
        return x + 1
    def bark(self):
        print("bark")

d = Dog("tim")
d2 = Dog("Bill")
d3 = Dog("laill")
d4 = Dog("yuill")

