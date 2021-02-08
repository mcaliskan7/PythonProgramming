def extra_average(func):
    def wrapper(numbers):
        even_num = 0
        even_sum = 0
        odd_num = 0
        odd_sum = 0

        for i in numbers:
            if i % 2 == 0:
                even_sum += i
                even_num += 1
            elif i % 2 != 0:
                odd_sum += i
                odd_num += 1

        print("\nEven numbers' average:",even_sum/even_num,"\nOdd numbers' average:",odd_sum/odd_num)

        func(numbers)
    return wrapper

@extra_average
def average(x):
    sum = 0
    for i in x:
        sum += i

    print("The average:",sum/len(x))

numnum = int(input("How many numbers do you want to calculate average?: "))

numbers = list()

i = 0
while i < numnum:
    a = int(input("Enter {}. number: ".format(i+1)))
    numbers.append(a)
    i += 1

average(numbers)
