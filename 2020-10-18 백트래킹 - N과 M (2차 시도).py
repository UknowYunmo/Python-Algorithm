"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""
# 1단계 - 1,2,3,4,5 리스트로 고정하고 두 개 뽑기
"""
num_list=[1,2,3,4,5]
for i in range(0,5):
    for j in range(0,5):
        if j==i:
            continue
        print(num_list[i],num_list[j])
# i와 j를 검사하고 다를 경우 첫번째 카드랑 두번째 카드 출력
"""
# 2단계 - 1,2,3,4,5 리스트로 고정하고 세 개 뽑기
"""
num_list=[1,2,3,4,5]
for i in range(0,5):
    for j in range(0,5):
        if j==i:
            continue
        for k in range(0,5):
            if k==j or k==i:
                continue
            print(num_list[i],num_list[j],num_list[k])
"""
# 3단계 - 1,2,3,4,5 리스트로 재귀 함수로 2개 뽑기
"""
N=int(input())
num_list=[1,2,3,4,5]
def koo(n):
    for i in range(0,5):
        if i==n:
            continue
        print(n+1,num_list[i])
for i in range(0,5):
    koo(i)
"""
# 4단계 - 1,2,3,4,5 리스트로 N에 3를 넣으면 재귀 함수로 3번 뽑았을 때가 나오게 만들자
# 실패..ㅎ
# 구글해서 답을 봐도 못하겠음 아직 이걸 풀 실력이 안되나보다 실력 쌓고 담에 풀어야겠다




