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

