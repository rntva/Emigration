import Make_Academy_class
from Managing_Academies.Curriculums.Make_Curiculum_class import *

while 1 :
    order_1 = input("학원관리스스템을 실행하시겠습니까?(1:예, 2:아니오)")
    if order_1 == "2" : break
    elif order_1 == "1" :
        temp_acafunc = Make_Academy_class.academies()
        while 1 :
            order_2 = input("학원정보를 입력하시겠습니까?(1:예, 2:아니오) : ")
            if order_2 == "1" :
                academy_info = input("학원 정보를 입력해 주십시오.\n이름,번호,주소,웹주소,과정명(,) : ")
                academy_info = academy_info.split(' ')
                temp_info = Make_Academy_class.academy_information(academy_info[0], academy_info[1], academy_info[2],\
academy_info[3], academy_info[4])
                temp_acafunc.make_academy(temp_info)
            elif order_2 == "2" : break
        while 1 :
            order_3 = input("학원정보들을 검색하시겠습니까?(1:예, 2:아니오) : ")
            if order_3 == "1" : temp_acafunc.serch_academy_info()
            elif order_3 == "2" : break
        while 1 :
            order_4 = input("각 과정의 정보를 입력?")
            if order_4 == "아니오" : break
            elif order_4 == "예" :
                curriculum_info_tutors = {}
                curriculum_info_students = {}
                curriculum_info = input("과정 정보를 입력.\n학원,이름,수업시간").split(' ')



