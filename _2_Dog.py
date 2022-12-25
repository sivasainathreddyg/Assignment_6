class Dog:
    def __init__(self,name,age,coat_color):
      self.name=name
      self.age=age
      self.coat_color=coat_color
    def description(self):
        print(f'the name of the dog is {self.name}')
        print(f'the dogs age is {self.age}')
    def get_info(self):
        print(f'the coat color of {self.name} is {self.coat_color}')

class JackRussellTerrier(Dog):
    def weight(self,weight=30):
        self.weight=weight
        print(f'the weight of {self.name} is {self.weight} pounds ')
        
    def life_span(self,lifespan):
        self.lifespan=lifespan
        print(f'the lifespan of {self.name} is {self.lifespan} years ')
class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
    def color(self,color):
        self.color=color
        print(f'the color of {self.name} is {self.color}')
    def bark(self,bark,gender):
        self.bark=bark
        self.gender=gender
        print(f'{self.name} is a {self.gender} and says {self.bark}')
obj=JackRussellTerrier('German Shepherd',8,'black')
obj.weight()
obj.life_span(13)

obj2=Bulldog('Golden Retriver',5,'black')
obj2.color('white')
obj2.bark('bow bow','male')