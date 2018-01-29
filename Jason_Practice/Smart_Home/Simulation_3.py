import urllib.request
import datetime
import json

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False

accesskey = "R9tidMCdl2pvpCuE0n4%2Fh%2FcPJIqFtgn3Vvp6UmSAWEpTQ4GbAwJ8n4O7IGhux4Vcm49bSCh64Md81lSPvY4dTQ%3D%3D"

def get_request_url(url) :
    req = urllib.request.Request(url) #Request를 쓰면 프로토콜 레벨에서 채워질 값이 들어간다.

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print("[%s] Url Request Successed" %datetime.datetime.now())
            return response.read().decode("utf-8")
    except Exception as e :
        print(print("[%s] Url Request Failed" % datetime.datetime.now()))
        print(e)
        return None

def get_weather_history_info(x_coordinate, y_coordinate, base_date, base_time) :
    basic_request_url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json"
    parameters += "&ServiceKey=" + accesskey
    parameters += "&nx=" + x_coordinate
    parameters += "&ny=" + y_coordinate
    parameters += "&base_date=" + base_date
    parameters += "&base_time=" + base_time

    final_request_url = basic_request_url + parameters
    retData = get_request_url(final_request_url)

    if retData == None : return None
    else : return json.loads(retData)

def process_weather_info() :
    now_date = datetime.datetime.now()
    base_date = str(now_date.year) + "{0:0>2}".format(str(now_date.month)) + "{0:0>2}".format(str(now_date.day))
    if now_date.minute >= 45 :
        base_time = "{0:0>2}".format(str(now_date.hour)) + "{0:0>2}".format(str(now_date.minute))
    else :
        base_time = "{0:0>2}".format(str(now_date.hour - 1)) + "{0:0>2}".format(str(now_date.minute))

    jsonData = get_weather_history_info("89", "91", base_date, base_time)

    if jsonData["response"]["header"]["resultMsg"] == "OK" :
        for item in jsonData["response"]["body"]["items"]["item"] :
            name_of_coordinate = "대구광역시 동구 신암4동"
            jsonResult.append({"name" : name_of_coordinate,
                               "base_date" : item["baseDate"],
                               "base_time" : item["baseTime"],
                               "weather" : item["category"],
                               "forecast_data" : item["fcstDate"],
                               "forecast_time" : item["fcstTime"],
                               "weather_value" : item["fcstValue"]})

    return None

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")

def print_device_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("작동")
    else: print("정지")

def check_device_status():
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door

    check_device_status()

def get_realtime_weather_info():
    process_weather_info()


def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else:print("중지")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else: print("중지")
    elif menu_num == 3:
        get_realtime_weather_info()

print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                                 - 이현구 -")
jsonResult = []
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num ==2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 4):
        break