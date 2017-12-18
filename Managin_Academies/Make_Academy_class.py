import pickle

class academy_information() :
    def __init__(self, name, number, address, web_address, curiculums) :
        self.name = name
        self.number = number
        self.address = address
        self.web_address = web_address
        self.curiculums = curiculums

class academies() :
    def serch_academy_info(self):
        order = input("검색 옵션을 설정해 주십시오.\n1.학원전체정보출력 2.학원명만출력 3.학원찾기 : ")
        try :
            file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\\Academies.bin", 'rb')
        except FileNotFoundError :
            print("파일이 없습니다.")
            exit()

        if order == '1' :
            while 1 :
                temp = pickle.load(file)
                if temp.name == "!@#$" : break
                else :
                    print("학원이름 : %s" %temp.name)
                    print("전화번호 : %s" %temp.number)
                    print("주소 : %s" %temp.address)
                    print("홈페이지 : %s" %temp.web_address)
                    print("교육과정 : %s" %temp.curiculums)
        elif order == '2' :
            while 1 :
                temp = pickle.load(file)
                if temp.name == "!@#$" : break
                else :
                    print("학원이름 : %s" %temp.name)
        elif order == '3' :
            serch_academy_name = input("학원 이름을 치세요. : ")
            while 1 :
                temp = pickle.load(file)
                if temp.name == "!@#$" :
                    print("찾으시는 학원(%s)이(가) 없습니다." %serch_academy_name)
                    break
                elif temp.name == serch_academy_name :
                    print("학원이름 : %s" % temp.name)
                    print("전화번호 : %s" % temp.number)
                    print("주소 : %s" % temp.address)
                    print("홈페이지 : %s" % temp.web_address)
                    print("교육과정 : %s" % temp.curiculums)
        file.close()

    def make_academy(self, instance) :
        file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\\Academies.bin", 'ab')
        pickle.dump(instance, file)

if __name__ == "__main__" :
    a = academy_information("한국it교육원a", "어느시 어느동 어느번지a", "0532456653a",\
"www.gkit.coma", "이거,저거,요거,많이a")
    b = academy_information("한국it교육원b", "어느시 어느동 어느번지b", "0532456653b",\
"www.gkit.comb", "이거,저거,요거,많이b")
    c = academy_information("한국it교육원c", "어느시 어느동 어느번지c", "0532456653c",\
"www.gkit.comc", "이거,저거,요거,많이c")
    last = academy_information("!@#$", "어느시 어느동 어느번지last", "0532456653last",\
"www.gkit.comlast", "이거,저거,요거,많이last")

test = academies()
# test.make_academy(a)
# test.make_academy(b)
# test.make_academy(c)
# test.make_academy(last)

test.serch_academy_info()