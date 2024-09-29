def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    while True:
        try:
            n = int(input("Type a number to calculate its factorial: "))
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Type a non-negative integer.")

    print("Result:", factorial(n))

if __name__=="__main__":
    main()
