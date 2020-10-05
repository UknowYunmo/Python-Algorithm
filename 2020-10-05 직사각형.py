"""
1. 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
"""
box_list=[]
X=0
Y=0
XY=[]

for i in range(0,3):
    A,B=map(int,input().split())
    box_list.append((A,B))

for i in range(0,2):
    if box_list[0][0]==box_list[1][0]:
        X=box_list[2][0]
        break
    elif box_list[1][0]==box_list[2][0]:
        X=box_list[0][0]
        break
    elif box_list[0][0]==box_list[2][0]:
        X=box_list[1][0]
        break
for i in range(0,2):
    if box_list[0][1]==box_list[1][1]:
        Y=box_list[2][1]
        break
    elif box_list[1][1]==box_list[2][1]:
        Y=box_list[0][1]
        break
    elif box_list[0][1]==box_list[2][1]:
        Y=box_list[1][1]
        break

# 한참 고민했다가 내가 택한 방법은 x,y 좌표 중에 겹치는게 있으면 나머지 x 좌표, y좌표를 출력하는 방법
# 난 코딩 어린이지만.. 뭔가 노다가를 한 것 같아 죄책감이 든다.
# 깔끔하게 만들어 죄책감을 좀 덜어보자
for i in range(0,2):
    if box_list[0][i]==box_list[1][i]:
        XY.append(box_list[2][i])
        continue
    elif box_list[1][i]==box_list[2][i]:
        XY.append(box_list[0][i])
        continue
    elif box_list[0][i]==box_list[2][i]:
        XY.append(box_list[1][i])
        continue
print(str(XY[0])+" "+str(XY[1]))
# 응애