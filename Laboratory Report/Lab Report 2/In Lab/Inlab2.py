class Person:  
      
    def __init__(self, name):  
        self.name = name  
      
    def say_hi(self):  
        print('Hello, my name is', self.name)  
     
p1 = Person('Jozhua')  
p2 = Person('Lenard')

  
p1.say_hi()  
p2.say_hi()
