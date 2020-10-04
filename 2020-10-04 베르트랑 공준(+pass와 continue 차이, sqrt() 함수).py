"""
1. 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다.
(11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하며, 한 줄로 이루어져 있다. (n ≤ 123456)
입력의 마지막에는 0이 주어진다.
"""
while True:
    N=int(input())
    cnt=0
    if N==0:
        break
    elif N==1:
        print(1)
    else:
        for i in range(N+1,2*N):
            sosu_x=0
            for j in range(2,i):
                if i%j==0:
                    sosu_x=1
                    break
            if sosu_x==0:
                cnt+=1
        print(cnt)
#1차 시도 - 시간 초과

from math import sqrt
while True:
    N=int(input())
    cnt=0
    if N==0:
        break
    elif N==1:
        print(1)
    else:
        for i in range(N+1,2*N+1):
            for j in range(2,int(sqrt(i))+1):
                if i%j==0:
                    break
            else:
                cnt+=1
        print(cnt)
#2차 시도 - 제곱근 sqrt() 사용 - 시간 초과

from math import sqrt
while True:
    N=int(input())
    cnt=0
    if N==0:
        break
    for i in range(N+1,2*N+1):
        if N==1:
            cnt=1
            continue
        else:
            for j in range(2,int(sqrt(i))+1):
                if i%j==0:
                    break
            else:
                cnt+=1
    print(cnt)
#3차 시도 sqrt() + if문 위치 바꾸기, for문 조정 - 시간 초과
#뭐 어쩌라고 나보고

# 하다가 알게된 pass와 continue의 차이점
for i in range(1, 5):
    if i == 3:
        pass
    print(i)
print("----------------------")
for i in range(1, 5):
    if i == 3:
        continue
    print(i)
# pass하면 밑의 print도 실행하지만 continue하면 그냥 바로 for문으로 다시 올라감





