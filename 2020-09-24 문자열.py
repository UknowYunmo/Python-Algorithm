"""
어제 못 풀은..
4. 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다.
위 목록에 없는 알파벳은 한 글자씩 센다.

Cro_list=['c=','c-','dz=','d-','lj','nj','s=','z=']

S=input()
count=len(S)
S+=" "
for i in range(0,len(S)-2):
    for j in Cro_list:
            if j==S[i]+S[i+1]+S[i+2]:
                count-=1
            else:
                if j==S[i]+S[i+1]:
                    count-=1
print(count)

# 원래는 'dz='가 3자리에서 1자리가 되니 -2를 해야하지만, 이 경우 항상 다음 'z='에도 인식되어 -1 처리가 강제적으로 한 번 더 됨
# 그래서 아예 -1로 바꾸었다. 이렇게 하면, 위에서 -1, 그리고 밑에서 -1 한 번 더 되서 알아서 -2가 됨
# 항상 range(0,len(s)-1)을 하면 세자리를 검출할때 s[i+2]가 리스트 범위에서 벗어날 수 밖에 없는 상황이 됐다.
# 그래서 아예 의미없는 빈 공백을 추가해서 S[i+2]를 만들어주고 범위를 len(s)-2로 바꾸니 해결됐다

5. 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

"""

N=int(input())
word_list=[]
change_list=[]
count=N
for i in range(0,N):
    word_list.append(input())
for i in range(0,N):
    for j in range(0,len(word_list[i])-1):
        if word_list[i][j]==word_list[i][j+1]:
            change_list=word_list[i].replace(word_list[i][j],"")
print(change_list)

"""
for i in range(0,N):
    error = 0
    if len(word_list[i])<3:
        pass
    else :
        for j in range(0,len(word_list[i])-2):
            for k in range(j+2,len(word_list[i])):
                if word_list[i][j]==word_list[i][k]:
                    error+=1
    if error>=1:
        count-=1
print(count)
"""

#아...도저히 못 풀겠다..뭔가 단단히 잘못됐다 문제를 단계별로 나눠서 풀어봐야겠다.....