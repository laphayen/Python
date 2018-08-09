# import
from tkinter import *
import Calculator_function

# 키 입력
def click(key):
    # = 버튼
    if key == "=":
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END, " --> Error")

    # C 버튼 display 엔트리 위젯 제거           
    elif key == "C":
        display.delete(0, END)

    # 상수
    elif key == constants_list[0]:
        display.insert(END, "3.141592654")
    elif key == constants_list[1]:
        display.insert(END, "300000000")
    elif key == constants_list[2]:
        display.insert(END, "330")
    elif key == constants_list[3]:
        display.insert(END, "149597887.5")

    # 함수 버튼
    elif key == functions_list[0]:
        # display 엔트리 위젯 저장
        n = display.get()
        # display 엔트리 위젯 제거
        display.delete(0, END)
        display.insert(END, calc_functions.factorial(n))

    elif key == functions_list[1]:
        # display 엔트리 위젯 저장
        n = display.get()
        # display 엔트리 위젯 제거
        display.delete(0, END)
        display.insert(END, calc_functions.to_roman(n))

    elif key == functions_list[2]:
        # display 엔트리 위젯 저장
        n = display.get()
        # display 엔트리 위젯 제거
        display.delete(0, END)
        display.insert(END, calc_functions.to_binary(n))
        
    elif key == functions_list[3]:
        # display 엔트리 위젯 저장
        n = display.get()
        # display 엔트리 위젯 제거
        display.delete(0, END)
        display.insert(END, calc_functions.from_binary(n))

    # 나머지 기본 동작:
    else:
        display.insert(END, key)

# main
window = Tk()
window.title("Calculator")

# top_row 프레임
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# 수정 엔트리 위젯
display = Entry(top_row, width=45, bg="light green")
display.grid()

# 숫자 버튼 프레임
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
'7',  '8',  '9',
'4',  '5',  '6',
'1',  '2',  '3',
'0',  '.',  '=' ]

# 버튼 생성
r = 0
c = 0
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
    c = c+1
    if c > 2:
        c = 0
        r = r+1

# 연산자 프레임
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = [
'*', '/',  
'+', '-',
'(', ')',
'C' ]

# 버튼 생성
r = 0
c = 0
for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)
    Button(operator, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
    c = c+1
    if c > 1:
        c = 0
        r = r+1

# mainloop
window.mainloop()
