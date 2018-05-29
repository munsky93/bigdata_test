i = input("숫자 5개를,로 구분하여 입력하세요 : ")
j = 0
i = i.split(",")

for k in i :
    j += int(k)

print(j/5)