# f1 = open("sample.txt", 'w')
# f1.write("70\n")
# f1.write("60\n")
# f1.write("55\n")
# f1.write("75\n")
# f1.write("95\n")
# f1.write("90\n")
# f1.write("80\n")
# f1.write("80\n")
# f1.write("85\n")
# f1.write("100\n")
# f1.close()
#
# with open ("sample.txt", 'r') as f1 :
#     with open("result.txt", 'w') as f2 :
#         result = 0
#         count = 0
#
#
#         for x in f1.readlines() :
#           result += int(x)
#           count += 1
#
#         f2.write(str(result/count))

# class Calculator :
#     def __init__(self):
#         self.result = 0
#
#     def adder(self, num):
#         self.result += num
#         return self.result
#
# Car1 = Calculator()
# Car2 = Calculator()
#
# print(Car1.adder(3))
# print(Car2.adder(5))
# print(Car1.adder(7))
# print(Car2.adder(4))
# print(Car1.adder(8))

#
# class Calculator :
#     def __init__(self, name):
#         self.result = 0
#         self.temp = 0
#         self.name = name
#
#     def adder(self, num):
#         self.result += num
#         print("%s계산기의 %f + %f의 값은 %f입니다." %( self.name, self.temp ,num, self.result))
#         self.temp = self.result
#
#
#     def substractor(self, num):
#         self.result -= num
#         print("%s계산기의 %f - %f의 값은 %f입니다." %( self.name, self.temp, num, self.result))
#         self.temp = self.result
#
#
#     def multiplier(self, num):
#         self.result *= num
#         print("%s계산기의 %f * %f의 값은 %f입니다." %( self.name, self.temp, num, self.result))
#         self.temp = self.result
#
#     def divisioner(self, num):
#         self.result /= num
#         print("%s계산기의 %f / %f의 값은 %f입니다." %( self.name, self.temp, num, self.result))
#         self.temp = self.result
#
# name = input("계산기 이름 입력")
# cal1 = Calculator(name)
#
# while 1 :
#     x = int(input("숫자입력"))
#     a = int(input("연산 종류 1:더하기, 2:빼기, 3:곱하기, 4:나누기, 5:종료"))
#     if a == 1 : cal1.adder(x)
#     if a == 2 : cal1.substractor(x)
#     if a == 3 : cal1.multiplier(x)
#     if a == 4 : cal1.divisioner(x)
#     if a == 5 : break

# treehit = 0
#
# while treehit < 10 :
#     treehit += 1
#     print("나무를 %d번 찍습니다." %treehit)
#     if(treehit == 10) : print("나무가 넘어갑니다")

class Housepark :
    lastname = "박"

pey = Housepark()
print(pey.lastname)
Housepark.lastname = "창씨개명" #클래스의 요소를 그대로 받았을 때는 클래스의 요소가 바뀌면 자식들도 자동으로 바뀜
pes = Housepark()
print(pes.lastname)
print((pey.lastname))
pey.lastname = "박" #직접 값을 때려박으면 바뀌지 않음
print(pes.lastname)
print((pey.lastname))
Housepark.lastname = "창씨개명"
print((pey.lastname))

# class Housepark :
#     lastname = '박'
#
#     def __init__(self, name):
#         self.fullname = self.lastname + name
#
#     def travel(self, destination):
#         self.destination = destination
#         print("%s은(는) %s로 여행을 가고싶다" %(self.fullname, destination))
#
#     def __add__(self, other):
#         print("%s과 %s은(는) 각자의 여행지 %s와 %s에서 텔레파시로 의사소통을 했다." \
#               %(self.fullname, other.fullname, self.destination, other.destination))
#
# pey = Housepark("응용")
# print(pey.fullname)
# pey.travel("안드로메다")
#
# class HouseKim(Housepark) :
#     lastname = "김"
#
#     def travel(self, destination, days):
#         self.destination = destination
#         print("%s은(는) %s로 %d일 동안 여행을 가고싶어 한다." %(self.fullname, destination, days))
#
# pes = HouseKim("줄리엣")
# pes.travel("깐따삐아", 5)
#
# pey + pes

# from mod1 import *
#
# a = int(input("숫자입력 :"))
# b = int(input("숫자입력 :"))
# print(sum_safe(a,b))
# print(sum_safe('vb',1))

# class Bird :
#     def fly(self):
#         raise Birdshouldhavawings
#
# Jickparkguri = Bird()
# try :
#     Jickparkguri.fly()
# except NameError as x :
#     print(x)

