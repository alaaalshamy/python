


class person:
    def __init__(self,name,money,mood,health):
        self.__name=name
        self.__money=money
        self.__mood=mood
        self.__health=health

    def sleep(self,hours):
       if hours ==7:
           print("happy")
       elif hours>7:
           print("lazy")
       else:
           print("tired")        

    def eat(self,meals):
        if meals ==3:
               print("100% hth")
        elif meals==2:
           print("75%")
        elif meals==1:
           print("50%") 
        else:
            print("you want to eat much")

    def buy(self,items):
        if items==1:
            self.money-=10
            print(self.money)
        else:
            print("try again")
        




class  employee(person):
    def __init__(self,id ,name,money,mood,health, car, email, salary, distanceToWork):
        super(employee,self).__init__(name,money,mood,health)
        print(name,money,mood,health,id , car, email, salary, distanceToWork)
        #  - methods (work, drive, refuel, send_mail)
    def work(self):
        print("iam working")

    def drive(self):
        print("iam driving")

    def refuel(self):
        print("will refuel")

    def send_mail(self):
        print("will send email")

class office:
    def __init__(self,name,employees):
        self.__name=name
        self.__employees=employees

# - Car Class:
#  - attributes (name, fuelRate, velocity)
#  -methods (run, stop)
class car:
    def __init__(self,name,fuelRate,speed):
        self.__name=name
        self.__fuelRate=fuelRate
        self.__speed=speed

    def run(self):
        print("will run")

    def stop(self):
        print("will stop")
class Car:
    def __init__(self, name,feulRate,velocity):
        self.name = name
        self.set_feulRate(feulRate)
        self.set_velocity(velocity)
        
        print(name,feulRate,velocity)

    def get_feulRate(self):
        return self._feulRate

    def set_feulRate(self, value):
        if value not in range(0,101):
            raise ValueError(" feul error")
        self._feulRate = value 

    def get_velocity(self):
        return self._velocity

    def set_velocity(self, value):
        if value not in range(0,201):
            raise ValueError("velocity error")
        self._velocity= value 

    def run(self,velocity):
        velocity=velocity
        print("velocity is:",velocity,", ","distace is:",Employee.drive(self,20))


    def stop(self):
        self._velocity=0
        print("you arrived")




alaa=employee(1,"alaa",122,"crazy","fine","nissan","alaa@ckc.com",20000,200)
