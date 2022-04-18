print("Identity Matrix".center(40, "-"))
#1 Identity Matrix
def Matrix(size):
    for row in range(0, size):
        for col in range(0, size):
            if (row == col):
                print("0 ", end=" ")
            else:
                print("0 ", end=" ")
        print()
size = 4
Matrix(size)

print("Armstrong".center(40, "-"))
# Armstrong
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        if num == sum:
            print(num)