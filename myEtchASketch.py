# tkinter 라이브러리
# myEtchASketch 응용 프로그램
# * 애스터리스크

# 좌표 왼쪽 위(0, 0)

from tkinter import *

# 변수
canvas_height = 600
canvas_width = 600
canvas_colour = "orange"

# 선 끝 x좌표
move_x = canvas_width/2

# 선 끝 y좌표
move_y = canvas_height

# 선 색상
move_colour = "lightgreen"

# 선 두께
line_width = 7

# 선 길이 
line_length = 7

# user
def move(event):
    global move_y

    canvas.create_line(move_x, move_y, move_x, (move_y - line_length), width = line_width, fill = move_colour)
    move_y = move_y - line_length

# main
window = Tk()
window.title("MyEtchASketch")
canvas = Canvas(bg = canvas_colour, height = canvas_height, width = canvas_width, highlightthickness = 0 )
canvas.pack()

window.mainloop()
