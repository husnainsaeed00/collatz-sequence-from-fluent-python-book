
    
def collatz(number):
    if (number % 2 == 0):
        return number // 2
    elif (number % 2 != 0):
        return 3 * number + 1

def main():
    number = int(input("Please input a number: "))
    while number != 1:
        print(number)
        number = collatz(number)
    print(number)

if __name__ == '__main__':
    main()