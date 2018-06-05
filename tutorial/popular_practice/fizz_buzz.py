for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    

# for i in range(100):print(i%3//2*"Fizz"+i%5//4*"Buzz"or-~i)