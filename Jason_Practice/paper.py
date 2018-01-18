import pickle
import json

name = "name"
age = "age"
address = "address"
class_info = "class_info"
p_registration = "p_registration"
attending_class = "attending_class"
c_name = "c_name"
c_tutor = "c_tutor"
c_open = "c_open"
c_close = "c_close"

def input_student_info_form_of_dic(primary_index_list) :
    primary_key = primary_index_list.pop()
    student_name = input("학생의 이름을 입력하십시오. : ")
    student_age = input("학생의 나이를 입력하십시오. : ")
    student_address = input("학생의 주소를 입력하십시오. : ")
    student_past_registration_times = input("학생의 과거 수강 횟수를 입력하십시오. : ")
    returned_result = \
        {
            primary_key:
                {
                    name: student_name, age: student_age, address: student_address,
                    class_info:
                        {
                            p_registration: student_past_registration_times,
                            attending_class: {}
                        }
                }
        }
    while 1 :
        order_1 = input("현재 수강 과목 정보를 추가하시겠습니까?(1:입력 2:무시) : ")
        if order_1 == '2' : break
        elif order_1 == '1' :
            student_attending_class_code = input("학생이 수강중인 강의코드를 입력하십시오.(강의코드 알파벳 2자리 + 개강 년월일 6자리)\n\
e.g)IB171106 : ")
            student_attending_class_name = input("학생이 수강중인 강의명을 입력하십시오.\n\
e.g)IoT 빅테이터 실무반 : ")
            student_attending_class_tutor = input("학생이 수강중인 강의의 강사명을 입력하십시오.\n\
e.g)이현구 : ")
            student_attending_class_open_date = input("학생이 수강중인 강의의 개강날짜들을 입력하십시오.\n\
e.g)2017-11-06 : ")
            student_attending_class_close_date = input("학생이 수강중인 강의의 종강날짜들을 입력하십시오.\n\
e.g)2018-09-05 : ")
            returned_result[primary_key][class_info][attending_class][student_attending_class_code] = \
            {
                "c_name" : student_attending_class_name,
                "c_tutor" : student_attending_class_tutor,
                "c_open" : student_attending_class_open_date,
                "c_close" : student_attending_class_close_date
            }
    return returned_result

def show_student_info(saved_primary_key_index, saved_primary_key) :
    print("<학생정보>")
    print("-학생이름 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][name])
    print("-학생나이 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][age])
    print("-학생주소 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][age])
    print("-과거수강정보")
    print(">>과거수강횟수 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][class_info][p_registration])
    temp_attending_class_keys_list = list(json_big_data[saved_primary_key_index][saved_primary_key][class_info][attending_class].keys())
    for y in temp_attending_class_keys_list:
        print(">>현재수강과목코드 : %s" % y)
        print(">>현재수강강의이름 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][class_info][attending_class][y][c_name])
        print(">>현재수강강의교사 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][class_info][attending_class][y][c_tutor])
        print(">>현재수강강의개강 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][class_info][attending_class][y][c_open])
        print(">>현재수강강의종강 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][class_info][attending_class][y][c_close])
        print()

def get_student_primary_key_list() :
    temp_student_primary_key_list = []
    for x in range(len(json_big_data)):
        temp_student_primary_key_list.append([x, list(json_big_data[x].keys())[0]])
    return temp_student_primary_key_list

def show_all() :
    for x in student_primary_key_list :
        show_student_info(x[0], x[1])
        print("------------------------------------------------------------------------")
    return None

def search_with_student_primary_key(primary_key) :
    for x in student_primary_key_list :
        if primary_key == x[1] :
            show_student_info(x[0],x[1])
            return None

# def check_codition(stored_data, inputted_data) :
#     divide_stored_data = list(str(stored_data))
#     divide_inputted_data = list(str(inputted_data))


def search_with_name(student_name) :
    searched_student_name_list = []
    for x in student_primary_key_list :
        if student_name == json_big_data[x[0]][x[1]][name] :
            searched_student_name_list.append(x)
    if len(searched_student_name_list) == 1 : show_student_info(searched_student_name_list[0][0],
                                                                searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1 :
        for x in searched_student_name_list :
            print(x[1])
    return None

def search_with_age(student_age) :
    searched_student_name_list = []
    for x in student_primary_key_list :
        if student_age == json_big_data[x[0]][x[1]][age] :
            searched_student_name_list.append(x)
    if len(searched_student_name_list) == 1 : show_student_info(searched_student_name_list[0][0],
                                                                searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1 :
        for x in searched_student_name_list :
            print(x[1])
    return None

def search_with_address(student_address) :
    searched_student_name_list = []
    for x in student_primary_key_list:
        if student_address == json_big_data[x[0]][x[1]][age]:
            searched_student_name_list.append(x)
    if len(searched_student_name_list) == 1: show_student_info(searched_student_name_list[0][0],
                                                               searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1 :
        for x in searched_student_name_list :
            print(x[1])
    return None

def search_with_past_registrarion(student_ragistrantion) :
    searched_student_name_list = []
    for x in student_primary_key_list :
        if student_ragistrantion == json_big_data[x[0]][x[1]][class_info][p_registration] :
            searched_student_name_list.append(x)
    if len(searched_student_name_list) == 1 : show_student_info(searched_student_name_list[0][0],
                                                                searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1 :
        for x in searched_student_name_list :
            print(x[1])
    return None

def search_with_now_studying() :
    searched_student_name_list = []
    for x in student_primary_key_list :
        if list(json_big_data[x[0]][x[1]][class_info][attending_class].keys()) != [] :
            searched_student_name_list.append(x)
    if len(searched_student_name_list) == 1:
        show_student_info(searched_student_name_list[0][0],
                          searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1:
        for x in searched_student_name_list:
            print(x[1])
    elif searched_student_name_list == [] : print("수강중인 학생이 없습니다.")
    return None

def search_with_opended_class(class_name) :
    searched_student_name_list = []
    for x in student_primary_key_list:
        student_class_code_list = list(json_big_data[x[0]][x[1]][class_info][attending_class].keys())
        for y in student_class_code_list :
            if json_big_data[x[0]][x[1]][class_info][attending_class][y][c_name] == class_name :
                searched_student_name_list.append(x)
                break
    if len(searched_student_name_list) == 1:
        show_student_info(searched_student_name_list[0][0],
                          searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1:
        for x in searched_student_name_list:
            print(x[1])
    elif searched_student_name_list == []:
        print("수강중인 학생이 없습니다.")
    return None

def search_with_tutor(tutor_name) :
    searched_student_name_list = []
    for x in student_primary_key_list:
        student_class_code_list = list(json_big_data[x[0]][x[1]][class_info][attending_class].keys())
        for y in student_class_code_list:
            if json_big_data[x[0]][x[1]][class_info][attending_class][y][c_tutor] == tutor_name:
                searched_student_name_list.append(x)
                break
    if len(searched_student_name_list) == 1:
        show_student_info(searched_student_name_list[0][0],
                          searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1:
        for x in searched_student_name_list:
            print(x[1])
    elif searched_student_name_list == []:
        print("수강중인 학생이 없습니다.")
    return None

def delet_with_student_primary_key(primary_key) :
    for x in student_primary_key_list :
        if primary_key == x[1] :
            del(json_big_data[x[0]])
            return None

# def update_student_info(student_id) :





########################################################################################################################

json_file_name = "ITT_Student.json"
json_big_data = []
left_primary_key_index_list = []
student_primary_key_list = []

try :
    with open(json_file_name, encoding='UTF8') as json_file :
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        student_primary_key_list = get_student_primary_key_list()
        show_all()
        # search_with_student_primary_key("ITT002")
        # search_with_name("김상엽")
        # search_with_age("ㅁ")
        # search_with_address("ㅁ")
        # search_with_past_registrarion("ㅂ")
        # search_with_now_studying()
        # search_with_opended_class('a')
        # search_with_tutor("이현구")
        delet_with_student_primary_key("ITT002")
        student_primary_key_list = get_student_primary_key_list()
        show_all()


except FileNotFoundError :
    file_not_found = input("%s파일이 없습니다. 다음 동작을 선택해 주십시오.(1:신규생성 2:경로설정) : " %json_file_name)
    if file_not_found == '2' :
        with open(json_file_name, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
    if file_not_found == '1' :
        with open("json_primary_code_sort.txt", 'wb') as index_file:
            temp_str = ""
            for x in range(1, 1000):
                temp_str += "ITT" + "{0:0>3}".format(str(x)) + '\n'
            index_list = list(reversed(temp_str[:-1].split('\n')))
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                json_big_dict = []
                while 1 :
                    order_1 = input("학생정보를 추가하시겠습니까?(1:예 2:아니오) : ")
                    if order_1 == '2' : break
                    elif order_1 == '1' : json_big_dict.append(input_student_info_form_of_dic(index_list))
                jsonResult = json_big_dict[:]
                readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json SAVED')
            pickle.dump(index_list, index_file)

    else :
        print("동작 선택 좀 똑디 하소.")
print("프로그램 종료")