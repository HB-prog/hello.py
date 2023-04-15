#1부터 10까지 출력하기
i = 0
while i < 10:
    i = i + 1
    print(i, end=" ") #end=" "는 가로로 출력하기 위한 print명령어의 옵션
print(' ') #end 옵션 때문에 가로 정렬로 출력되는 것을 원래대로 되돌림

#for문으로 작성
for n in range(1,11):
    print(n, end=" ")
print(' ')





#1부터 10까지의 총합 출력하기
sum = 0
for value in range(1,11):
    sum = sum + value
print(sum)

#while문으로 작성
sum2 = 0
value = 0
while value < 10:
    value = value + 1
    sum2 = sum2 + value
print(sum2)





#1부터 20까지 홀수만 출력하기
for odd in range(1,21):
    if odd%2 != 0:
        print(odd, end=" ")
print(' ')

#while문으로 작성, 이번엔 짝수만
odd = 0
while odd < 20:
    odd = odd + 1
    if odd%2 == 0:
        print(odd, end=" ")
print(' ')






#소수인지 아닌지 판별하기
num = int(input("숫자를 입력하세요: "))
for i in range(2,num):
    is_prime = True
    if num%i == 0:
        is_prime = False
        break
if is_prime == True:
    print("%d은 소수입니다." %num)
else:
    print("%d은 소수입니다." %num)



#홀짝 판별하기
is_even = int(input("숫자를 입력해주세요: "))
if is_even%2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
