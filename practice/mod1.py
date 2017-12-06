# def sum(a, b) :
#     return a + b
#
# def sum_safe(a, b) :
#     if type(a) != type(b) :
#         print("연산할 수 없습니다.")
#         return
#     else :
#         return a + b
#
# if __name__ == "__main__" :
#     print(sum(3,5))
#     print(sum_safe(8,'a'))

PI = 3.141592
class Math :
    def resolve(self, r ):
        return PI * (r ** 2)

def sum(a, b ) :
    return a + b

if __name__ == "__main__" :
    print(PI)
    a = Math()
    print(a.resolve(2))
    print(sum(PI, 4.4))