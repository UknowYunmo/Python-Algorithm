# 1.두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.
print("강한친구 대한육군")
print("강한친구 대한육군")
# 2.두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
a,b=input().split()
a=int(a)
b=int(b)
print(a+b)
# 첫째줄에 여러개 입력을 동시에 받으려면 변수를 여러개 선언하구 스플릿으로 나눈다
# 3. 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
a, b=input().split()
a=int(a)
b=int(b)
print(a-b)
# 4.두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
a, b=input().split()
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
# 5.시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
a=int(input())
if a>=90 :
    print("A")
elif a>=80 :
    print("B")
elif a>=70 :
    print("C")
elif a>=60 :
    print("D")
else :
    print("F")
# 6.연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다.
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
a=int(input())
if a%4==0 :
    if a%400==0 :
        print(1)
    elif a%100==0 :
        print(0)
    else :
        print(1)
else :
    print(0)
# 7.점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
a=int(input())
b=int(input())
if a>0 :
    if b>0 :
        print(1)
    else :
        print(4)
else :
    if b>0 :
        print(2)
    else :
        print(3)
# 8.45분 일찍 알람 설정하기
# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.
h,m=input().split()
h=int(h)
m=int(m)
if m>=45 :
    m=m-45
else :
    m=m+15
    if h==0 :
        h=23
    else :
        h=h-1
print(h)
print(m)
