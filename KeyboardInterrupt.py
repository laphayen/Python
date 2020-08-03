import time

num = 1

try:
    while True:
        print(num)
        num += 1
        time.sleep(0.01)

except KeyboardInterrupt:
    print('Ctrl + C 중지')