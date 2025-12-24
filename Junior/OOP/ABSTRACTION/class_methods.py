from abc import ABC,abstractmethod
class shape(ABC):
  @abstractmethod
  def Area(self):
    pass
  
class square(shape):
  def __init__(self , length):
    self.length = length
  def Area(self):
    a=self.length**2
    print(f"Area = {a}cm^2")
    
class rectangle(shape):
  def __init__(self , length , breadth):
    self.length = length
    self.breadth = breadth
  def Area(self):
    a = self.length*self.breadth
    print(f"Area = {a}cm^2")
    
sq = square(4)
rsq = rectangle(3,4)
sq.Area()
rsq.Area()

class Animal(ABC):
  @abstractmethod
  def make_sound(self):
    pass
class Dog(Animal):
  def __init__(self,sound):
    self.sound=sound
  def make_sound(self):
    print(f"Dog makes the sound {self.sound}")
class Cat(Animal):
  def __init__(self,sound):
    self.sound = sound
  def make_sound(self):
    print(f"Cat makes the sound {self.sound}")

dog = Dog("woof")
cat = Cat("meow")
dog.make_sound()
cat.make_sound()


class payment(ABC):
  @abstractmethod
  def process_amount(self):
    pass
class CardPayment(payment):
  def __init__(self,amt):
    self.amt = amt
  def process_amount(self):
    print(f"${self.amt} successfully withdrawn!")
class MobileMoney(payment):
  def __init__(self, amt):
    self.amt = amt
  def process_amount(self):
    print(f"Hooraay!! ${self.amt} has been subtracted from your account")

card = CardPayment(200)
momo = MobileMoney(100)
card.process_amount()
momo.process_amount()
    



class FileReader(ABC):
    @abstractmethod
    def read_file(self, path):
        pass
class TextFileReader(FileReader):
    def read_file(self, path):
        print(f"Reading TEXT file at: {path}")
        print("Content: This is some sample text from the .txt file.\n")
class JSONFileReader(FileReader):
    def read_file(self, path):
        print(f"Reading JSON file at: {path}")
        print("Content: {'name': 'Lad', 'age': 18}\n")
txt_reader = TextFileReader()
json_reader = JSONFileReader()

txt_reader.read_file("documents/note.txt")
json_reader.read_file("data/user.json")


class Vehicle(ABC):
  @abstractmethod
  def max_speed(self):
    pass
  @abstractmethod
  def wheels(self):
    pass
  
class Car(Vehicle):
  def __init__(self,speed,nowheels):
    self.speed = speed
    self.nowheels = nowheels
  def max_speed(self):
    print(f"This car has a maximum speed of {self.speed}")
  def wheels(self):
    print(f"Also has {self.nowheels} wheels")

class MotorBike(Vehicle):
  def __init__(self,speed,nowheels):
    self.speed = speed
    self.nowheels = nowheels
  def max_speed(self):
    print(f"This car has a maximum speed of {self.speed}")
  def wheels(self):
    print(f"Also has {self.nowheels} wheels")

car = Car("250km/hr" , 4)
motor = MotorBike("120Km/hr" , 2)
car.max_speed()
car.wheels()
motor.max_speed()
motor.wheels()
  

  
  
  