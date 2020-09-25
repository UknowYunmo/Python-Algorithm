"""
어제 못 푼 그룹 단어 체커를 단계별로 나눠서 해보자..
1단계
----------------------------------
"AAABOBCCAB"를
"ABOBCAB"로 만들어보자
----------------------------------
"""
S="AAABOBCCAB"
S+=" "
word_A=[]
for i in range(0,len(S)-1):
    if S[i]==S[i+1]:
        pass
    else:
        word_A.append(S[i])
print(word_A)
#마지막 알파벳도 그 다음 알파벳과 비교를 해야하는 상황이 반드시 오기 때문에 의미가 없는 공백을 추가해서 비교하게 하고,
#word에 리스트의 형태로 넣었다.
S2=""
for i in range(0,len(word_A)):
    S2+=word_A[i]
print(S2)
#S2를 빈 스트링으로 만들고, for문을 돌려 한 글자씩 추가해서 ABOBCAB라는 내가 원하는 알파벳을 만드는데 성공했다.
#그럼 이제 이 과정을 한 번에 여러개 받아 변환하도록 해보자
"""
--------------------------------------------
2단계
여러 줄에 알파벳을 받고 각각의 알파벳에
1단계를 반복해서 수행하여 한 곳에 저장까지 해보자
--------------------------------------------
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
print(word_list)
# 1단계를 응용하는 대신, del word_A[:]을 통해서 word_A를 계속 비우는 것이 핵심이다.
# 이걸 안 비워주면 계속 첫번째 행의 변환된 문자만 돌려주기 때문
# 계속 비워주면서 대신 word_list라는 리스트에 담아둠으로서 저장했다.