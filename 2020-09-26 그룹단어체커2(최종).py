"""
그저께 못 푼 그룹 단어 체커를 단계별로 나눠서 해보자..

--------------------------------------------
2단계
여러 줄에 알파벳을 받고 각각의 알파벳에
1단계를 반복해서 수행하여 한 곳에 저장까지 해보자
--------------------------------------------

N=int(input())
word_list=[]
for i in range(0,N):
    S=input()
    S+=" "
    word_A = []
    for i in range(0,len(S)-1):
        if S[i]==S[i+1]:
            pass
        else:
            word_A.append(S[i])
    S2 = ""
    for i in range(0, len(word_A)):
        S2+=word_A[i]
    word_list.append(S2)
    del word_A[:]
"""
# 1단계를 응용하는 대신, del word_A[:]을 통해서 word_A를 계속 비우는 것이 핵심이다.
# 이걸 안 비워주면 계속 첫번째 행의 변환된 문자만 돌려주기 때문
# 계속 비워주면서 대신 word_list라는 리스트에 담아둠으로서 저장했다.
"""
3단계
---------------------------------------------
word_list에 담긴 중복 없는 문자열들 중
이미 나왔던 문자가 또 나오는 문자열에 대해 검증해보자
---------------------------------------------
count=0
for i in range(0,len(word_list)):
    error=0
    for j in range(0,len(word_list[i])):
        for k in range(j+2,len(word_list[i])):
            if word_list[i][j]==word_list[i][k]:
                error+=1
    if error>=1:
        count+=1
print(N-count)
---------------------------------------------
4단계
합치기
---------------------------------------------
"""
N=int(input())
word_list=[]
for i in range(0,N):
    S=input()
    S+=" "
    word_A = []
    for i in range(0,len(S)-1):
        if S[i]==S[i+1]:
            pass
        else:
            word_A.append(S[i])
    S2 = ""
    for i in range(0, len(word_A)):
        S2+=word_A[i]
    word_list.append(S2)
    del word_A[:]
count=0
for i in range(0,len(word_list)):
    error=0
    for j in range(0,len(word_list[i])):
        for k in range(j+2,len(word_list[i])):
            if word_list[i][j]==word_list[i][k]:
                error+=1
    if error>=1:
        count+=1
print(N-count)
#성공!!!!!!!!!!!!!!!!!ㅠㅠㅠ
#앞으로 안 풀릴 때는 단계별로 나눠서 테스트 해봐야겠다 뿌듯하구만ㅎㅎ
