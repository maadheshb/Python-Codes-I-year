def check_odd_or_even(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
number = int(input("Enter a number: "))
print(check_odd_or_even(number))
