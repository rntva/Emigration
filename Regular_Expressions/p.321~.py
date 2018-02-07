import re
import os


p1 = re.compile(".+(?=:)")
p2 = re.compile(".+(?!:)")
print(p1.search(r"http://www.google.com").group())
print(p2.search(r"http://www.google.com").group())

test1 = re.compile(r".+[.](?!exe$|DBF$).+")
D_dir_list = os.listdir("D:\\")
print(D_dir_list)

for file_name in D_dir_list :
    if os.path.isfile("D:\\"+file_name) :
        if test1.search(file_name) != None :
            print(test1.search(file_name).group())
        elif test1.search(file_name) == None :
            print("%s는 .exe 또는 .DBF 파일이라 제외되었다." %file_name)