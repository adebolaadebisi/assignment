# python operators
# operators are special symbols in python that performs operations on variables and values.
#types of operators in python
# comparison operators
# Assignment operators
#  Logical operators

# comparison operators: they are used to compare two values. the result is always true or false.
#operator  example  meaning
#==        5==5     equal to
# !=       5!=3      not equal to
# >        7>4       Greater than
# <        3<8        less than
# >=       6>=6       greater than or equal to
# <=       2<=5       less than or equal to

a = 10
b = 20

print(a == b)  # False
print(a !=b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= 10)   # TRue
print(b <= 25)   # True

# use case example - student exam result
score = 75

print(score >= 50)  # True (passed)
print(score < 50)   # False (failed)
print(score == 100) # False (not full marks)

# Assignment operators
# Assignment operators are used to assign values to variables. they can also combine an operation with assignment , so instead of writing x =x+5, we can write x+=5

#| Operator | Example   | Meaning                         |
#| -------- | --------- | ------------------------------- |
#| `=`      | `x = 10`  | Assigns value 10 to `x`         |
#| `+=`     | `x += 5`  | Adds 5 to `x` (`x = x + 5`)     |
#| `-=`     | `x -= 3`  | Subtracts 3 from `x`            |
#| `*=`     | `x *= 2`  | Multiplies `x` by 2             |
#| `/=`     | `x /= 4`  | Divides `x` by 4                |
#| `%=`     | `x %= 3`  | Stores remainder after division |
#| `**=`    | `x **= 2` | Raises `x` to the power of 2    |
#| `//=`    | `x //= 2` | Floor divides `x` by 2          |

x = 10
print("Initial value:", x)

x +=5
print("After x += 5:",x)

x -= 2
print("After x -=2:", x)

x *= 3
print("After x *=3:", x)

x /= 4
print("After x /= 4:", x)

x %=3
print("After x %=3:",x)

x = 4
x **= 2
print("After x **= 2:", x)

x //= 3
print("After x //= 3:", x)

# use case example
# define variables
balance = 1000
deposit = 200
withdraw = 150

balance += deposit # Add deposit
balance -= withdraw # subtract withdrawal
print("updated balance:", balance)
# output: updated balance: 1050

# logical operators
# logical operators are used to combine condition statements. they work with boolean values(True or false).

#| Operator | Example            | Meaning                                |
#| -------- | ------------------ | -------------------------------------- |
#| `and`    | `x > 5 and x < 15` | True if both conditions are true       |
#| `or`     | `x < 5 or x > 20`  | True if at least one condition is true |
#| `not`    | `not(x == 10)`     | True if the condition is false         |

x = 10
y = 20

# and operator
print(x > 5 and y > 15) # True

# or operator
print(x < 5 or y > 15)  # True

# not operator
print(not(x == 10))   # False

# use case example1 - scholarship eligibility
# define variables
age = 17
score = 85

# must be younger than 18 and score above 80
eligible = (age < 18) and (score > 80)

print("Scholarship Eligible:", eligible)
# output: Scholarship Eligible: True

# use case example2 - Event Access
age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)

print("Access Granted:", can_enter)
# output: Access Granted: True (because age < 25 even without ticket)

