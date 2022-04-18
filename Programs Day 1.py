print("Pattern A".center(40, "-"))
#1 Patterns
n=int(input("ENTER THE NUMBERS OF ROWS :"))
num=1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num=num+1
    print()

print("Pattern B".center(40, "-"))

# Patterns
for i in range(6):
    for j in range(i):
        print(i, end="")
    print('')



print("Pattern C".center(40, "-"))

#3 Patterns

for i in range(1,6):
    for k in range(7-i,1,-1):
        print(" ",end="")
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
for i in range(4,0,-1):
    for k in range(7-i,1,-1):
        print(" ",end="")
    for j in range(1,i+1):

        print(j, end=" ")

    print()

print("Fibonacci".center(40, "-"))

#2Fibonacci
a=0
b=1
for i in range(10):
    c=a+b
    a=b
    b=c
    print(c)


print("Pascals Triangle".center(40, "-"))

# Pascal's Triangle
num = int(input("Enter the number: "))
list1 = []
for i in range(num):
  list1.append([])
  list1[i].append(1)
  for j in range(1, i):
    list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
  if(num != 0):
    list1[i].append(1)
for i in range(num):
  print(" " * (num - i), end = " ", sep = " ")
  for j in range(0, i + 1):
    print('{0:6}'.format(list1[i][j]), end = " ", sep = " ")
  print()

print("Greedy".center(40, "-"))

#Greedy
cntr = 0
j = 1
while cntr < 6:
    num = j
    flag = False
    lst = []
    for i in range(3):
        if (num - 1) % 3 == 0:
            res = (num - 1) // 3 + 1
            lst.append(res)
            num = num - res
            if i == 2:
                flag = True
        else:
            break
    if flag and num and num % 3 == 0:
        print("Total {} -->  remaining {} --> father distributes {} to each daughter".format(j, num, num//3))
        print("\t\tDaughter #1 --> {}\n\t\tDaughter #2 -->{}\n\t\tDaughter #3 --> {}".format(lst[0], lst[1], lst[2]))
        cntr += 1
    j += 1








