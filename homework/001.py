import numpy as np
def main():
    temp = []
    for i in range(21):
        temp.append(int(i))
    even = onlyEven(temp)
    three = threeMul(temp)
    print(np.array(temp))
    print(np.array(even))
    print(np.array(three))
def onlyEven(array):
    temp = []
    for i in array:
        if int(i) % 2 == 0:
            temp.append(i)
    return temp
def threeMul(array):
    temp = []
    for i in array:
        if int(i) % 3 == 0:
            temp.append(i)
    return temp

main()