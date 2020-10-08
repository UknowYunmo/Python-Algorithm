"""
1. 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
첫째 줄에 N!을 출력한다.
"""
N=int(input())
if N==0 or N==1:
    print(1)
else:
    for i in range(N-1,0,-1):
        N*=i
    print(N)
# 그냥 for문으로 해봐도 답이 나온다.
# 하지만 '재귀 함수'를 써보라니까 일단 개념을 알아보자.
# 재귀 함수 : 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 방식으로 주어진 문제를 푸는 방법

N = int(input())
def factorial(N):   #def로 함수 만들기
    if N==0 or N==1:
        return 1
    else:
        return N * factorial(N-1)   #함수 안에 자기 자신 함수를 넣기
print(factorial(N))
# 신기해서 이게 과연 자바로도 될까 해서 검색해봤는데 static으로 선언해서 함수 만들면 가능