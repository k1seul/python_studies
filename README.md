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
