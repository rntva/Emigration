# a = "janny hannah margot kevin min"
# list = a.split(' ')
# blank = ' '
# # import sys
#
# def greet_users(str_list) :
#     result = ""
#     for x in usernames :
#         temp2 = ""
#         temp = x
#         temp1 = temp[0].upper()
#         for y in temp[1:] :
#             temp2 = temp2 + str(y)
#             # result += temp2
#             # print("Hello, %s!" %(temp1+temp2))
#         result += temp1+ temp2 + ' '
#     result = result[:-1]
#     return result
#
# usernames = list
# for x in greet_users(usernames).split(' ') :
#     print("Hello, %s!" %x)
#
# import pickle
# file = open("refdf.txt", 'wb')
# data = "안녕하세요."
# for x in range(3) :
#     pickle.dump(data+str(x), file)
# file.close()
#
# file = open("refdf.txt", 'rb')
# for x in range(3) :
#     print(pickle.load(file))

# file = open("sample.txt", 'r')
# print(file.readlines()[-1])

# print("\\\\")

# A = input("아무거나 : ").split(' ')
# print(A)
#
# for x in  range(len(A)) :
#     if sorted(A[x]) == ['0','1','2','3','4','5','6','7','8','9'] : print(True, end = ' ')
#     else : print(False, end = ' ')

# list_n = [1,2,3,4,5]
# list_s = ['1','2','3','4','5']
# print("%d와 %s" %(list_n, list_s))
# # print(list_n, end = '')
# # print(list_s)

# import pickle
# class test():
#     name = "한국it교육원"
#     address = "어느시 어느동 어디어디"
#     number = "542234232"
#     classes = "융햡, 과정, 몰라, 그래, 알아"
# a = test()
# b = test()
# b.name = b.name+"bbbbb"
# b.address = b.address+"bbbbbb"
# b.number = b.number+"bbbbbbb"
# b.classes = b.classes+",bbbbbb"
# c = test()
# c.name = c.name+"ccccc"
# c.address = c.address+"cccccc"
# c.number = c.number+"ccccccc"
# c.classes = c.classes+",cccccc"
# d = test()
# d.name = d.name+"ddddd"
# d.address = d.address+"dddddd"
# d.number = d.number+"ddddddd"
# d.classes = d.classes+",dddddd"
# last = test()
# last.name = "!@#$"
#
# f = open("Academy.bin", 'wb')
# pickle.dump(a, f)
# pickle.dump(b, f)
# pickle.dump(c, f)
# pickle.dump(d, f)
# pickle.dump(last,f)
# f.close()

#
# f = open("test.bin", 'rb')
# e = pickle.load(f)
# print(e.name)
# ff = pickle.load(f)
# print(ff.name)
# g = pickle.load(f)
# print(g.name)
# h = pickle.load(f)
# print(h.name)
# print()
# print()
# print()
# print()

# f.seek(0)
# while 1 :
#     x = pickle.load(f)
#     if x.name == "한국it교육원ccccc" :
#         print(x.name)
#         break
#     else : pass
#
# f.close()


# f = open("test.bin", 'rb')
# ff = open("test_2.bin", 'wb')
# while 1 :
#     x = pickle.load(f)
#     if x.name == "!@#$" :
#         pickle.dump(x, ff)
#         break
#     elif x.name == "한국it교육원ccccc":
#         x.name = x.name + "awefdee"
#         x.address = x.address + "aefdfe"
#         pickle.dump(x, ff)
#     else : pickle.dump(x, ff)
# ff.close()
# ff = open("test_2.bin", 'rb')
# ff.seek(0)
# while 1 :
#     # print(pickle.load(ff))
#     x = pickle.load(ff)
#     if x.name == "!@#$" : break
#     else : print(x.name)
# f.close()
# ff.close()

# import os
#
# file_name = os.listdir()
# print(file_name)
# print(str(file_name))
# for x in file_name :
#     ext = x.split('.')
#     if ext[-1] == "bin" :
#         print(ext[0])

# curriculum_info_tutors = {}
# curriculum_info_tutors_input = input("강사명과 전화번호 입력 : ").split(' ')
# x = 0
# while 1 :
#     try :
#         if x >= len(curriculum_info_tutors_input) : break
#         else :
#             curriculum_info_tutors[curriculum_info_tutors_input[x]] = str(curriculum_info_tutors_input[x+1])
#             x += 2
#     except KeyError as e :
#         print(e)
#         break
# print(curriculum_info_tutors)
#
# file  = open("poll.txt", 'r')
# file.seek(0, 2)
# print(file.readline())

a = "0.444"
b = "0.445"
if a > b : print("a > b")
else : print("b > a")

a = "0.445"
b = "0.444"
if a > b : print("a > b")
else : print("b > a")