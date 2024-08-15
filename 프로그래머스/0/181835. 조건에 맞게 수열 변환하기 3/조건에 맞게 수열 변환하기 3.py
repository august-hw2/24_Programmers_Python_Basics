def solution(arr, k):
    if k%2: #홀수일 때
        return [i*k for i in arr]
    else: #짝수일 때
        return [i+k for i in arr]
    