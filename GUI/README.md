# 파이썬 GUI(Graphical User Interface)

## tkinter
* 파이썬에서 제공하는 GUI 모듈로 표준 윈도 라이브러리이다.
* import를 통해 라이브러리를 불러온다.
<pre><code>from tkinter import &#42;</code></pre>

* 루트 윈도(Root Window) 또는 베이스 윈도(Base Window)
* 기본이 되는 윈도를 반환한다.
<pre><code>window = Tk()</code></pre>

* window.mainloop() 함수
* 이벤트(키보드 입력, 마우스 클릭 등)를 처리한다.
<pre><code>window.mainloop()</code></pre>

* window.title() 함수
* 윈도창 제목 표시
<pre><code>window.title("윈도창 제목")</code></pre>

* window.geometry() 함수
* 윈도창의 크기를 지정한다.
<pre><code>window.geometry("500x500")</code></pre>

* window.resizable(width = FALSE, height = FALSE)
* 윈도창 크기 고정
<pre><code>window.resizable(width = FALSE, height = FALSE)</code></pre>