# Python-Refresher
## Let's first of all refreshing on basic data types we have:
### Operators
- `//` Floor division `i.e. x//y = 2` rounds down to the answer to the nearest whole number
- `%` Modulus: `x%y = 1` gives the remainder when 5 is divided by 2
- `**` Exponent: no explanation needed
- `+=, -=, *=: x += 2 -> x = x + 2, x -= y -> x = x-y; x *= 8 -> x = x * 8`

### Integers
No more to say.

### Float
No more to say.

### String: 
Can be either using single or double quotes. Use `(+)` sign for concatenation.

#### Built-in string functions:
- `count(sub,[start,[end]])` returns the number of the times that substring sub appears in the string. case-sensitive. i.e. `'This is a string'.count('s', 4, 10) => 1.` The end position is not included. If change to `'This is a string'.count('s', 4, 11) => 2`
  
- similar to count, we also have `startswith(prefix, [start, [end]])` and `endswith(suffix,[start,[end]])`. It will return `True` or `False`.

- `find/index(sub,[start.[end]])`:returns the index in the string where the first occurrence of the substring sub is found. find() returns `-1` if sub is not found. index() returns ValueError is sub is not found. `'This is a string'.find('s',7,11)` Check from index `7` to `11-1`. The answer is `10`.
  
- `isalnum()`: returns True if all characters in the string are alphanumeric and there is at least one character. False otherwise. Alphanumeric does not include whitespaces. i.e. `'abcd1234'.isalnum() => True`; `'a b c d 1 2 3 4'.isalnum() => False`; `isalpha()`: checks alphabetic; `isdigit()`: checks all digits or not; `islower()/isupper()`; `isspace()`; `istitle()`: `'This Is A String'.istitle() => True` while `'This is a string'.istitle() => False`
  
- `join()`: returns a string in which the argument provided is joined by a speparator.
`sep='-', myTuple=('a','b','c), sep.join(myTuple) => 'a-b-c'`
`myList=['d','e','f'], sep.join(myList) => 'd-e-f'`
`myString="Hello World", sep.join(myString) => 'H-e-l-l-o- -W-o-r-l-d'`

- `replace(old, new[,count])`: `'This is a string'.replace('s', 'p', 2) => 'Thip ip a string'` Replace first 2 occurences, count is optional.
  
- `split([sep[,maxsplit]])`: `'This is a string'.split() => ['This', 'is', 'a', 'string']; 'This, is, a, string'.split(', ', 2) => ['This', 'is', 'a, string']` Split using a comma followed by a whitespace as the delimiter. Only do 2 splits.

- `splitlines([keepends])`: not often used
  
- `strip([chars])`:`'   This is a string   '.strip() => 'This is a string'. If char is not provided, whitespaces will be removed. Otherwise, the char will be removed.`

- `.upper()`,`.lower()`

#### Formatting Strings and Digits
- % can be used as formatter in string, for example:
`brand = 'Apple'
exchangeRate = 1.235235245
message = 'The price of this %s laptop is $ %d USD and the exchange rate is $%4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)
print(message)
=> The price of this Apple laptop is $ 1299 USD and the exchange rate is $1.24 USD to 1 EUR` `%4.2f` is total of 4 length and 2 decimal places

- Use `format()` method instead of using % operator
`message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
=> The price of this Apple laptop is 1299 USD and the exchange rate is 1.24 USD to 1 EUR`
The `0,1,2` from `{0:s}, {1:d}, {2:4.2f}` are referring to the positions of this argument `('Apple', 1299, 1.235235245)`.

#### Type Casting Strings and Digits
`int()`, `float()`, `str()`

### List
- Slice a list
Let's say you have a list as `userAge = [21, 22, 23, 24, 25]`.
`userAge[2:4]` will give you items from index 2 to index 4-1 (index 3) => [23, 24]
`userAge[1:5:2]` will get a sub list consisting of every second number from index 1 to index 5-1, b/c the stepper is 2. => `[22, 24]`
`userAge[:4]` will give index 0 to index 4-1
`userAge[1:]` gives index 1 to index 5-1

- `len()`
- Add an item to a list: `userAge.append(99)` -> add the value `99` to the end of the list => `userAge=[21, 22, 23, 24, 25, 99]`
- Add an item to a list at a PARTICULAR POSITION: `insert()`. `myList = ['a', 'b', 'c', 'd'], myList.insert('Hi', 1) => ['a','Hi ,'b', 'c', 'd']`
  
- Combine two lists:  `extend()`
- `myList = ['a', 'b', 'c', 'd', 'e'], myList2 = [11,21,38,12,8], myList.extend(myList2) => ['a', 'b', 'c', 'd', 'e', 11, 21, 38, 12, 8]'`
- If we do `myList.append(myList2) => ['a', 'b', 'c', 'd', 'e', [11, 21, 38, 12, 8]]'`

- Check if an item is in a list: `myList = ['a', 'b', 'c', 'd'], 'c' in myList => True, 'e' in myList => False`

- `reverse()`: Reverse the items in a list. `myList.reverse() => ['d','c','b','a']`

- Addition operator `+`: concatenate the list but the original list won't change
- Multiplication Operator `*` Duplicate a list and concatenate it to the end of the list

###### About Remove Related Operators:
- Remove items, we do `del userAge[2]`: removes the 3rd item from the list
  
- `pop()`: Get the value of an item and remove it from the list. Requires index of item as the argument. The original list will be modified and no need to assign a new list.
- `myList = ['a', 'b', 'c', 'd', 'e'], myList.pop(2) => ['a', 'b', 'd', 'e']`, or:
- `myList = ['a', 'b', 'c', 'd', 'e'], myList.pop() => ['e']` the last item of the list got removed.
- If we do `myList.pop()`
  `print(myList)=> ['a', 'b', 'c', 'd']`
  
###### Note the difference: 
- `del userAge[2]`: Removes the 3rd item from the list without returning it. The original list is modified, and you do not need to create a new list.
if `userAge=[21,22,23,24,25]
del userAge[2]
print(userAge)`
=> `[21, 22, 24, 25]`

- `userAge.pop(2)`: Removes and returns the 3rd item. Also modifies the list in-place. If print out `userAge` the modified list will return.
`userAge=[21,22,23,24,25]
print(userAge.pop(2)) => [23]
print(userAge) = > [21, 22, 24, 25]`

- `remove()`: Remove an item from a list. Requires the value of the item as the argument. i.e.`myList.remove('c') => ['a','b','d','e']`
  
###### About Sorting Related Operators:
- `sort()`: sort a list alphabetically or numerically
- `sorted()`: returns a new sorted list wihout sorting the original list. Requires a list as the aurgument.

###### Note the difference: 
- `myList = [3, 0, -1, 4, 6]`
- `print(myList)  => [3, 0, -1, 4, 6]`
- `print(myList.sort())  => None` will return none
- `print(myList)  => [-1, 0, 3, 4, 6]` The original list is sorted

- `print(sorted(myList)) => [-1, 0, 3, 4, 6]` will return a sorted list
- `new_list = sorted(myList)`
- `print(new_list) => [-1, 0, 3, 4, 6]` the new list will be sorted
- `print(myList) => [3, 0, -1, 4, 6]` the original list is not sorted

### Set
- a `set` is like a deduplicated list. A non-empty `set` can be represented using `{}`, however, if you declare a set, you cannot use `{}`, b/c Python will treat it as a dictionary. A set is unordered, unindexed, and optimized for fast membership checking.

- Only hashable data types can go to a `set`: `int`, `float`, `str`, `bool`, `tuple` (only if all its elements are hashable), `frozenset` (an immutable version of set); Cannot go to a `set`: `list`, `set`, `dic`
- When to use a `set`:
- Remove duplicates: `names = ["Alice", "Bob", "Alice", "Eve"], unique_names = set(names)`  # ➜ {'Alice', 'Bob', 'Eve'}
- Fast membership checks: `set` uses hashing, so checking if an item exists is much faster `(O(1))` compared to a `list` `(O(n))`:
`fruits = {"apple", "banana", "orange"}`
`if "apple" in fruits:`
    `print("Yes!")`  Fast!
- `Set` operations (math-style)
`a = {1, 2, 3}, b = {3, 4, 5}`
`print(a | b)`  Union: `{1, 2, 3, 4, 5}`
`print(a & b)`  Intersection: `{3}`
`print(a - b)`  Difference: `{1, 2}`

### Tuple
- Similar to lists, but cannot modify their values. The initial values are the values that will stay for the rest of the program. 
To declare, it will be `tupleName = (initial values)`. Use parentheses() and separated by a comma. i.e. `monthsOfYear = ("Jan" ,"Feb", ...)`

- `del`: you can say `del myTuple`, this will delete the tuple completely. Cannot modify an item from a tuple. Usually will convert it to a List and then convert back, such as:
`my_tuple = (10, 20, 30)`
`temp_list = list(my_tuple)`
`del temp_list[1]` Remove 20
`my_tuple = tuple(temp_list)`
`print(my_tuple)` => `(10, 30)`
- `in`: check if an item is in a tuple. `myTuple = ('a', 'c'), 'c' in myTuple => True`
- `len()`
- Addition and Multiplication Operators: same as Lists

### Dictionary
- A collection of related data pairs. Dictionary keys and data can be of different data types.
- How to declare a dictionary: `userNameAndAge = dict(Peter= 38, John = 51, Alex = 13, Alvin = "Not Available")` If using dict() method, no need to have quotes for dictionary keys.
- Add an item: `userNameAndAge["Joe"]=40`
- Remove an item: `del userNameAndAge["Joe"]=40`
- `clear()`: Removes all elements of the dictionary, returning an empty dictionary. `dict1.clear(), print(dict1)` => `{}`
- `del`: Deletes the entire dictionary. `del dict1, print(dict1)` => `NameError: name 'dict1' is not defined.`
- `items()`: Returns list of the dictionary's pairs as tuples
- `keys()`: Returns list of the dictionary's keys
- `values()`: Returns list of the dictionary's values
- `get()`: Returns the value of a given key. `dic1 = {1: 'one', 2: 'two'}`, `dic1.get(1)` => `one`; `dic1.get(5, "Not Found")` => `Not Found` Return a user-defined value if the key is not found. 
- `update()`: Adds one dictionary's key-values pairs to another. Duplicates are removed. `dic1 = {1: 'one', 2: 'two'}, dic2 = {1: 'one', 3: 'three'}`, `dic1.update(dic2) => print(dic1) => {1: 'one', 2: 'two', 3: 'three'} and print(dic2) => {1: 'one', 3: 'three'}` no change.
- `in`: Checks if an item is in a dictionary. Based on the key: `1 in dic1` => `True`; Based on the values: `'one' in the dic1.values()` => `True`
- `len()`: Returns the number of items (pairs) of a dictionary

## Condition Statements
### If Statements
- Indentation, indentation, indentation
### Inline if
- `Do Task A if condition is True else do Task B`
### For loop
- Noting more to say, but just if you'd like to display the index of the members in the list. We can do `enumerate()` function.
- `pets = ['cats', 'dogs', 'rabbits', 'hamsters']
- for i, v in enumerate(pets):
- print(i, v)`
  
- Alternatively, this will be:
-`for i in range(len(fruits)):
-  print(i, fruits[i])`

- Loop through a dictionary
- `userNameAndAge = dict(Peter= 38, John = 51, Alex = 13, Alvin = "Not Available")`

- `for i in userNameAndAge:
-  print("Name = %s, Age = %s" %(i, userNameAge[i]))`

`=> Name = Peter, Age = 38
Name = John, Age = 51
Name = Alex, Age = 13
Name = Alvin, Age = Not Available`

- `range(5) => list[0,1,2,3,4]`
- `range(3,10) => list[3,4,5,6,7,8,9]`
- `range(4,10,2) => list[4,6,8]`

### While Loop
`counter = 5
while counter > 0:
  print("Counter =", counter)
  counter -= 1`
  
`=> 
Counter = 5
Counter = 4
Counter = 3
Counter = 2
Counter = 1`

### Break
`counter = 5
while counter > 0:
  print("Counter =", counter)
  counter -= 1
  if counter == 3:
    break`
  
`=> 
Counter = 5
Counter = 4`

### Continue

### Try, Except

## Functions and Modules

## Working with Files

## Misc. Notes:
### What are the different styles of naming a object?
| Style          | Example          | Usage                                                        |
| -------------- | ---------------- | ------------------------------------------------------------ |
| lowerCamelCase | myFunctionName   | Variables, functions in JavaScript, Java, TypeScript         |
| UpperCamelCase | MyClassName      | Class names, types, constructors                             |
| snake_case     | my_variable_name | Python variables and functions                               |
| kebab-case     | my-variable-name | URLs, CSS class names                                        |

