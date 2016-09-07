<!--
.. title: Functions and Modules
.. slug: 05-functions-modules
.. date: 2016-09-07 11:14:55 UTC+08:00
.. tags: python-crash-course, functions, modules
.. category:
.. link:
.. description:
.. type: text
-->

## Functions ##
- ``` def function_name():``` // define a function

### Parameters and Arguments ###
- ``` def describe_pet(animal_type, pet_name):``` // define function describe_pet with parameter animal_type and pet_name
- ``` describe_pet('dog', 'willie') ``` // calling function describe_pet and passing 'dog' and 'willie' as positional arguments, order matters.
- ``` describe_pet(animal_type = 'dog', pet_name = 'willie') ``` or ``` describe_pet(pet_name = 'harry', animal_type = 'hamster', ) ``` // calling function describe_pet and passing 'dog' and 'willie' as positional arguments, order doesn't matter.
- ``` def describe_pet(pet_name, animal_type = 'dog'):``` // define function describe_pet with parameter animal_type, its default value 'dog' and pet_name.  Parameter with default value usually listed last.
- ``` def get_formatted_name(fname, lname, mname=''):``` // define function get_formatted_name with parameters fname, lname, and optional mname.  Optional parameter also listed last.
- When a list is passed to a function, the function can modify the list.  Any changes made to the list inside the function's body are permanent.  
- Sometimes, you may decide you want to keep the original list unchanged.  In that case, you may pass the function with a copy of the list.
- ``` function_name(list_name[:]) ``` // calling function_name and pass a copy of list_name by ' list_name[:] '

### Passing an Arbitrary Number of Arguments ###
- Sometimes you won't know ahead of times how many arguments a function needs to accept.  In this case, we define a function with \*parameter to collect as many arguments as the calling line provides.
- ``` def make_pizza(*toppings): ``` // the asterisk in the parameter name \*toppings tells python to make an empty tuple and pack whatever values it receives into this tuple.  
- Eg: ``` make_pizza('pepperoni') ``` or ``` make_pizza('mushrooms', 'green peppers', 'extra cheese') ```
- ``` def make_pizza(size, *toppings): ``` // mix positional and arbitrary arguments
- Eg: ```make_pizza(16, 'pepperoni')``` or ``` make_pizza(24, 'mushrooms', 'green peppers', 'extra cheese') ```

### Using Arbitrary Keyword Arguments ###
- Sometimes you'll want to accept an arbitrary number of arguments, but won't know ahead of time what kind of information will be passed to the function.  In this case, you can write functions that accept as many key-value pair as the calling statement provides.
```python
    def build_profile(fname, lname, **user_info):
          profile = {}
          profile['first_name'] = fname
          profile['last_name'] = lname
          for key, value in user_info.items():
              profile[key] = value
          return profile
```
- \**user_info represents an arbitrary number of keyword arguments.  
- Eg: ``` user_profile = build_profile('albert', 'einstein', location='princeton', field='physics') ```


## Modules ##
- A module is a file ending in .py that contains the code you want to import to your program.  For example, to make a module that contains the function make_pizza(), move the function make_pizza() to a file pizza.py.  
- pizza.py
```python
  def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
      print("- " + topping)
```
- making_pizza.py
```python
  import pizza

  pizza.make_pizza(16, 'pepperoni')
  pizza.make_pizza(24, 'mushrooms', 'green peppers', 'extra cheese')
```

### Importing Specific Functions ###
- ``` from module_name import function_name```
- ``` from module_name import function_0, function_1, function_2```
```python
  from pizza import make_pizza

  make_pizza(16, 'pepperoni')
  make_pizza(24, 'mushrooms', 'green peppers', 'extra cheese')
```

### Use as to Give a Function an Alias ###
- ``` from module_name import function_name as fn ```
```python
  from pizza import make_pizza as mp
  mp(16, 'pepperoni')
  mp(24, 'mushrooms', 'green peppers', 'extra cheese')
```

### Use as to Give a Module an Alias ###
- ``` import module_name as mn ```
```python
  import pizza as p
  p.make_pizza(16, 'pepperoni')
  p.make_pizza(24, 'mushrooms', 'green peppers', 'extra cheese')
```

### Import All Functions in a Module ###
- ``` from module_name import * ```
```python
  from pizza import *
  make_pizza(16, 'pepperoni')
  make_pizza(24, 'mushrooms', 'green peppers', 'extra cheese')
```
- However it is best not to use this approach.  Python may see several functions or variables with the same name, and instead of importing all the functions separately it will overwrite the functions.
