# [Python](https://github.com/11618nathan/Python) 

1991년 귀도 반 로섬(Guido van rossum)이 발표한 프로그래밍 언어. 1989년 크리스마스가 있던 주에 연구실이 닫혀서 심심하던 차에 만들기 시작했다고 함. 파이썬이라는 이름은 영국의 6인조 코미디 그룹 '몬티 파이썬'에서 따왔고, 로고는 파이썬(Python)이라는 영어 단어가 뜻하는 '비단뱀'을 모티프로 만들어졌음. 

## 특징
* 인터프리터 언어로 한 라인씩 순서대로 실행(대화식 프로그래밍)
* 배치(batch) 형식으로 동작 - 작성된 프로그램을 일괄적으로 실행

## 장점 
* 짧은 프로그램을 빠르게 작업 가능
* 문법이 간단해서 배우기 쉬움.
* 다양한 분야(웹 서버, 해킹 도구, IoT, 기계학습-딥러닝에서 활용되고 많은 유저들이 있음.
* 대부분의 운영체제(윈도우, 리눅스, 맥)에서 사용 가능.
* 파이썬 3.x 버전을 기본적으로 사용.

## 단점
* 느리다(C언어보다 10 ~ 350배 느림)

## 주석

프로그램에 영향을 주지 않는 코드, 프로그램을 설명하는데 사용. # 시호를 붙여 주석 처리.

## IDLE

기본으로 제공하는 IDLE 사용.
대화형 모드로 파이썬 실행.

## Syntax Error

Syntax Error는 파이썬의 일반적인 오류. 
코드 작성시 콜론, 괄호, 큰따옴표, 작은따옴표를 포함하여 단어의 철자까지 정확히 사용하는지를 확인.

## 키워드

키워드(keyword)는 특별한 의미가 부여된 단어, 파이썬에서 미리 정해짐. 대소문자 구분.

ex)키워드 리스트 목록 출력하는 방법
* import keyword
* keyword.kwlist

## 식별자

식별자(identifier)는 프로그래밍 언어에서 이름을 붙일 때 사용하는 단어. 주로 변수 또는 함수 이름 등으로 사용. 스네이크 케이스와 캐멀 케이스 사용.
* 스네이크 케이스(snake_case): 단어 사이에 \_기호를 붙여 식별자 생성.
* 캐멀 케이스(CamelCase): 단어들의 첫 글자를 대문자로 만들어 식별자 생성.
* 파스칼 케이스

## 변수
* 자료형 명시X -> 값에 따라 
* 

## 변수명 기본 규칙 
* 첫 문자는 영문자 또는 밑줄 문자로 시작
* 알파벳, 숫자, 언더스코어(특수 문자 \_)만 사용 가능
* 키워드 사용X
* 공백 포함X
* 예약어(사용하고 있는 일부 단어)X -> SyntaxError: invalid syntax


## 출력

print() 함수 사용.

## 자료형
* 수치형 자료
** 데이터의 종류를 구분하기 위해 사용
** 정수형 상수: -1, 0, 1 과 같은 상수
** 실수형 상수: -0.7, 2.1 등과 같이 분수로 표현할 수 있는 유리수와 파이(원주율), 무리수 포함
** 복소수형 상수: 복소수(실수부 + 허수부)

* 문자열 자료
** 한 글자 이상의 문자나 숫자, 기호 구성된 자료

*리스트 자료
** [] 안에 임의의 객체를 순서 있게 나열한 자료형
** 리스트 요소는 콤마(,)로 구분

* 튜플 자료
** 요소 값 변경X

* 사전 자료
** {} 안에 키:값 으로 된 쌍이 요소로 구성된 순서가 없는 자료형
** 콤마(,)로 구분
** 순서X -> 키로 접근, 인덱스로 값 접근X

문자열, 정수, 실수 등, 불린(boolean): 참(True)/False(거짓), 컨테이너 형

## 튜플

문자열, 숫자, 다른 자료형을  저장할 수 있음. 콤마로 값을 구분, 변수와 달리 저장된 값을 변경할 수 없음. 튜플에 저장된 값은 인덱스 0부터 시작.

## 문자열

특수 문자열(이스케이프 시퀀스) 
* \n - 문자열의 줄을 바꿔줌.
* \t - 문자열에 탭 형식의 들여쓰기를 삽입
* \\ - 문자열에 \(역슬래시) 문자를 표현.
* \" - 문자열에 인용 부호를 표현.

## 연산자

산술 연산자 목록
* \+ 더하기
* \- 빼기
* \* 곱하기
* / 나누기
* // 나누기(정수값)
* % 나머지

비교 연산자
* == ~와 같으면
* != ~와 같지 않다면
* > ~보다 크면
* \< ~보다 작으면
* >= ~보다 크거나 같으면
* \<= ~보다 작거나 같으면

## 수학 계산

파이썬의 별표를 곱하기 기호로 사용.
나누기 기호는 슬래시로 사용.


## 주석
\# 주석 또는 코멘트 사용
\"\"\"주석 처리할 문장\"\"\"

## 사용자 입력
사용자 입력 받는 함수. 한 번에 문자열을 하나만 받을 수 있고 사용자가 엔터 키를 누를 때까지 기다림.
* input()


## * 애스터 리스크

