import project #project 모듈을 Import 함

a,op,b = input().split() #a와 b를 피 연산자로 입력받고 op변수(Operator)로 연산자를 입력받음
a=int(a) #string에서 integer형으로 변환
b=int(b)

if op== "+":
    project.add(a,b)

if op== "-":
    project.ms(a,b)

if op== "*":
    project.mul(a,b)

if op== "*": #곱하기 연산의 경우
    if b==0:
        project.mul_if_a(a) #b에 0이 입력될 경우 a에 해당하는 값을 인자로 보내고 구구단 값을 출력하는 함수 mul_if_a를 호출

if a==0:
    project.mul_if_b(b) #a에 0이 입력될 경우 b에 해당하는 값을 인자로 보내고 구구단 값을 출력하는 함수 mul_if_b를 호출

if op== "/":
    project.ahffn(a,b)