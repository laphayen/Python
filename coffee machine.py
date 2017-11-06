
# 가격
price = 300

# 기본
base = 10

while (base > 0):
    print('----- COFFEE MACHINE -----')
    money = int(input('돈을 넣어주세요: '))
    
    # 2잔 이상
    if money >= 600:
        cup = int(input('몇 잔을 드릴까요?'))
        money = money - ( price * cup )
        base = (base - cup)
        print(cup,'잔을 드립니다.')
        print(money, '을 반환합니다.')
    
    # 1잔
    elif money > 300:
        money = money - price
        base = (base - 1)
        print('1잔을 드립니다.')
        print(money, '을 반환합니다.')

    # 1잔
    elif money == 300:
        base = (base - 1)
        print('1잔을 드립니다.')
    
    # 반환
    else:
        print('돈이 부족합니다.')
        print('돈이 반환합니다.')

    print(' ')

print('다 팔렸어ㅋㅋ 내일 오셈ㅋㅋ')
