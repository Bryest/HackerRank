n = int(input())
arr = list(map(int, input().split()))


def FirstMaximum(arrNum, arrBool):
    high = None
    aux = arrNum[0]
    for i in range(n):
        if aux > arrNum[i] and arrBool != True:
            high = aux
    return high


def SecondMaximum():
    for i in range(1, n):
        foo = FirstMaximum-arr[i]
        if arr[i] != FirstMaximum:
            if foo < FirstMaximum-arr[i]:
                high = arr[i]
            else:
                foo = FirstMaximum-arr[i]
    return high


FirstMaximum = FirstMaximum(arr,)
SecondMaximum = SecondMaximum()

print(FirstMaximum)
print(SecondMaximum)
