"""
1. 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.
알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.
입력으로 주어진 글자의 아스키 코드 값을 출력한다.

a=input()
print(ord(a)) # -- 문자-> 아스키 코드
#print(chr(ord(a))) -- 아스키 코드-> 문자로 변환

2. N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
입력으로 주어진 숫자 N개의 합을 출력한다.

N=int(input())
X=input()
sum=0
for i in range(0,N):
    sum+=int(X[i])
print(sum)

3. 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서,
단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

S=input()
for i in range(97,123):
    already=0
    for j in range(0,len(S)):
        if already==0 and chr(i)==S[j]:
            print(j)
            already+=1
    if already==0:
        print(-1)

4. 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

N=int(input())
case_list=[]
QR_list=[]
for i in range(0,N):
    case_list.append(input())
for i in range(0,N):
    QR_code=''
    for j in range(0,len(case_list[i])-2):
        QR_code+=case_list[i][j+2]*int(case_list[i][0])
    QR_list.append(QR_code)
for i in range(0,N):
    print(QR_list[i])

5. 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
"""
S=input()
S=S.upper()
max=0
count_list=[]
for i in range(65,91):
    count=0
    for j in range(0,len(S)):
        if ord(S[j])==i:
            count+=1
    if count>max:
        max=count
    count_list.append(count)
if count_list.count(max)>=2:
    print("?")
else:
    print(chr(count_list.index(max)+65))