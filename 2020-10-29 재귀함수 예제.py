"""
재귀 함수를 이용해서 1부터 num까지의 곱이 출력되게 만들기
"""
def every(n):
    if n==1:
        return 1
    else:
        return n*every(n-1)
print(every(10))

"""
숫자가 있는 리스트가 주어졌을 때, 리스트의 합을 출력하는 재귀함수
"""
import random
case=random.sample(range(100),10) # 랜덤 리스트 만드는 함수!
sum=0
for i in range(len(case)):
    sum+=case[i]
print(sum)
print(case)
def sum(case):
    if len(case)==1:
        return case[0]
    else:
        return case.pop()+sum(case)
print(sum(case))
"""
회문은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미한다.
회문을 판별할 수 있는 함수를 리스트 슬라이싱과 재귀함수 활용해서 만들기
"""
def dis(string):
    if len(string)<=1:
        print("회문입니다")
        return
    else:
        if string[0]==string[-1]:
            return dis(string[1:-1])
        else:
            print("회문이 아닙니다")
            return

dis('rurur')
dis('kimmik')
dis('kimchi')

"""
n이 홀수면 3*n+1을 하고
n이 짝수면 n을 2로 나눈다
이렇게 계속 진행해서 n이 결국 1이 될 때까지 2와 3의 과정을 반복한다.
"""
def event(n):
    print(n)
    if n==1:
        return n
    else:
        if n%2==1:
            return event(3*n+1)
        else:
            return event(n//2)
event(int(3))