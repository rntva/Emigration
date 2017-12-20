import pickle
import os

class academy_information() :
    def __init__(self, name, number, address, web_address, curriculums) :
        self.name = name
        self.number = number
        self.address = address
        self.web_address = web_address
        self.curriculums = curriculums

def print_all_academies_info() :
    try:
        file = open("..\\..\\Academies.bin", 'rb')
        while 1:
            try:
                temp = pickle.load(file)
                print("학원이름 : %s" % temp.name)
                print("전화번호 : %s" % temp.number)
                print("주소 : %s" % temp.address)
                print("홈페이지 : %s" % temp.web_address)
                print("교육과정 : %s" % temp.curriculums)
            except:
                break
    except FileNotFoundError:
        print("Academies.bin 파일이 없습니다.")

def print_all_academies_name() :
    try:
        file = open("..\\..\\Academies.bin", 'rb')
        numbering = 1
        while 1:
            try:
                temp = pickle.load(file)
                print("%d.학원 : %s" % (numbering, temp.name))
                numbering += 1
            except:
                break
    except FileNotFoundError:
        print("Academies.bin 파일이 없습니다.")

def search_academy(searching_academy_name) :
    try:
        file = open("..\\..\\Academies.bin", 'rb')
        while 1:
            try:
                temp = pickle.load(file)
                if temp.name == searching_academy_name:
                    print("학원이름 : %s" % temp.name)
                    print("전화번호 : %s" % temp.number)
                    print("주소 : %s" % temp.address)
                    print("홈페이지 : %s" % temp.web_address)
                    print("교육과정 : %s" % temp.curriculums)
                    break
            except:
                print("찾으시는 학원(%s)이 없습니다." % searching_academy_name)
                break
    except FileNotFoundError:
        print("Academies.bin 파일이 없습니다.")

def delet_academy(deleting_academy_name) :
    try:
        file = open("..\\..\\Academies.bin", 'rb')
        file_copy = open("..\\..\\Academies_copy.bin", 'wb')
        token = "없다"
        while 1 :
            try :
                temp = pickle.load(file)
                if temp.name == deleting_academy_name :
                    try:
                        os.rmdir("..\\..\\Academies\\" + deleting_academy_name)
                        token = "지웠다"
                    except OSError as e_msg:
                        print(e_msg)
                        judge = input("상관없이 다 지우시겠습니까?(1:예 2:아니오) : ")
                        if judge == '2' : token = "안지웠다"
                        elif judge == '1' :
                            dirlist = os.listdir("..\\..\\Academies\\" + deleting_academy_name)
                            for x in dirlist :
                                os.unlink("..\\..\\Academies\\" + deleting_academy_name + "\\" + x)
                            os.rmdir("..\\..\\Academies\\" + deleting_academy_name)
                            token = "지웠다"
                else : pickle.dump(temp, file_copy)
            except :
                if token == "없다" :
                    print("%s라는 학원이 없습니다." %deleting_academy_name)
                    file.close()
                    file_copy.close()
                    os.unlink("..\\..\\Academies_copy.bin")
                    break
                elif token == "안지웠다" :
                    file.close()
                    file_copy.close()
                    os.unlink("..\\..\\Academies_copy.bin")
                    break
                elif token == "지웠다" :
                    file.close()
                    file_copy.close()
                    os.unlink("..\\..\\Academies.bin")
                    os.rename("..\\..\\Academies_copy.bin", "..\\..\\Academies.bin")
                    break
    except FileNotFoundError:
        print("Academies.bin 파일이 없습니다.")

def make_academy(instance) :
    try :
        if instance.name != "!@#$" :
            os.mkdir("..\\..\\Academies\\"+instance.name)
            for x in str(instance.curriculums).split(' ') :
                try :
                    ffile = open("..\\..\\Academies\\"+instance.name+"\\"+x+".bin", 'rb')
                    ffile.close()
                except FileNotFoundError :
                    ffile = open("..\\..\\Academies\\"+instance.name+"\\"+x+".bin", 'wb')
                    ffile.close()
        try :
            file = open("..\\..\\Academies.bin", 'rb')
            file.close()
            file = open("..\\..\\Academies.bin", 'ab')
            pickle.dump(instance, file)
            file.close()
        except FileNotFoundError :
            file = open("..\\..\\Academies.bin", 'wb')
            pickle.dump(instance, file)
            file.close()
    except FileExistsError :
        print("%s라는 학원은 이미 생성되었습니다." %instance.name)