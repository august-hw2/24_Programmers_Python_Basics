user = input()
result = "" #문자열 선언

if 1 <= len(user) <= 20 and user.isalpha():
    for i in user:
        if 'a' <= i <= 'z':  # 소문자일 경우
            result += i.upper()
        elif 'A' <= i <= 'Z':  # 대문자일 경우
            result += i.lower()
    print(result)