"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""
# 일단 감이 오지 않으니 N과 M 선언받기 이전 단계로 1,2,3,4 리스트 만들어서 뽑는 연습을 해보자

num_list=[1,2,3,4]
# 한 개 뽑을 때

for i in range(0,4):
    print(num_list[i])


# 두 개 뽑을 때
"""
하다가 새로운 사실을 알았는데
a=2
b=a
a=1
print(b)를 하면 당연히 b는 2가 되지만
a=[1,2,3,4]
b=a
a.pop(0)
a.remove(3)
print(b)
를 하면 b도 [2,4]로 바뀌어있는걸 알 수 있다
#a랑 b가 다른 객체?가 아니라 서로 같은 곳을 참조?하는 느낌인거 같다
#아무튼 리스트를 뽑아쓴 다음에 다시 리스트 원상태로 돌리려면 어떻게 해야하는지 temp 임시 리스트를 만드는거 말고 새로운 방법을 찾아야될거 같다.
"""
for i in range(0,4):
    num_list.remove(i+1)
    for j in range(0,3):
        print(i+1,end=" ")
        print(num_list[j])
    del num_list[:]
    for i in range(0,4):
        num_list.append(i+1)
#일단 del[:]로 초기화하고 다시 1부터 채워넣는 방법을 썼다. 완전 비효율적인건 알지만 다른 방법은 모르겠다. 일단 계속 해보자

# 세 개 뽑을 때

for i in range(0,4):
    num_list.remove(i+1)
    for j in range(0,3):
        num_list.remove(j+1)
        for k in range(0,2):
            print(i+1,end=" ")
            print(j+1,end=" ")
            print(num_list[k])
        del num_list[:]
        for i in range(0,4):
            num_list.append(i+1)

# 이렇게하면 remove할 때 i+1과 j+1이 겹치는 경우에 오류가 발생해서 멈춘다..remove로 하는 방법은 옳지 않은 듯
# 그리고 N과 M을 나중에 선언받아서 해야되는데..M값에 따라 for문을 몇 번 돌릴지 정해야되는데 이건 아닌거 같다..
