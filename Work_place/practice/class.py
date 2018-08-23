class Human():

    def create(self, name, weight):
#        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat(self):
        self.weight += 0.1
        print ("{} eat so much so becomes {}kg now".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print ("{} walk a lot so becomes {}kg now".format(self.name, self.weight))

    def speak(self, message):
        print(message)


person = Human()
person.create("han", 60.5)
#person = Human.create("han", 60.5)

person.eat()

person.walk()

person.speak("hi how are you")

###########################################################
# class Person :
#     def __init__(self,name):
#         self.name = name
#     def say(self):
#         print ("my name is", self.name)
#
# p1 = Person('han kim')
# p1.say()

###########################################################
# class Person :
#     def __init__(self):
#         self.name = ""
#     def say(self,name):
#         self.name = "my name is + self.name"
#         print (self.name)
#
# p2 = Person()
# p2.say('han kim')
##############################################################

class Man :
    cnt = 0
    def __init__(self,name):
        self.name = name
        print ("{} is  creating......".format(self.name))
        Man.cnt += 1

    def die(self) :
       # "when man object die "
        print("{} is die !!!".format(self.name))
        Man.cnt -= 1

        if Man.cnt == 0 :
            print ("{} is last man".format(self.name))
        else :
            print ("Still {:d} man alive".format(Man.cnt))

    def say(self):
        print("Created!!!,  Hi My name is {}".format(self.name))

    @classmethod
    def how_many(cls):
        #check of how many object left
        print("Currently {} alive".format(Man.cnt))

gameActor1 = Man("Han")
gameActor1.say()
gameActor2 = Man("Kim")
gameActor2.say()

print ("-------------------------------------")
gameActor2.die()
gameActor1.die()
########################################################################


############### Class Basic #################

class Person :
    def __init__(self):
        self.name = ""   #변수를 만들어 준다.
        self.age = ""
    def say(self,name,age):
        self.name = ("my name is : " + name)
        self.age = ("my age is :" + age)
        print(self.name)
        print(self.age)

p2 = Person()
p2.say("han kim","52")  #method 를 call 할때 argument 를 넣어준다, say method 에서 name,age argument 를 expect 하고 있다

##### 위의 방법을 아래와 같이 할수 있다 ##########

class Person2:
    def __init__(self,name,age):
        self.name = name   #들어온 argument(name)을 self.name 에 assign 한다
        self.age = age
    def say(self):
        print("my name is :" + self.name)
        print("my age is :" + self.age)

p3 = Person2("han kim","52")  #class 를 call 할때 argument 를 넣어준다, 왜냐면. __init__ 에서 name,age argument 를 expect 하고 있다
p3.say()

