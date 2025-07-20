# 🧪 Exercise: Filter and Process a List of User Inputs
# You're given a list of strings that represent user inputs. Some are valid integers, some are empty, and some are invalid (like letters).
# Write a program that:
# - Tries to convert each item to an integer.
# - If conversion fails, print a warning and continue to the next item.
# - If the value is negative, skip it (using continue).
# - If the value is zero, break the loop and stop processing.
# - For positive numbers, print the square.

# user_inputs = ["10", "abc", "-5", "", "3", "0", "20"]

# Expected Output:
# 100
# Warning: Invalid input 'abc'. Skipping.
# Skipping negative number: -5
# Warning: Invalid input ''. Skipping.
# 9
# Encountered zero. Stopping.

# Fill in the logic using try, except, continue, and break appropriately.

# user_inputs = ["10", "abc", "-5", "", "3", "0", "20"]

# for item in user_inputs:
#     try:
#         number = int(item)
#     except ValueError:
#         print(f"Warning: Invalid input '{item}'. Skipping.")
#         # TODO: Skip to next item
#     # TODO: If number is negative, skip
#     # TODO: If number is zero, stop
#     # TODO: Otherwise, print the square

user_inputs = ["10", "abc", "-5", "", "3", "0", "20"]

for item in user_inputs:
    try:
        number = int(item)
    except ValueError:
        print(f"Warning: Invalid input '{item}'. Skipping.")
        continue 
    if int(item) < 0:
        print(f"Warning: The input value is {item}', less than 0. Skipping.")
        continue # Not pass. Skips the rest of the current loop iteration and goes to the next one
    elif int(item) == 0:
        print(f"Warning: The input value is {item}', equals to 0. Stopping.")
        break #20 is not picked up
    else:
        print(f"Original: {number}, Squared: {number**2}")

