"""
1. 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다.
카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다.
블랙잭은 카지노마다 다양한 규정이 있다.
한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
그런 후에 딜러는 숫자 M을 크게 외친다.
이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다.
블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
"""

# 이것저것 시도해보다가 단계로 나눠서 풀어야겠다는 결론.. 애초에 3개를 못 고르겠다 ㅠ

# 1단계
# [5, 6, 7, 8, 9] 이렇게 있는 리스트에서 2개를 뽑는 모든 경우의 수를 출력해보자

card_list=[5, 6, 7, 8, 9]
for i in range(0,4):
    for j in range(i+1,5):
        print(card_list[i], card_list[j])
# 지금보면 정말 간단한 과정인데 이 생각을 하는 게 제일 어려웠음..ㅠㅠ

# 2단계
# 3개를 뽑는 모든 경우의 수를 출력해보자

for i in range(0,4):
    for j in range(i+1,5):
        for k in range(j+1,5):
            print(card_list[i], card_list[j], card_list[k])

# 3단계
# 뭔가 규칙을 찾았으니 이제 5개로 고정하지말고, 카드 값도 입력받는 형태로 일반화 시켜보자

N,M=map(int,input().split())
card_list=list(map(int,input().split()))
for i in range(0,N-1):
    for j in range(i+1,N):
        for k in range(j+1,N):
            print(card_list[i], card_list[j], card_list[k])

# 4단계
# 이제 3가지 카드를 다 더하고, 저장한 뒤, M과 가장 비슷한 값을 찾아보자
N,M=map(int,input().split())
card_list=list(map(int,input().split()))
sum_list=[]
for i in range(0,N-1):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (card_list[i]+card_list[j]+card_list[k])<=M:
                sum_list.append(card_list[i]+card_list[j]+card_list[k])
print(max(sum_list))

# 오늘의 결론 : 3개를 뽑으려면 for문을 1씩 더하면서 계속 3번 늘려주면 가능하다.