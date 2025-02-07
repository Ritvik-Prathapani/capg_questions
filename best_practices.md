# for loop using enumerate
fruits = ["apple", "banana", "mango"]
## bad practice
for i in range(len(fruits)):
    print(i, fruits[i])
## good practice
for index,fruit in enumerate(fruits):
    print(index, fruit)

## for loop using list comprehension
newList = [fruit for fruit in fruits]
print(newList)


# Ternary operator instead of if-elif
a,b = 5,10
## Bad practice
if a>b:
    print(a)
else:
    print(b)
## Good practice
print(a if a > b else b)


# Nested for loop
## Bad practice
for i in range(3):
    for j in range(3):
        print(i, j)
## Good practice
print([(i,j) for i in range(3) for j in range(3)]) # prints pairs
print(*[f"{i} {j}" for i in range(3) for j in range(3)]) # prints values directly


# Check if prime or not
## Bad practice
def is_prime(n):
    f = 0
    for i in range(2, n):
        if n % i == 0:
            f = 1
    if f == 0:
        print("Prime")
    else:
        print("Not Prime")
is_prime(7)
## Good practice
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
print(is_prime(7))
