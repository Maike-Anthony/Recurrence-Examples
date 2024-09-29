def collatz(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return collatz(n/2) + 1
    else:
        return collatz(3*n + 1) + 1

def main():
    while True:
        try:
            n = int(input("Number: "))
            if n < 1:
                raise ValueError
            break
        except ValueError:
            print("Type a positive integer.")

    print("Number of steps to reach one:", collatz(n))


if __name__=="__main__":
    main()
