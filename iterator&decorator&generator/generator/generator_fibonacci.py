def fibonacci():
    a = 1
    b = 1

    yield a
    yield b

    while True:
        a, b = b, a+b
        yield b

for i in fibonacci():
    if i > 10000000:
        break

    print(i,end=" ")
