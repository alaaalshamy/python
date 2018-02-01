class a:
    def __init__(self):
        print("constarctor A")
    def say(self):
        print("say A")


class b:
    def __init__(self):
        print("constarctor B")

    def say(self):
        print("say B")


# class c(a,b):
#     a.__init__()
#     b.__init__()
#
# onobj=c()
# onobj.say()
class human:
    def __init__(self,age):
       self.__age=age
        #self.__age=self.age(age) # you can't call the function age

    @property
    def age(self):
        return  self.__age

    @age.setter
    def age(self,age):
        if age>0:
            self.__age=age
        if age <=0:
            self.__age=0

man=human(-23) # if you
print(man.age)
man.age=-25
print(man.age)


#functional programming
def sum(n):
    return  lambda x:x+n

print(sum(4)) #you have to call it with two values

print(sum(5)(4))

############3
#iterator
l={"js","python","java"}

it=iter(l)
print(next(it))
print(next(it))
print(next(it))
#next(it)
###########################3
#yield
def non():
    for i in range(5):
        return  i

print(non())

def gen():
    for i in range(5):
        yield i
g=gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
#############
print("###################")
#map
it= map(lambda x:x+4,[1,4,7])#return list
print(type(it))
for i in it:
    print(i)
########################
print("###################")
#filter
it=filter(lambda x:x%5==0,[-15,-8,1,4,7])
print(type(it))
for i in it:
    print(i)
