<!--
.. title: Python Design Patterns - Introduction
.. slug: 01-intro
.. date: 2016-09-26 16:22:03 UTC+08:00
.. tags: book, python, design-patterns, introduction, Chetan Giridhar
.. category:
.. link:
.. description:
.. type: text
-->



#Understanding Object-Oriented Programming

## Objects
Objects are described as:

- They represent entities in your application under development
- Entities interact among themselves to solve real-world problems

## Classes
Classes help represent real-world entities by:

- Classes define objects in attributes and behaviors. Attributes are data members and behaviors are manifested by the member functions
- Classes consist of constructors that provide the initial state of these objects
- Classes are like templates and hence can be easily reused.

## Methods
Methods are described as following:

- They represent the behavior of the objects.
- Methods work on attributes and also implement the desired functionality.

```python
    class Person(object):
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def get_person(self,)
        return "<Person (%s, %s)>" % (self.name, self.age)

    p = Person("John Doe", 32)
    print("Type of Object:", type(p), "Memory Address:" , id(p))

```

# Major Aspects of Object-Oriented Programming

## Encapsulation
Key Features are:

- an object's behavior is kept hidden from the outside world or objects kept their state information private.
- Clients can't change the object's internal state by directly acting on them; rather clients request the object by sending messages. Based on the type of requests, objects may respond by changing their internal state using special member functions such as `get` or `set`
- In Python, the concept of encapsulation isn't implicit, as it doesn't have keywords such as public, private, and protected that are required to support encapsulation. Accessibility is on the other hand made private by prefixing `__` in the variable or function name.

## Polymorphism
Key Features are:

- There are two types:
    - An object provides different implementations of the method based on input parameters.
    - The same interface can be used by objects of different types.
- In Python, polymorphism is built in for the language.
- Examples:
    - The + operator can act on two integers to add them or can work with strings to concatenate them.
    - Strings, tuples and lists can all be accessed with an integer index. I.E, `s(1)`, `t(2)` or `l(-1)`.

## Inheritance

- Inheritance indicates that one class derives (most of its) functionality from the parent class.
- Inheritance is described as an option to reuse functionality defined in the base class and allow independent extensions of the original software implementation.
- Inheritance creates hierarchy via the relationships among objects of different classes. Python, unlike Java, supports multiple inheritance (inheriting multiple base classes).

## Abstraction
Key Features are:

- It provides you with a simple interface to the clients, where the client can interact with the class object and call methods defined in the interface.  
- It abstracts the complexity of internal classes with an interface so that the client needs not aware of the internal implementation.  

```python
    class Adder:
      def __init__(self):
        self.sum = 0
      def add(self, value):
        self.sum += value

    acc = Adder()
    for i in range(99):
      acc.add(i)

    print(acc.sum)
```

## Composition
Key Points:

- It is a way to combine objects or classes into more complex data structures or software implementation
- In composition, an object is used to call member functions other modules thereby making base functionality available across modules without inheritance.  

```python
    class A(object):
      def a1(self):
      print("a1")

    class B(object):
      def b(self):
      print("b")
      A().a1()

    objectB = B()
    objectB.b()
```


# Object-Oriented Design Principles

## The Open/Close Principle
The open/close principle states that _classes or objects and methods should be open for extension but closed for modifications._  

For example, the open/close principle is manifested in a case where a user has to create a class implementation by extending the abstract base class to implement the required behavior instead of changing the abstract class.

The advantages of this design principle are:

- Existing classes are changed and hence the chances of regression are less.
- It also helps maintain backward compatibility for the previous code.

## The Inversion of Control Principle
The inversion of control principle states that _high-level modules shouldn't be dependent on low-level modules; they should both be dependent on abstractions.  Details should depend on abstractions but not the other way around._

The principle suggests that any two modules shouldn't be dependent on each other in a tight way but should be decoupled with an abstraction layer in between.  It also suggests that the details of the class should represent the abstractions. In some cases, where the philosophy gets inverted and implementation details itself decide the abstraction, which should be avoided.  

Advantages of the inversion of control principles are as follow:

- The tight coupling of modules is more prevalent and hence no complexity/rigidity in the system.  
- As there is a clear abstraction layer between dependent modules (provided by a hook or parameter), it's easy to deal with dependencies across modules in a better way.  

## The Interface Segregation Principle
The interface segregation principle states, _clients should not be forced to depend on interfaces they don't use._

It reminds developers to develop methods that relate to the functionality.  If there is any method that is not related to the interface, the class dependent on the interface has to implement it unnecessarily.  For example: a `Pizza` interface shouldn't have a method called `add_chicken()`.  The `VegePizza` class based on `Pizza` shouldn't be forced to implement this method.  

Advantages of this design principle are:

- It forces developers to write thin interfaces and have methods that are specific to the interface
- It helps you not to populate by adding unintentional methods

## The Single Responsibility Principle
The single responsibility principle states, _a class should have only one reason to change._  

When a class is developed, it should cater to the given functionality well.  If it is serving two functionalities, it is better to split them.  It refers to functionality as a reason to change.  For example, a class can undergo changes because of the difference in behavior expected in it, but if a class is changed for two reasons (ie changes in two functionalities), then the class should definitely be split.  

Advantages of this design principle:

- Whenever there is a change in one functionality, this particular class needs to change, and nothing else.
- Additionally, if a class has multiple functionalities, the dependent classes will have to undergo changes for multiple reason, which gets avoided.  


## The Single Responsibility Principle
The substitution principle states that _derived classes must be able to completely substitute the base classes._  

It says when developers write derived classes, they should extend the base classes.  The derived class should be as close to the base class as possible so much so that the derived class itself should replace the base class without any code changes.  

# The Concept of Design Patterns
Design patterns were first introduced by **GoF** (**Gang of Four**), where they mentioned them as being solutions to given problems.  The book, [Design Patterns: Elements of Reusable Object-Oriented Software][b1638219], covers software engineering solutions to the commonly occurring problems in software design.  There are 23 design patterns first identified, and first implemented to the Java programming language.  _Design patterns are discoveries, and not invention in themselves._  

  [b1638219]: http://bla "Design Patterns by Gang of Four"

The key features of design patterns are:

- They are language-neutral and can be implemented across multiple languages
- They are dynamic, as new patterns get introduced every now and then
- They are open for customization and hence useful for developers

One would also find:

- It is a panacea to all design problemsthat a developer has had so far
- It's an extraordinary, specially clever way to solving a problem
- Many experts in software development world agree to these solutions
- There's something repeatable about the design, hence the word pattern

Completeness in a software solution refers to many factors such as design, scalability, reuse, memory utilization and etc.  

## Advantages of Design Patterns
The advantages of design patterns are:
- They are reusable across multiple projects
- The architectural level of problems can be solved.
- They are time-tested and well-proven, which is the experience of developers and architects
- They have reliability and dependence

## Taxonomy of Design Patterns
Not every piece of code/design can be termed as a design patterns.  
- **Snippet**: Some code in some language for a certain purpose, for example, DB connectivity in Python can be a code Snippet
- **Design**: A better solution to solve a particular problem.
- **Standard**: A way to solve some kind of problems, which can be very generic and applicable to a situation at hand.
- **Pattern**: A time-tested, efficient and scalable solution that will resolve entire class of known issues.  

## Context - The Applicability of Design Patterns
To use design patterns efficiently, application developers must be aware of the context where design patterns apply.  Context are classified into the following categories:

- **Participants**: They are classes that are used in design patterns.  Classes play different roles to accomplish multiple goals in the pattern.  
- **Non-functional Requirements**: Requirements such as memory optimization, usablility and performance fall under this category.  These factors impact the complete software solution and are thus critical.
- **Trade-offs**: Not all design patterns fit in (application development) as it is, and trade-offs are necessary.  These are decisions
that you take while using a design pattern in an application.  
- **Results**: Design patterns can have a negative impact on other parts of the code if the context is not appropriate.  Developers should understand the consequences and use of design patterns.  

# Patterns for Dynamic Languages
Python is a dynamic language.  The dynamic nature of Python can be represented as follows:

- Types or classes are objects at runtime.
- Variables can have type as a value and can be modified at runtime.  For example, a = 5 and a = "John", the a variable is assigned at runtime and type also gets changed.
- Dynamic languages have more flexibility in terms of of class restrictions.
- In Python, polymorphism is built into the language, there is no keywords such as `private` and `protected` and everything is public by default.  
- Represents a case where design patterns can be easily implemented in dynamic languages.

# Classifying Patterns
The GoF generally classified 23 patterns under three main categories:

- Creational Pattern
    - They work on the basis of how objects can be created
    - They isolate the details of object creation
    - Code is independent of the type of object to be created
    - An example of a creation pattern is the Singleton pattern.

- Structural Pattern
    - They design the structure of objects and classes so that they can compose to archive larger results
    - The focus is on simplifying the structure and identifying the relationship between classes and objects
    - They focus on class inheritance and composition
    - An example of a behavioral pattern is the Adapter pattern.

- Behavioral Pattern
    - They are concerned with the interaction among objects and responsibility of objects
    - Objects should be able to interact and still be loosely coupled.  
