import pickle

class academies() :

    def serch(self):
        order = input("검색 옵션을 설정해 주십시오.\n1.학원전체정보출력 2.학원명만출력 3.학원찾기 : ")
        file = open("D:\\Pycharm_projects\\Emigration\\Managin_Academies\\Academies.bin", 'rb')
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
                    break
                elif temp.name == serch_academy_name :
                    print("학원이름 : %s" % temp.name)
                    break

    def make_academy(self, name, number, address, web_address, curiculums) :
        self.name = name
        self.numberm = number
        self.address = address
        self.web_address = web_address
        self.curiculums = curiculums


academies.serch()