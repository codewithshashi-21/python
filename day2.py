# check even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(check_even_odd(num))


# factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))


# maximum in a list
numbers = [10, 25, 7, 99, 3]
print("Maximum:", max(numbers))


# reverse a list
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print("Reversed:", reversed_list)


# count vowels in string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)
