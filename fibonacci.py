def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    while True:
        try:
            x = int(input("Position in the Fibonacci sequence: "))
            if x < 0:
                raise ValueError
            break
        except ValueError:
            print("Type a non-negative integer")
    print("Fibonacci term:", fibonacci(x))

if __name__=="__main__":
    main()

