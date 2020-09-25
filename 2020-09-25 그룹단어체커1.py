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