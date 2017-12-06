a = [0,0]

def test(arr) :
    arr[0] += 1
    arr[1] += 2
    return arr

for x in range(1,10) :
    test(a)

print(a)