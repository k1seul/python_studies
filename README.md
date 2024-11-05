# python_studies
Hanseul's studies on python(python, pytorch etc.)


## [Fluent Python](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
![Fluent Python](https://m.media-amazon.com/images/I/81OvszBEdhL._UF894,1000_QL80_.jpg)
### About 
* Data structures: Sequences, dicts, sets, Unicode, and data classes
* Functions as objects: First-class functions, related design patterns, and type hints in function declarations
* Object-oriented idioms: Composition, inheritance, mixins, interfaces, operator overloading, protocols, and more static types
* Control flow: Context managers, generators, coroutines, async/await, and thread/process pools
* Metaprogramming: Properties, attribute descriptors, class decorators, and new class metaprogramming hooks that replace or simplify metaclasses

### Doing: Reading and Code examples 
### Part 1: Data structures 
#### ch1. The Python Data Model
* Everything in python is [classes](https://docs.python.org/ko/3/tutorial/classes.html)!

#### ch2. An Array of Sequences 
* [List Comprehensions](https://docs.python.org/2/tutorial/datastructures.html) and [Generators](https://wiki.python.org/moin/Generators)
* [Tuples](https://docs.python.org/3/tutorial/datastructures.html) are immutable list!
* [Packing and unpacking](https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python
* [Container datatypes](https://docs.python.org/ko/3/library/collections.html) queue, deque, etc...

#### ch3. Dictionaries and Sets
* [Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
* [Sets](https://www.w3schools.com/python/python_sets.asp) sets operations are just like in math!
* [Pattern Matching](https://peps.python.org/pep-0636/) -> still quite didn't understand.

#### ch4. Unicode Text Versus Bytes
* Skimmed through -> read when needed

#### ch5. Data Class Builders
* More about [Container datatypes](https://docs.python.org/ko/3/library/collections.html) queue, deque, etc...

#### ch6. Object References, Mutability, and Recycling
* [equality in python](https://www.tutorialspoint.com/difference-between-eq-vs-is-vs-in-python)
* Object Identity, Type, and Value: Every Python object has a unique identity, a type, and a value. While an object's value may change, its identity and type remain constant.
* Mutability and Immutability: Immutable objects, like integers or strings, cannot change after creation, while mutable objects, like lists, can. However, immutable collections (e.g., tuples) containing mutable items can have their values indirectly altered if any contained mutable item changes.
* Variable References and Assignments: Variables in Python hold references to objects. Simple assignment copies the reference, not the object, while augmented assignments (e.g., +=) create new objects for immutable items but modify mutable items in place. Rebinding a variable to a new object discards the reference to the original object.
* Function Parameter Behavior: Function arguments are passed as aliases. Functions can modify mutable arguments, and changes to mutable default parameter values persist across function calls if not handled carefully.
* Garbage Collection and Weak References: Python’s garbage collection discards objects with zero references, including cyclically referenced groups. Weak references, useful for non-owning references to objects, are supported through WeakValueDictionary, WeakKeyDictionary, WeakSet, and finalize.

#### ch10. Design Patterns with First-Class Functions
*design pattern* is a general reciple for solving common design problems. 
### Refactoring

* **Classic Strategy**  
  Define a family of algorithms, encapsulate each one, and make them interchangeable.

  ```python
  from abc import ABC, abstractmethod
  from decimal import Decimal
  
  class Promotion(ABC):
      @abstractmethod  # Use abstract method so it can be changed later by children classes
      def discount(self, order: Order) -> Decimal:
          """Return discount as a positive dollar amount"""

  class Promo1(Promotion):
      def discount(self, order: Order) -> Decimal:
          rate = Decimal(0.05)
          if condition:
              return order.total() * rate 
          return Decimal(0)


* **Function-Oriented Strategy**
Define a function doing the exact thing as the class.

  ```python
  def promo_1(order: Order) -> Decimal:
    rate = Decimal(0.05)
    if condition:
        return order.total() * rate
    return Decimal(0)



| Refactoring Aspect               | **Class Refactoring**                                                                                      | **Function Refactoring**                                                                       |
|----------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Modularity & Reusability**     | Encourages modularity and reuse.                                                                           | Improves readability by breaking down code into smaller, meaningful pieces.                    |
| **Encapsulation**                | Encapsulates related data and behavior, improving readability.                                             | Lacks the structural benefits and encapsulation of class-based refactoring for complex systems.|
| **Code Complexity**              | Can lead to over-engineering and increased complexity with inheritance.                                    | May lead to scattered code if functions are too specialized or granular.                       |
| **Readability & Maintainability**| Makes code easier to maintain by grouping related functionality.                                           | Reduces code duplication, especially for repeated tasks.                                       |
| **Performance**                  | Can increase memory usage and reduce performance due to object-oriented overhead.                          | May increase stack usage if functions are deeply nested or overly fragmented.                  |
| **Testing**                      | Simplifies testing by breaking functionality into discrete, testable units.                               | Eases testing by allowing isolated, unit-based function tests.                                 |
| **Flexibility & Scope**          | Supports polymorphism, allowing flexible use of derived classes.                                          | Isolates specific actions, limiting scope and impact of changes to individual functions.       |


### Decorator-Enhanced Strategy Pattern

* **Overview**  
  Use a decorator to register and apply different promotion strategies dynamically. This approach simplifies adding or modifying strategies without altering existing code.

  ```python
  from decimal import Decimal
  from typing import Callable, List

  # Dictionary to hold all registered promotion strategies
  promotions: List[Callable[[Order], Decimal]] = []

  # Decorator for registering a promotion strategy
  def promotion_strategy(func: Callable[[Order], Decimal]) -> Callable[[Order], Decimal]:
      promotions.append(func)
      return func

  # Example usage of the decorator to register a strategy
  @promotion_strategy
  def promo_1(order: Order) -> Decimal:
      rate = Decimal(0.05)
      if condition:
          return order.total() * rate
      return Decimal(0)

  @promotion_strategy
  def promo_2(order: Order) -> Decimal:
      rate = Decimal(0.10)
      if another_condition:
          return order.total() * rate
      return Decimal(0)

  # Function to apply the best available promotion
  def best_promotion(order: Order) -> Decimal:
      return max(promo(order) for promo in promotions)


**Benefits**
* Extensibility: New promotion strategies can be added easily by defining a function and applying the @promotion_strategy decorator.
* Modularity: The promotion logic is separated from the main order processing, making it more readable and maintainable.
* Runtime Flexibility: Promotions can be evaluated dynamically, allowing selection of the best applicable strategy.


### Command Pattern

* **Overview**  
  The Command Pattern encapsulates a request as an object, allowing you to parameterize clients with queues, requests, or logs. It’s useful for undo operations and when you need to queue commands.

  ```python
  from abc import ABC, abstractmethod

  # Command Interface
  class Command(ABC):
      @abstractmethod
      def execute(self) -> None:
          """Execute the command."""

      @abstractmethod
      def undo(self) -> None:
          """Undo the command."""

  # Receiver: the class on which operations are performed
  class Light:
      def on(self) -> None:
          print("Light is on")

      def off(self) -> None:
          print("Light is off")

  # Concrete Command to turn on the light
  class LightOnCommand(Command):
      def __init__(self, light: Light):
          self.light = light

      def execute(self) -> None:
          self.light.on()

      def undo(self) -> None:
          self.light.off()

  # Concrete Command to turn off the light
  class LightOffCommand(Command):
      def __init__(self, light: Light):
          self.light = light

      def execute(self) -> None:
          self.light.off()

      def undo(self) -> None:
          self.light.on()

  # Invoker: stores commands and executes them
  class RemoteControl:
      def __init__(self):
          self.history = []

      def submit(self, command: Command) -> None:
          command.execute()
          self.history.append(command)

      def undo_last(self) -> None:
          if self.history:
              command = self.history.pop()
              command.undo()

  # Client Code
  light = Light()
  light_on = LightOnCommand(light)
  light_off = LightOffCommand(light)
  remote = RemoteControl()

  remote.submit(light_on)  # Output: "Light is on"
  remote.submit(light_off) # Output: "Light is off"
  remote.undo_last()       # Output: "Light is on" (undoes turning the light off)


**Benefits**
* Encapsulation: Commands encapsulate all information needed for a request.
* Undoable Actions: Since each command knows how to undo itself, actions can easily be reversed.
* Extensibility: New commands can be added without modifying existing code.


#### ch11. A Pythonic Object
talks about python class methods 

#### \_\_method__ (*dunder method*)
##### Difference between \__str__, \__repr__ 

  ```python
  class Point:
      def __init__(self, x, y):
          self.x = x
          self.y = y
  
      def __str__(self):
          return f"Point({self.x}, {self.y})"
  
      def __repr__(self):
          return f"Point(x={self.x}, y={self.y})"
  
  # Create an instance of Point
  p = Point(1, 2)
  
  # Using __str__
  print(str(p))  # Output: Point(1, 2)
  print(p)       # Output: Point(1, 2)
  
  # Using __repr__
  print(repr(p))  # Output: Point(x=1, y=2)
  ```

#### Difference between class method and static method

   ```python
  class Demo:
      # Class method that takes variable arguments
      @classmethod
      def klassmeth(*args):
          # Returns the arguments passed to the method
          return args 
  
      # Static method that also takes variable arguments
      @staticmethod
      def statmeth(*args):
          # Returns the arguments passed to the method
          return args 
  
  # Calling the class method with no arguments
  # This will print a tuple with the class itself as the first argument
  print(Demo.klassmeth())  # Output: (<class '__main__.Demo'>,)
  
  # Calling the class method with one argument ('spam')
  # This will print a tuple containing the class and the argument
  print(Demo.klassmeth('spam'))  # Output: (<class '__main__.Demo'>, 'spam')
  
  # Calling the static method with no arguments
  # This will print an empty tuple
  print(Demo.statmeth())  # Output: ()
  
  # Calling the static method with one argument ('spam')
  # This will print a tuple containing the argument
  print(Demo.statmeth('spam'))  # Output: ('spam',)
  ```
#### @property 

@property
The @property decorator is used to define a method as a property. This allows you to access the method as if it were an attribute, providing a way to encapsulate getter and setter functionality without changing the way the attribute is accessed


#### \__ (Double Underscore)
The double underscore prefix (also known as "dunder") is used in Python to invoke name mangling, which helps avoid naming conflicts in subclasses. Attributes with a double underscore are intended to be private to the class and are not meant to be accessed directly from outside the class.

Name Mangling: When you prefix a variable with two underscores, Python changes its name in a way that makes it harder to create subclasses that accidentally override the private attributes and methods.

#### Saving memory with \__slots__ 

When you define a class in Python, each instance of that class typically has a dictionary (\__dict__) that stores all of its attributes. This allows for dynamic attribute creation but can consume a significant amount of memory. By defining \__slots__, you can explicitly declare a fixed set of attributes for your class, and Python will allocate a more memory-efficient structure to hold these attributes, eliminating the need for \__dict__


```python
import sys

class PointWithSlots:
    __slots__ = ['x', 'y']  # Declare the attributes to be stored

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointWithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Memory size of an instance without __slots__
point_without_slots = PointWithoutSlots(1, 2)
print(f"Memory without __slots__: {sys.getsizeof(point_without_slots)} bytes")

# Memory size of an instance with __slots__
point_with_slots = PointWithSlots(1, 2)
print(f"Memory with __slots__: {sys.getsizeof(point_with_slots)} bytes")

"""
Output:
Memory without __slots__: 56 bytes
Memory with __slots__: 48 bytes
"""

```
#### Huge memory saving! 
![image](https://github.com/user-attachments/assets/78878e78-e16d-479d-aef7-e3528bf94325)

# ch13. Interface, Protocols, and ABCs 

## Duck Typing in Python
Duck Typing is a programming concept in Python where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type. The term comes from the phrase:

"If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

In Python, you don't need to explicitly check an object's type. Instead, you can just use the object if it implements the required methods or properties.

## Protocols

*Dynamic Protocol
  * Defined by convention: A class adheres to a dynamic protocol if it implements methods with specific names and signatures, as described in documentation or expected by convention.
  * No explicit type checks: The conformance to the protocol is determined at runtime by duck typing—"If it looks like a duck and quacks like a duck, it must be a duck."

* Usage: Monkey patching
  * Quick fix method by inserting the method needed

```python
def new_greet():
    print("Hi, Universe!")

# Monkey patch the greet method
OriginalClass.greet = new_greet

# Now, any instance of OriginalClass will use the patched method
obj = OriginalClass()
obj.greet()  # Output: Hi, Universe!
```

* Static Protocol
  * Explicit definition: A static protocol is explicitly defined by subclassing typing.Protocol.
  * Type checking: Tools like mypy can check at compile time whether a class implements the required methods and attributes defined in the protocol
 
## Goose Typing 

Goose Typing is not a standard term in programming but is sometimes humorously used to contrast with Duck Typing. While Duck Typing is about checking if an object behaves like a duck (i.e., has the required methods), Goose Typing emphasizes that the object should not only have the methods but also behave correctly when those methods are called.

* What Goose Typing Implies:
  * Correct Behavior: In addition to having the right methods, the object must also perform correctly according to the expected semantics of those methods.
  * Deeper Verification: Goose Typing implies a stricter adherence to expected behavior, not just method names and signatures

## Abstract Base Classes(ABC) 

In Python, abc stands for Abstract Base Classes, a module in the standard library used to define abstract base classes. Abstract base classes (ABCs) are a form of interface definition, allowing developers to specify methods that must be implemented by any concrete subclass.

Key Points about abc Module
Purpose:

The abc module provides the infrastructure for defining abstract base classes.
It helps enforce that certain methods or properties are implemented in subclasses.
Useful in defining and ensuring adherence to an interface or contract in a hierarchy of classes.
Defining an Abstract Base Class:

You define an ABC by subclassing ABC (from the abc module).
Use the @abstractmethod decorator to mark methods that must be implemented by subclasses.

  ![[Figure from Fluent Python](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)](https://github.com/user-attachments/assets/369ce794-7b91-43d2-8ccf-71bba56d5ede)

* For fun Exception class hierarchy
![image](https://github.com/user-attachments/assets/736a8443-32b7-448f-8fc2-a132cb276ce2)


