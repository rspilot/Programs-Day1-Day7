#1
print("1Ans".center(40, "-"))

d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50,6:60}
d4={}
print(f"d4 :{d4}")
d4.update(d1)
print(f"d4 After Result :{d4}")
d4.update(d2)
print(f"d4 After Result :{d4}")
d4.update(d3)
print(f"d4 After Result:{d4}")

print("3Ans".center(40, "-"))

#3
d={'a)':1,'b)':2,'c)':3,'d)':4}
for key,value in d.items():
    print(key,value)


print("4Ans".center(40, "-"))

#4
N = 5
d = {}
for i in range(1, N + 1):
    d[i] = i * i
print(f"d  :{d}")

print("5Ans".center(40, "-"))

#5
d1 = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20, 'F': 15}
temp = []
result = dict()
for key, value in d1.items():
    if value not in temp:
        temp.append(value)
        result[key] = value
print(f"result :{result}")

print("6Ans".center(40, "-"))

#6
Sample = {'a' : 11, 'b' : 2, 'c' : 11, 'd':8, 'e':1}
print(f"Key:{min(Sample, key = Sample.get)}")

print("7Ans".center(40, "-"))

#7
list = [1,2,3,4,5,6,7,8,9]
list.reverse()
print(list)


print("8Ans".center(40, "-"))
#8
L1 = [1,2,3,4,5,6]
L1.remove(2)
print(f"After Removing  :{L1}")


print("9Ans".center(40, "-"))

#9
A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = sum(A)
print(f"sum : {sum}")

print("10Ans".center(40, "-"))

#10
list = [20, 30, 40, 25, 10,60,50,55]
list.sort()
print(f"Second Largest :{list[-2]}")

print("11Ans".center(40, "-"))

#11
list = [20, 30, 40, 25, 10,60,50,55]
list.sort()
print(f"Second Smallest :{list[1]}")

print("13Ans".center(40, "-"))

#13
list = [20, 20, 40, 25, 20, 60, 50 , 60]
print(f"Count :{list.count(20)}")

print("14Ans".center(40, "-"))

#14
list1 = [1,2,3,4,5,6]
list2 = [4,7,6,3,8,9]
res= set(list1).intersection(set(list2))
print(f"res :{res}")

print("15Ans".center(40, "-"))

#15
def list_count(L):
    return len(L)
L= [[1, 2], [3, 4, 6], [5, 7], [9, 10, 11] ,[8, 12 ,20]]
print(f"Common Count :{list_count(L)}")










