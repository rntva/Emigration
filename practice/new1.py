"""
a = int(input())
b = int(input())
c = a + b
print(c)
"""

"""
dic = { 'a' : 1 , 'b' : 2, 'c' : 3 }
for k in dic.keys() :
    print(k)

b = 0
for i in range(1, 100) :
    b = b + i

print(b)
"""

"""
a = [1,2]

while a :
    b = int(input())
    c = int(input())
    print(b + c)
    a.pop()
"""

"""
a = {'name' : 'kim' , 'phone' : '010-0202-3030', 'birth' : '1929' }
print("type what you wanna search.")
b = input()
c = 1
for k in a.values() :
    if k in b : print("Ture")
    else : c = 0
if c == 0 : print("False")
"""

"""
print("How mouch money do you have?")

a = 5000
b = int(input())
c = 0;

if b >= a :
    print("You have enough money to take a texi.")
else :
    print("If you have any card, press '1'. If not, press'0'?")
    c = int(input())
    if c == 1 :
        print("You can take a texi.")
    else : 
        print("Walk to the destnation.")
"""

a = [10,10,10]
soldout = 1
e = 1
change = -1
while soldout :
    print("Welcome~! This is the newest banding meachine.")
    print("What kind of drink do you want?")
    print("Coffee : 1, Orange Juice : 2, Hot Choco : 3")
    b = int(input())
    if a[b-1] == 0 : 
        print("Sold out.")
    else :
        print("Plese insert coins.")
        c = int(input())
        change = c - 300
    if change >= 0 :  
        if (b == 1 and a[0] > 0) :
            a[0] = a[0] - 1
            print("Here is change %d." %change)
            # print(a[0])
        if b == 2 and a[1] > 0 :
            a[1] = a[1] - 1
            print("Here is change %d." %change)
            # print(a[1])
        if b == 3 and a[2] > 0 :
            a[2] = a[2] - 1
            print("Here is change %d." %change)
            # print(a[2])
    else : print("You didn't insert enough money.")

    print("Coffee : %d Orange Juice : %d Hot Choco : %d left\n" %(a[0], a[1], a[2]))

    if a[0] ==0 and a[1] == 0 and a[2] == 0 :
        print("Every drink is sold out. Sorry.")
        break

"""
score = {'aa' : 90, 'bb' : 44, 'cc' : 66, 'dd' : 78, 'ee' : 100}

for (i, k) in score.items() :
    print(i)
    if k >= 60 : print("Pass")
    else : print("Fail")
"""

"""
for x in range(5) :
    y = x + 1
    while y :
        print("*", end='')
        y = y - 1
    print()
"""

"""
i = 0
while True :
    i += 1
    if i > 5 : break
    print('*'* i)
"""

"""
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0  
for x in range(len(A)):
    total += A[x]
average = total / (x+1)
print(average)
"""

print("sum or nul")
coin = input()
arr = []
print("How many number?")
count = int(input())
x = count

while count :
    c = int(input())
    arr.append(c)
    count -= 1

def sum_mul(coin, x, arr) :
    result = 0
    if coin == "sum" :
        for y in range(x) :
            result += arr[y]
    elif coin == "nul" :
        for y in range(x) :
            result *= arr[y]
    return result

print(sum_mul(coin, x, arr))

"""
print("sum and nul")
arr = []
print("How many number?")
count = int(input())
x = count

while count :
    c = int(input())
    arr.append(c)
    count -= 1

def sum_mul(x, arr) :
    result1 = 0
    result2 = 1
    for y in range(x) :
        result1 += arr[y]
    for y in range(x) :
        result2 *= arr[y]
    return result1, result2

print(sum_mul(x, arr))
"""

"""
f = open("new1.txt", 'w')
for x in range(1,6) :
    f.write('*'*x)
    f.write('\n')
f.close()
"""

"""
f1 = open("new1.txt", 'r')
f2 = open("new1_copy.txt", 'w')

while 1 :
    line = f1.readline()
    if not line : break
    f2.write(line)

f1.close()
f2.close()
"""

"""
f1 = open("new1.txt", 'r')
f2 = open("new1_copy.txt", 'w')

line = f1.readlines()
for i in line : f2.write(i)

f1.close()
f2.close()
"""

"""
f1 = open("new1.txt", 'r')
f2 = open("new1_copy.txt", 'w')

line = f1.readlines()
a = 0
cc=10
while cc :
    if a >= len(line) : break
    f2.write(line[a])
    a += 1
    cc -= 1

f1.close()
f2.close()
"""

"""
f1 = open("new1_copy.txt", 'r')
f2 = open("new1_copy_copy.txt", 'w')

lines = f1.read()
f2.write(lines)

f1.close()
f2.close()
"""

"""
f1 = open("new1_copy_copy.txt", 'a')


for x in range(1,5) :
    f1.write("Add this line %d.\n" %x)

f1.close()
"""

"""
import sys

args = sys.argv[1:]

for x in args : print(x)
"""

"""
import sys

args = sys.argv[1:]

args.sort()
print(args)
"""

# print("This is function for Fibnacci Sequence")
#
# def fib(n) :
#     if n == 0 : return 0
#     if n == 1 : return 1
#     return fib(n-1) + fib(n-2)
#
# for x in range(10) :
#     print(fib(x))