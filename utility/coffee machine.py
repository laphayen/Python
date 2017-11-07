# 가격
price = 300

# 기본
coffee = 10

while True:
    print('----- COFFEE MACHINE -----')
    money = int(input('돈을 넣어주세요: '))

    # 2잔 이상
    if money >= 600:
        cup = int(input('몇 잔을 드릴까요?'))
        money = money - (price * cup)
        if money >= 0:
            coffee = (coffee - cup)
            print(cup, '잔을 드립니다.')
            print(money, '을 반환합니다.')
        else:
            print('금액이 부족합니다.')
            print('돈을 반환합니다.')

    # 1잔
    elif money > 300:
        money = money - price
        coffee = (coffee - 1)
        print('1잔을 드립니다.')
        print(money, '을 반환합니다.')

    # 1잔
    elif money == 300:
        coffee = (coffee - 1)
        print('1잔을 드립니다.')

    # 반환
    else:
        print('돈이 부족합니다.')
        print('돈이 반환합니다.')

    print('커피가 ', coffee, '잔 남았습니다.')

    if coffee == 0:
        break
