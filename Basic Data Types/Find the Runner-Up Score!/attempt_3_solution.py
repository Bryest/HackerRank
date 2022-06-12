n = int(input())
arr = list(map(int, input().split()))


def HighValue(arrNum):
    high = None
    aux = arrNum[0]
    for i in range(n):
        if aux < arrNum[i]:
            aux = arrNum[i]
        high = aux
    return high


def SecondHighValue(arrNum, arrBool):
    for i in range(len(arrBool)):
        if arrBool[i] != True:
            aux = arrNum[i]

    high = None

    for i in range(n):
        if aux < arrNum[i] and arrBool[i] != True:
            aux = arrNum[i]
        high = aux
    return high


def HighValuePositions(maxNum, arrBool, arrNum):
    for i in range(n):
        if arrNum[i] == maxNum:
            arrBool[i] = True


FirstMaximum = None
arrBool = list(bytearray(n))

FirstMaximum = HighValue(arr)
HighValuePositions(FirstMaximum, arrBool, arr)
SecondMaximum = SecondHighValue(arr, arrBool)

print(SecondMaximum)
