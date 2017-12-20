import pickle
import os

class curriculum_information() :
    def __init__(self, name, tutors, time, students) :
        self.name = name
        self.tutors = tutors
        self.time = time
        self.students = students

def print_all_curriculmums_info() :
    listdir_name = os.listdir("..\\..\\Academies")
    for x in listdir_name:
        for y in os.listdir("..\\..\\Academies\\" + x):
            file = open("..\\..\\Academies\\" + x + "\\" + y, 'rb')
            try:
                temp = pickle.load(file)
                print("학원명 : %s" % x)
                print("과정명 : %s" % temp.name)
                print("강사진 : ", end='')
                print(temp.tutors)
                print("수업시간 : %s" % temp.time)
                print("학생들 : ", end='')
                print(temp.students, end="\n\n")
            except:
                pass

def print_all_curriculums_name() :
    listdir_name = os.listdir("..\\..\\Academies")
    for x in listdir_name:
        curr_name = os.listdir("..\\..\\Academies\\" + x)
        for y in curr_name:
            print("학원명 : %s - 과정명 : " % x, end='')
            print(y.split('.')[0])

def search_curriculum(searching_curriculum_name) :
    listdir_name = os.listdir("..\\..\\Academies")
    token = 0
    for x in listdir_name:
        try:
            file = open("..\\..\\Academies\\" + x + "\\" + searching_curriculum_name + ".bin", 'rb')
            temp = pickle.load(file)
            print("학원명 : %s" % x)
            print("과정명 : %s" % temp.name)
            print("강사진 : ", end='')
            print(temp.tutors)
            print("수업시간 : %s" % temp.time)
            print("학생들 : ", end='')
            print(temp.students, end="\n")
            file.close()
            token = 1
            continue
        except FileNotFoundError:
            continue
        except EOFError:
            pass
    if token == 0: print("찾는 과정(%s)이 없거나 내부정보가 없습니다." %searching_curriculum_name)

def delet_curriculum(deleting_academy_name, deleting_curriculum_name) :
    try:
        os.unlink("..\\..\\Academies\\" + deleting_academy_name + "\\" + deleting_curriculum_name + ".bin")
    except FileNotFoundError:
        print("해당 학원 혹은 과정이 없습니다.")

def update_curriculum(academy_name, instance) :
    try :
        file = open("..\\..\\Academies\\"+academy_name+"\\"+instance.name+".bin", 'rb')
        judge = input("파일이 존재합니다. 덮어 쓰시겠습니까?(1:예 2:아니오")
        if judge == '2' :
            file.close()
            pass
        elif judge == '1' :
            file = open("..\\..\\Academies\\"+academy_name+"\\"+instance.name+".bin", 'wb')
            pickle.dump(instance, file)
            file.close()
    except FileNotFoundError :
        file = open("..\\..\\Academies\\"+academy_name+"\\"+instance.name+".bin", 'wb')
        pickle.dump(instance, file)
        file.close()