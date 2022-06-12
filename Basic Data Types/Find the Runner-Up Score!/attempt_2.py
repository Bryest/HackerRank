n = int(input())
arr = list(map(int, input().split()))


def Maximum(arrNum, arrBool):
    high = None
    aux = arrNum[0]
    for i in range(n):
        if len(arrBool) == 0:
            if aux < arrNum[i]:
                aux = arrNum[i]
            high = aux
        if len(arrBool) > 0:
            if aux == FirstMaximum:
                for i in range(n):
                    aux = arrBool
            if aux < arrNum[i] and arrBool[i] != True:
                if aux != FirstMaximum:
                    aux = arrNum[i]
            high = aux
    return high


def MaximumPositions(maxNum, arrBool, arrNum):
    for i in range(n):
        if arrNum[i] == maxNum:
            arrBool[i] = True


FirstMaximum = None
FirstMaximum = Maximum(arr, [])
arrBool = list(bytearray(n))
MaximumPositions(FirstMaximum, arrBool, arr)
SecondMaximum = Maximum(arr, arrBool)
print(SecondMaximum)
