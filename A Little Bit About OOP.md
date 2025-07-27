## OOP
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
  def __init__(self, balance: float, owner: str, annual_interest:float):
    self.balance = balance
    self.owner = owner
    self.annual_interest = annual_interest

  # This method adds the annual interest to the balance of the account
  def add_interest(self):
    self.balance += self.balance * self.annual_interest
```
- Objects in data structures: own objects can be stored into a list
- Items stored as referneces: the items stored in a data structure are actually references to items
- Objects as parameters: variable *self* can be used to references the object itself
- Objects as attributes: objects can be stored inside other objects
- None: keyword *None* denotes an empty reference
  
- Getters & Setters: special methods that allow the client to access the hidden attributes. Getters: `@property` Getter should be defined before the (possible) setter method. Setters: `@variable_name.setter`

- Visibility: double underscores before a method name that hides the method from the client

- What is self:
- A CLASS variable (类变量) belongs to the class and is shared by all instances of the class. It is defined outside any method in the class.
- An INSTANCE variable (实例变量), on the other hand, is defined inside a method and belongs to an instance. It is always prefixed with the *self* keyword.

- When to use CLASS variable? When the value is common to all instances and should stay the same unless explicitly changed for everyone.
For example,
```python
class BankAccount:
    annual_interest = 0.03  # class variable — shared by all accounts

    def __init__(self, balance, owner):
        self.balance = balance  # instance variable
        self.owner = owner      # instance variable

    def add_interest(self):
        self.balance += self.balance * BankAccount.annual_interest
```

There is alwaso the idea of CLASS method. It is used when you want to modify or access class-level data shared across all instances. For example,
```python
@classmethod
def set_interest_rate(cls, new_rate):
    cls.interest_rate = new_rate
```
This is a class method, because of the `@classmethod` decorator. It takes cls as the first argument, which refers to the `class` itself, not a specific object.
| Convention | Refers to            | Commonly Used In                    |
| ---------- | -------------------- | ----------------------------------- |
| `self`     | the **instance**     | instance methods (`def foo(self):`) |
| `cls`      | the **class itself** | class methods (`@classmethod`)      |

There is also `@staticmethod`, which does NOT take `self` or `cls` as the first parameter; Belongs to the `class`, but it doesn’t access or modify class or instance data. Simply a function logically grouped inside the `class`, for organizational clarity.

<img width="678" height="425" alt="image" src="https://github.com/user-attachments/assets/1829d97b-18a1-401c-a86e-066de0f177bc" />

- Class: `Person`
- Instance variables (per object): `name`, `sex`, `profession`
- Instance methods: `work()`, `study()`

| Class Variable                                                | Description                                       |
| ------------------------------------------------------------- | ------------------------------------------------- |
| `species = "Homo sapiens"`                                    | All people are the same species                   |
| `country = "USA"` *(if all people are from the same country)* | Shared attribute                                  |
| `total_people = 0` *(used with `@classmethod`)*               | Count how many `Person` objects have been created |
| `default_study_hours = 10`                                    | A default value used by all unless overridden     |

To reiterate: OOP is a programming paradigm that organizes code around objects — real-world or conceptual "things" that: Have attributes/state (variables). Can perform actions (methods). Belong to a blueprint (class).

Characteristics:
| Principle         | Meaning                                                                       |
| ----------------- | ----------------------------------------------------------------------------- |
| **Encapsulation** | Bundling data (variables) and behavior (methods) inside classes/objects       |
| **Abstraction**   | Hiding complex details and exposing only necessary parts                      |
| **Inheritance**   | Letting one class inherit properties/methods from another                     |
| **Polymorphism**  | Using a shared interface to perform different actions depending on the object |


Abstraction（抽象）: To reduce complexity and focus on what an object does, not how it does it. Think of a car: You just use the steering wheel, pedals, and gear. You don’t need to know how the engine, fuel injection, or brakes work internally.

Polymorphism（多态）:To write flexible, reusable code that can work with objects of different types interchangeably. Both Bird and Plane implement a fly() method — same method name, different behavior.

For example: 
```python
if type(animal) == Dog:
    animal.bark()
elif type(animal) == Cat:
    animal.meow()
```
With abstraction & polymorphism,
```python 
animal.make_sound()  # Much cleaner and extendable
```

| Goal                                                      | What you use   |
| --------------------------------------------------------- | -------------- |
| Hide *how* it's done                                      | ✅ Abstraction  |
| Let objects respond in different ways to the same message | ✅ Polymorphism |

- 


### Ch10: Inheritance and class hierachies
### Ch11: List comprehension, recursion
### Ch12: Generator functions, lambda, reduce, map, filter
### Ch13-14: Game programming with Pygame

## More OOP
### Special Methods
### Python Built-in Functions for Objects

## Math and Binary

