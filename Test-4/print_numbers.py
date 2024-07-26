# print_numbers.py

# The included code stub will read an integer, n , from STDIN.

# Without using any string methods, try to print the following:

# 123...n

def print_numbers(n):
    # CODE BELOW THIS LINE
    # We cannot use string methods, so we use print with end=''
    for i in range(1, n+1):
        num= (i, end = '')
        # print(i, end = '')

    return num

if __name__ == '__main__':
    n = int(input("Enter a int number = "))

    print(print_numbers(n))