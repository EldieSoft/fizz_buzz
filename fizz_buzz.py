num = int(input("Enter a number: "))

for i in range(num+1):
    if i % 15 == 0:
        print("Fizz-buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

