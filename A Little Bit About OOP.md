## OOP
### Ch8: Objects, references, writing own classes
Definition: A class is a template or blueprint that defines how variables (attributes) and functions (methods) are named and used within its objects.

Terminology:
- client: is the program code that utilizes the class
- Encapsulation: hides the implementation from the client in order to ensure the internal integrity of the class

What are the benefits of using a class? (ERS)
| Benefit          | Why It’s Useful                               |
| ---------------- | --------------------------------------------- |
| 1. Encapsulation | Keeps related logic and data together         |
| 2. Reusability   | Allows shared behavior with less code         |
| 3. Statefulness  | Objects can store memory and evolve over time |

When to use a class and when to use a function?
- Functions = great for stateless tools, scripts, transformations (data transformation/pipelines)
- Classes = great for stateful models (hint:self), reusable components, large systems (Game design, UI design)

```python
class BankAccount:
  # The constructor
  def __init__(self, balance: float, owner: str):
    self.balance = balance
    self.owner = owner
    self.annual_interest = annual_interest

  # This method adds the annual interest to the balance of the account
  def add_interest(self):
    self.balance += self.balance * self.annual_interest
```

### Ch9: More than one class, getters and setters, visibility, static members
- Objects in data structures: own objects can be stored into a list
- Items stored as referneces: the items stored in a data structure are actually references to items
- Objects as parameters: variable *self* can be used to references the object itself
- Objects as attributes: objects can be stored inside other objects
- None: keyword *None* denotes an empty reference
  
- Getters & Setters: special methods that allow the client to access the hidden attributes
- Getters:`@property` Getter should be defined before the (possible) setter method.
- Setters: `@variable_name.setter`

- Visibility: double underscores before a method name that hides the method from the client

- Static members:
- Class members are called static members, including class variables and class methods.
- *Class Variable*:
- Class variable is defined inside the class definition (but outside methods).
- Variable can be used without instantiating an object out of the class.
- *Class Methods*:
- Class method is defined with *cls* as the first parameter. It also annotated as @classmethod and called as `ClassName.class_method(parameters)`

- 
  



### Ch10: Inheritance and class hierachies
### Ch11: List comprehension, recursion
### Ch12: Generator functions, lambda, reduce, map, filter
### Ch13-14: Game programming with Pygame

## More OOP
### Special Methods
### Python Built-in Functions for Objects

## Math and Binary

