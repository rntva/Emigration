import pickle
import json

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
                    "name": student_name, "age": student_age, "address": student_address,
                    "class_info":
                        {
                            "p_registration": student_past_registration_times,
                            "atteding_class": {}
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
            returned_result[primary_key]["class_info"]["atteding_class"][student_attending_class_code] = \
            {
                "c_name" : student_attending_class_name,
                "c_tutor" : student_attending_class_tutor,
                "c_open" : student_attending_class_open_date,
                "c_close" : student_attending_class_close_date
            }
    return returned_result

def show_student_info(saved_primary_key_index, saved_primary_key) :
    print("<학생정보>")
    print("-학생이름 : %s" % json_big_data[saved_primary_key_index][saved_primary_key]["name"])
    print("-학생나이 : %s" % json_big_data[saved_primary_key_index][saved_primary_key]["age"])
    print("-학생주소 : %s" % json_big_data[saved_primary_key_index][saved_primary_key]["address"])
    print("-과거수강정보")
    print(">>과거수강횟수 : %s" % json_big_data[saved_primary_key_index][saved_primary_key]["class_info"]["p_registration"])
    temp_atteding_class_keys_list = list(json_big_data[saved_primary_key_index][saved_primary_key]["class_info"]["atteding_class"].keys())
    for y in temp_atteding_class_keys_list:
        print(">>현재수강과목코드 : %s" % y)
        print(">>현재수강강의이름 : %s" % json_big_data[saved_primary_key_index][saved_primary_key]["class_info"]["atteding_class"][y]["c_name"])
        print(">>현재수강강의교사 : %s" % json_big_data[saved_primary_key_index][saved_primary_key]["class_info"]["atteding_class"][y]["c_tutor"])
        print(">>현재수강강의개강 : %s" % json_big_data[saved_primary_key_index][saved_primary_key]["class_info"]["atteding_class"][y]["c_open"])
        print(">>현재수강강의종강 : %s" % json_big_data[saved_primary_key_index][saved_primary_key]["class_info"]["atteding_class"][y]["c_close"])
        print()

def get_student_primary_key_list() :
    for x in range(len(json_big_data)):
        student_primary_key_list.append([x, list(json_big_data[x].keys())[0]])
    return None

def show_all() :
    for x in range(len(student_primary_key_list)) :
        show_student_info(student_primary_key_list[x][0], student_primary_key_list[x][1])
        print("------------------------------------------------------------------------")
    return None

########################################################################################################################
json_file_name = "ITT_Student.json"
json_big_data = []
json_big_dict = []
left_primary_key_index_list = []
student_primary_key_list = []

try :
    with open(json_file_name, encoding='UTF8') as json_file :
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
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







# import json
# import pickle
#
# def input_student_info_form_of_dic(primary_index_list) :
#     primary_key = primary_index_list.pop()
#     student_name = input("학생의 이름을 입력하십시오. : ")
#     student_age = input("학생의 나이를 입력하십시오. : ")
#     student_address = input("학생의 주소를 입력하십시오. : ")
#     student_past_registration_times = input("학생의 과거 수강 횟수를 입력하십시오. : ")
#     returned_result = \
#         {
#             primary_key:
#                 {
#                     "name": student_name, "age": student_age, "address": student_address,
#                     "class_info":
#                         {
#                             "p_registration": student_past_registration_times,
#                             "atteding_class": {}
#                         }
#                 }
#         }
#     while 1 :
#         order_1 = input("현재 수강 과목 정보를 입력메뉴입니다.(1:입력 2:무시) : ")
#         if order_1 == '2' : break
#         elif order_1 == '1' :
#             student_attending_class_code = input("학생이 수강중인 강의코드를 입력하십시오.(강의코드 알파벳 2자리 + 개강 년월일 6자리)\n\
# e.g)IB171106 : ")
#             student_attending_class_name = input("학생이 수강중인 강의명을 입력하십시오.\n\
# e.g)IoT 빅테이터 실무반 : ")
#             student_attending_class_tutor = input("학생이 수강중인 강의의 강사명을 입력하십시오.\n\
# e.g)이현구 : ")
#             student_attending_class_open_date = input("학생이 수강중인 강의의 개강날짜들을 입력하십시오.\n\
# e.g)2017-11-06 : ")
#             student_attending_class_close_date = input("학생이 수강중인 강의의 종강날짜들을 입력하십시오.\n\
# e.g)2018-09-05 : ")
#             returned_result[primary_key]["class_info"]["atteding_class"][student_attending_class_code] = \
#             {
#                 "c_name" : student_attending_class_name,
#                 "c_tutor" : student_attending_class_tutor,
#                 "c_open" : student_attending_class_open_date,
#                 "c_close" : student_attending_class_close_date
#             }
#     return returned_result
#
# def get_primaty_key_list() :
#     primary_keys = []
#     for x in json_big_data :
#          primary_keys.append(list(x.keys())[0])
#     return primary_keys
#
# def get_class_code_list(primary_keys) :
#     class_code_list = []
#     for x in range(len(primary_keys)) :
#         temp_key = list(json_big_data[x].keys())[0]
#         class_code_list.append(list(json_big_data[x][temp_key]["class_info"]["atteding_class"].keys()))
#     return class_code_list
#
# def search_with_primary_key(primary_keys, primary_key_input) :
#     if primary_keys.count(primary_key_input) == 1 :
#         for x in range(len(primary_keys)) :
#             try :
#                 print("<학생정보>")
#                 print("-학생이름 : %s" %json_big_data[x][primary_key_input]["name"])
#                 print("-학생나이 : %s" %json_big_data[x][primary_key_input]["age"])
#                 print("-학생주소 : %s" %json_big_data[x][primary_key_input]["address"])
#                 print("-과거수강정보")
#                 print(">>과거수강횟수 : %s" %json_big_data[x][primary_key_input]["class_info"]["p_registration"])
#                 temp_atteding_class_keys_list = list(json_big_data[x][primary_key_input]["class_info"]["atteding_class"].keys())
#                 for y in temp_atteding_class_keys_list :
#                     print(">>현재수강과목코드 : %s" %y)
#                     print(">>현재수강강의이름 : %s" %json_big_data[x][primary_key_input]["class_info"]["atteding_class"][y]["c_name"])
#                     print(">>현재수강강의교사 : %s" %json_big_data[x][primary_key_input]["class_info"]["atteding_class"][y]["c_tutor"])
#                     print(">>현재수강강의개강 : %s" %json_big_data[x][primary_key_input]["class_info"]["atteding_class"][y]["c_open"])
#                     print(">>현재수강강의종강 : %s" %json_big_data[x][primary_key_input]["class_info"]["atteding_class"][y]["c_close"])
#                     print("------------------------------------------------------------------------")
#                 break
#             except KeyError : pass
#     return None
#
# def search_with_student_name(primary_keys, student_name_input) :
#     temp_name_keys_list = []
#     counting = 0
#     for x in range(len(primary_keys)) :
#         temp_key = list(json_big_data[x].keys())[0]
#         if json_big_data[x][temp_key]["name"] == student_name_input :
#             temp_name_keys_list.append([x, json_big_data[x][temp_key]])
#             counting += 1
#         else : pass
#     if counting == 1 :
#         print("<학생정보>")
#         print("-학생이름 : %s" % json_big_data[temp_name_keys_list[0]][temp_name_keys_list[1]]["name"])
#         print("-학생나이 : %s" % json_big_data[temp_name_keys_list[0]][temp_name_keys_list[1]]["age"])
#         print("-학생주소 : %s" % json_big_data[temp_name_keys_list[0]][temp_name_keys_list[1]]["address"])
#         print("-과거수강정보")
#         print(">>과거수강횟수 : %s" % json_big_data[temp_name_keys_list[0]][temp_name_keys_list[1]]["class_info"]["p_registration"])
#         temp_atteding_class_keys_list = list(json_big_data[temp_name_keys_list[0]][temp_name_keys_list[1]]["class_info"]["atteding_class"].keys())
#         print(">>현재수강과목코드 : %s" % y)
#         print(">>현재수강강의이름 : %s" % json_big_data[temp_name_keys_list[0]][temp_name_keys_list[1]]["class_info"]["atteding_class"][y]["c_name"])
#         print(">>현재수강강의교사 : %s" % json_big_data[temp_name_keys_list[0]][temp_name_keys_list[1]]["class_info"]["atteding_class"][y]["c_tutor"])
#         print(">>현재수강강의개강 : %s" % json_big_data[temp_name_keys_list[0]][temp_name_keys_list[1]]["class_info"]["atteding_class"][y]["c_open"])
#         print(">>현재수강강의종강 : %s" % json_big_data[temp_name_keys_list[0]][temp_name_keys_list[1]]["class_info"]["atteding_class"][y]["c_close"])
#         print("------------------------------------------------------------------------")
#     elif counting >= 2 :
#         for x in range(len(temp_name_keys_list)/2) :
#             print("%s" %temp_name_keys_list[x*2], end = '')
#         print("------------------------------------------------------------------------")
#     return None
#
#
#
#
#
# def search_student_info() :
#     searched_result = []
#     order_1 = input("1:dict전체정보출력 2:ID 3:이름 4:나이 5:주소 6:과거수강횟수 7:현재강의를수강하는학생 8:현재수강과목의강의명\
#  9:현재수강과목의강사 10:메인메뉴로 : ")
#
# json_file_name = "ITT_Student.json"
# json_big_data = []
# json_big_dict = []
# last_primary_key = ""
# index_list = []
#
# try :
#     with open(json_file_name, encoding='UTF8') as json_file :
#         json_object = json.load(json_file)
#         json_string = json.dumps(json_object)
#         json_big_data = json.loads(json_string)
#
# except FileNotFoundError :
#     file_not_found = input("%s파일이 없습니다. 다음 동작을 선택해 주십시오.\n1:신규생성 2:경로설정")
#     if file_not_found == '2' :
#         with open(json_file_name, encoding='UTF8') as json_file:
#             json_object = json.load(json_file)
#     if file_not_found == '1' :
#         with open("json_primary_code_sort.txt", 'wb') as index_file:
#             temp_str = ""
#             for x in range(1, 1000):
#                 temp_str += "ITT" + "{0:0>3}".format(str(x)) + '\n'
#             index_list = list(reversed(temp_str[:-1].split('\n')))
#             with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
#                 while 1 :
#                     order_1 = input("학생정보를 추가하시겠습니까?(1:예 2:아니오) : ")
#                     if order_1 == '2' : break
#                     elif order_1 == '1' : json_big_dict.append(input_student_info_form_of_dic(index_list))
#                 jsonResult = json_big_dict[:]
#                 readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
#                 outfile.write(readable_result)
#                 print('ITT_Student.json SAVED')
#             pickle.dump(index_list, index_file)
#     else :
#         print("동작 선택 좀 똑디 하소.")