def solution(arr):
    x = len(arr[0]) #가로 길이 = 열의 수
    y = len(arr) #세로 길이 = 행의 수
    temp = []

    if x > y: #열 > 행
        for i in range(x-y):
            for j in range(x):
                temp.append(0)
            arr.append(temp)
            temp = []

    elif x < y: #열 < 행
        for i in range(y):
            for j in range(y-x):
                arr[i].append(0)

    else: #열 = 행
        pass

    return arr