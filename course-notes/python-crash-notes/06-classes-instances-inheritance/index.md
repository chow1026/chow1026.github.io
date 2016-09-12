<!--
.. title: Classes, Instances and Inheritance
.. slug: 06-classes-instances-inheritance
.. date: 2016-09-07 13:12:46 UTC+08:00
.. tags: python-crash-course, classes, instances, inheritance
.. category:
.. link:
.. description:
.. type: text
-->

## Classes ##
- dog.py
```python
  class Dog(): # define class with class_name
    """ A simple attempt to model a dog """ #docstring describing what this class does.  

    def __init__(self, name, age):
      """ Initialize name and age attributes """
      self.name = name
      self.age = age

    def sit(self):
      """ Simulate a dog sitting in response to command """
      print(self.name.title() + " is now sitting.")

    def roll_over(self):
      """ Simulate a dog rolling over in response to a command """
      print(self.name.title() + " rolled over!")
```
- ``` my_dog = Dog('willie', 6) ``` // makes an instance of dog.  
- ``` print("My dog's name is " + my_dog.name.title() + ".") ``` // access name of my_dog.
- ``` print("My dog is " + str(my_dog.age) + " years old.") ``` // access age of my_dog.
- ``` my_dog.sit() ``` // calling sit method
- ``` my_dog.roll_over() ``` // calling roll_over method.
- car.py
```python
  class Car():
    """ A simple attempt to represent a car. """

    def __init__(self, make, model, year):
      """ Initialize attributes to describe a car. """
      self.make = make
      self.model = model
      self.year = year
      self.odometer_reading = 0 # setting default value for an attribute

    def get_descriptive_name(self):
      """ Return a neatly formatted descriptive name."""
      long_name = str(self.year) + ' ' + self.make + ' ' + self.model
      return long_name.title()

    def read_odometer(self):
      """ Print a statement showing the car's mileage."""
      print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
      """
      Set the odometer reading to new value.
      Rejects if it attempts to roll the odometer back.
      """
      if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
      else:
        print("You are not allowed to roll back an odometer")

    def increment_odometer(self, miles):
      """ Add the given amount to odometer reading """
      self.odometer_reading += miles

    def fill_gas_tank(self):
      """ A function to simulate filing gas tank of a car """
      print("Gas tank is filled to full.")

  my_car = Car('audi', 'a4', 2016) #instantiating a car (create an instance of car)
  print(my_car.get_descriptive_name())  
  my_car.read_odometer() # calling method to read odometer value
  my_car.odometer_reading = 45 # modifying an attribute's value directly
  my_car.read_odometer() # calling method to read odometer value again
  my_car.update_odometer(78) # modifying an attribute's value through a method
  my_car.read_odometer() # calling method to read odometer value again
  my_car.increment_odometer(100) # increment a set amount of miles to odometer
  my_car.read_odometer() # calling method to read odometer value again


  class Battery():
    """ A simple attempt to model a battery for an electric car """

    def __init__(self, battery_size = 70):
      """ Initialize the battery's attributes. """
      self.battery_size = battery_size

    def describe_battery(self):
      """ Print a statement describing the battery size """
      print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
      """ Print a statement about the range this battery provides """
      if self.battery_size == 70:
        range = 240
      elif self.battery_size == 85:
        range = 270
      message = "This car can go approximately " + str(range) + " miles on a full charge."
      print(message)

  class ElectricCar(Car):
    """ Represents aspects of a car, but specific to electric vehicle. """

    def __init__(self, make, model, year):
      """ Initialize attributes of the parent class """
      super().__init__(make, model, year)
      """ Initialize attributes specific to an electric car """
      self.battery_size = 70 # specifying initial battery size
      self.battery_size = Battery() # initialize a battery object

    # Method Moved to Battery Class
    #def describe_battery(self):
    #  """ Print a statement describing the battery size """
    #  print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self): # overwrite parent class car's method
      """ Electric Car has no gas tanks """
      print("This car doesn't have a gas tank!")

  my_tesla = ElectricCar('tesla', 'model s', 2016) #instantiating an electric car (create an instance of electric car)
  print(my_tesla.get_descriptive_name())  
  my_tesla.describe_battery() # if battery isn't a separate class.
  my_tesla.battery.describe_battery() # if battery is its separate own class.
  my_tesla.battery.get_range()
```

### Importing Class ###
- The above examples show classes stored in a same file.  When more functionality added to the classes, the file could get long. Thus it is a good idea to store classes in modules and import the classes as needed.  
- car.py
```python
  class Car():
    """ A simple attempt to represent a car. """

    def __init__(self, make, model, year):
      """ Initialize attributes to describe a car. """
      self.make = make
      self.model = model
      self.year = year
      self.odometer_reading = 0 # setting default value for an attribute

    def get_descriptive_name(self):
      """ Return a neatly formatted descriptive name."""
      long_name = str(self.year) + ' ' + self.make + ' ' + self.model
      return long_name.title()

    def read_odometer(self):
      """ Print a statement showing the car's mileage."""
      print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
      """
      Set the odometer reading to new value.
      Rejects if it attempts to roll the odometer back.
      """
      if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
      else:
        print("You are not allowed to roll back an odometer")

    def increment_odometer(self, miles):
      """ Add the given amount to odometer reading """
      self.odometer_reading += miles

    def fill_gas_tank(self):
      """ A function to simulate filing gas tank of a car """
      print("Gas tank is filled to full.")
```
- my_car.py
```python
  from car import Car
  my_car = Car('audi', 'a4', 2016) #instantiating a car (create an instance of car)
  print(my_car.get_descriptive_name())  
  my_car.read_odometer() # calling method to read odometer value
  my_car.odometer_reading = 45 # modifying an attribute's value directly
  my_car.read_odometer() # calling method to read odometer value again
```

### Multiple Classes in one Module ###
- You could store multiple classes in one module, for example keeping both class Car and class ElectricCar in the same file as Car.py, as shown below again.
```python
  class Car():
    """ A simple attempt to represent a car. """

    def __init__(self, make, model, year):
      """ Initialize attributes to describe a car. """
      self.make = make
      self.model = model
      self.year = year
      self.odometer_reading = 0 # setting default value for an attribute

    def get_descriptive_name(self):
      """ Return a neatly formatted descriptive name."""
      long_name = str(self.year) + ' ' + self.make + ' ' + self.model
      return long_name.title()

    def read_odometer(self):
      """ Print a statement showing the car's mileage."""
      print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
      """
      Set the odometer reading to new value.
      Rejects if it attempts to roll the odometer back.
      """
      if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
      else:
        print("You are not allowed to roll back an odometer")

    def increment_odometer(self, miles):
      """ Add the given amount to odometer reading """
      self.odometer_reading += miles

    def fill_gas_tank(self):
      """ A function to simulate filing gas tank of a car """
      print("Gas tank is filled to full.")

  class ElectricCar(Car):
    """ Represents aspects of a car, but specific to electric vehicle. """

    def __init__(self, make, model, year):
      """ Initialize attributes of the parent class """
      super().__init__(make, model, year)
      """ Initialize attributes specific to an electric car """
      self.battery_size = Battery() # initialize a battery object

    def fill_gas_tank(self): # overwrite parent class car's method
      """ Electric Car has no gas tanks """
      print("This car doesn't have a gas tank!")
```
- my_electric_car.py
```python
  from car import ElectricCar
  my_tesla = ElectricCar('tesla', 'model s', 2016) #instantiating an electric car (create an instance of electric car)
  print(my_tesla.get_descriptive_name())  
  my_tesla.describe_battery() # if battery isn't a separate class.
  my_tesla.battery.describe_battery() # if battery is its separate own class.
  my_tesla.battery.get_range()
```

### Importing Multiple Classes from a Module ###
- my_cars.py
```python
  from car import Car, ElectricCar

  my_toyota = Car('Toyota', 'Corola', 2003)
  print(my_toyota.get_descriptive_name())

  my_tesla = ElectricCar('tesla', 'roadster', 2016)
  print(my_tesla.get_descriptive_name())
```

### Importing Entire Module ###
- my_cars.py
```python
  import car

  my_toyota = car.Car('Toyota', 'Corola', 2003)
  print(my_toyota.get_descriptive_name())

  my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
  print(my_tesla.get_descriptive_name())
```

### Importing a Module into a Module ###
- You could also separate Car.py for generic cars properties, and keep all electric car related properties in electric_car.py
- car.py
```python
class Car():
  """ A simple attempt to represent a car. """

  def __init__(self, make, model, year):
    """ Initialize attributes to describe a car. """
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0 # setting default value for an attribute

  def get_descriptive_name(self):
    """ Return a neatly formatted descriptive name."""
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()

  def read_odometer(self):
    """ Print a statement showing the car's mileage."""
    print("This car has " + str(self.odometer_reading) + " miles on it.")

  def update_odometer(self, mileage):
    """
    Set the odometer reading to new value.
    Rejects if it attempts to roll the odometer back.
    """
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You are not allowed to roll back an odometer")

  def increment_odometer(self, miles):
    """ Add the given amount to odometer reading """
    self.odometer_reading += miles

  def fill_gas_tank(self):
    """ A function to simulate filing gas tank of a car """
    print("Gas tank is filled to full.")
```
- electric_car.py
```python
from car import Car

class Battery():
  """ A simple attempt to model a battery for an electric car """

  def __init__(self, battery_size = 70):
    """ Initialize the battery's attributes. """
    self.battery_size = battery_size

  def describe_battery(self):
    """ Print a statement describing the battery size """
    print("This car has a " + str(self.battery_size) + "-kWh battery.")

  def get_range(self):
    """ Print a statement about the range this battery provides """
    if self.battery_size == 70:
      range = 240
    elif self.battery_size == 85:
      range = 270
    message = "This car can go approximately " + str(range) + " miles on a full charge."
    print(message)

class ElectricCar(Car):
  """ Represents aspects of a car, but specific to electric vehicle. """

  def __init__(self, make, model, year):
    """ Initialize attributes of the parent class """
    super().__init__(make, model, year)
    """ Initialize attributes specific to an electric car """
    self.battery_size = Battery() # initialize a battery object

  def fill_gas_tank(self): # overwrite parent class car's method
    """ Electric Car has no gas tanks """
    print("This car doesn't have a gas tank!")
```
- my_cars.py
```python
  from car import Car
  from electric_car import ElectricCar

  my_toyota = Car('Toyota', 'Corola', 2003)
  print(my_toyota.get_descriptive_name())

  my_tesla = ElectricCar('tesla', 'roadster', 2016)
  print(my_tesla.get_descriptive_name())
```
