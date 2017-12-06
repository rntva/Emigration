file1 = open("sample.txt", 'r')
file2 = open("result.txt", 'w')

for x in file1.readline():
    file2.write(x)
file2.write(file1.readline())

c = file1.tell() + 2
print(type(c))
file1.seek(0)
k = file1.readline()
file2.write(k[0])
print(file1.tell())
k = file1.readline()
file2.write(k)
# while 1 :
#     file1.seek(file1 + 2)

file1.close()
file2.close()
