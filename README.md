# Python-Refresher
1. Let's first of all refreshing on basic data types we have:

0/Operators
// Floor division i.e. x//y = 2 (rounds down to the answer to the nearest whole number)
% Modulus: x%y = 1 (gives the remainder when 5 is divided by 2)
** Exponent: no explanation needed
+=, -=, *=: x += 2 -> x = x + 2, x -= y -> x = x-y; x *= 8 -> x = x * 8

1/Integers

2/Float

3/String: can be either using single or double quotes. Use (+) sign for concatenation.
Built-in string functions:
- count(sub,[start,[end]]) returns the number of the times that substring sub appears in the string. case-sensitive. i.e. 'This is a string'.count('s', 4, 10) => 1. The end position is not included. If change to 'This is a string'.count('s', 4, 11) => 2
  
- similar to count, we also have startswith(prefix, [start, [end]]) and endswith(suffix,[start,[end]]). It will return True or False.

- find/index(sub,[start.[end]]):returns the index in the string where the first occurrence of the substring sub is found. find() returns -1 if sub is not found. index() returns ValueError is sub is not found. 'This is a string'.find('s',7,11) #check from index 7 to 11-1. The answer is 10.
  
- isalnum(): returns True if all characters in the string are alphanumeric and there is at least one character. False otherwise. Alphanumeric does not include whitespaces. i.e. 'abcd1234'.isalnum() => True; 'a b c d 1 2 3 4'.isalnum() => False; isalpha(): checks alphabetic; isdigit(): checks all digits or not; islower()/isupper(); isspace(); istitle(): 'This Is A String'.istitle() => True while 'This is a string'.istitle() => False
  
- join(): returns a string in which the argument provided is joined by a speparator.
- i.e. sep='-', myTuple=('a','b','c), sep.join(myTuple) => 'a-b-c'
- i.e. myList=['d','e','f'], sep.join(myList) => 'd-e-f'
- i.e. myString="Hello World", sep.join(myString) => 'H-e-l-l-o- -W-o-r-l-d'

- replace(old, new[,count]): 'This is a string'.replace('s', 'p', 2) => 'Thip ip a string' #replace first 2 occurences, count is optional.
  
- split([sep[,maxsplit]]): 'This is a string'.split() => ['This', 'is', 'a', 'string']; 'This, is, a, string'.split(', ', 2) => ['This', 'is', 'a, string'] #Split using a comma followed by a whitespace as the delimiter. Only do 2 splits.

- splitlines([keepends]): not often used
  
- strip([chars]):'   This is a string   '.strip() => 'This is a string'. If char is not provided, whitespaces will be removed. Otherwise, the char will be removed.

- .upper(),.lower()

4/List
5/Tuple
6/Set
7/Dictionary
99/Type Casting

3. Condition Statements
1/If Statements
- Inline if
2/For loop
3/While Loop
4/Break
5/Continue
6/Try, Except

3. Functions and Modules

4. Working with Files
5. OOP
1/Class
Definition: A class is a template or blueprint that defines how variables (attributes) and functions (methods) are named and used within its objects.

What are the benefits of using a class? (ERS)
| Benefit          | Why It’s Useful                               |
| ---------------- | --------------------------------------------- |
| 1. Encapsulation | Keeps related logic and data together         |
| 2. Reusability   | Allows shared behavior with less code         |
| 3. Statefulness  | Objects can store memory and evolve over time |

When to use a class and when to use a function?
1/Functions = great for stateless tools, scripts, transformations (data transformation/pipelines)
2/Classes = great for stateful models (hint:self), reusable components, large systems (Game design, UI design)

What is a Constructor? Why do we need a Constructor? How a Constructor 

6. More OOP
1/Special Methods
2/Python Built-in Functions for Objects

7. Math and Binary
8. 


Misc. Notes:

What are the different styles of naming a object?

| Style          | Example          | Usage                                                        |
| -------------- | ---------------- | ------------------------------------------------------------ |
| lowerCamelCase | myFunctionName   | Variables, functions in JavaScript, Java, TypeScript         |
| UpperCamelCase | MyClassName      | Class names, types, constructors                             |
| snake_case     | my_variable_name | Python variables and functions                               |
| kebab-case     | my-variable-name | URLs, CSS class names                                        |

