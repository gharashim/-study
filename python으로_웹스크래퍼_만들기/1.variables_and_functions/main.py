###############################################################
# .0 Hello wolrd
print('Hello world')


###############################################################
# .1 Variables
# python은 변수 선언 및 타입 지정 불필요
a = 2 # 0x0001
b = 3 # 0x0002
c = a + b
# c = 1
print(c)

# my age = 98 # 변수에 공백은 불가능
my_age = 98 # snake
MyAge = 98 # camel
# 654my_age = 98 # 숫자로 시작하는 변수 선언 불가능


###############################################################
# .2 Booleans and Stings
# my_name = garam # garam이라는 문자를 변수로 인식
my_name = 'garam' # 따옴표로 감싸면 뭐든 문자로 인식
print(my_name)

my_boolean1 = True
my_boolean2 = False # boolean은 참/거짓
# boolean인 True 및 False는 따옴표 없이!
# 맨 앞글자는 대문자로 입력해야 한다.


###############################################################
# .3 recap
my_name = 'Garam'
age = 32
print('Hello my nams is', my_name)
print("and I'm", age, 'years old')


###############################################################
# .4 functions
def say_hello():
    # 함수 이름도 변수와 동일한 법칙 적용
    # 뒤에 괄호 및 콜론을 붙여야 한다.
    print('Helow, how are you?')
    print('This is functions space.')

# def는 함수를 정의만 할 뿐이다.
# 함수를 실행하기 위해서는 아래와 같이 함수 이름을 입력한다.
say_hello() # 함수 뒤의 괄호는 함수를 실행한다는 의미
# say_hello(123) say_hello 함수 정의 시 입력 변수 없으므로 error 발생


###############################################################
# .5 Indentation
# 파이썬은 들여쓰기를 통해 function을 구분한다.
def say_bye():
    print('bye bye')
    say_hello()


###############################################################
# .6 Parameters
# function에 입력값 전달하기 - parameter 혹은 argument라고 부른다
def say_hello_name(name):
    print('hello', name, 'how r u?')

say_hello_name('Garam')


###############################################################
# .7 Multiple Parameters
# function에 입력값 전달하기 - parameter 혹은 argument라고 부른다
def say_hello_name2(name, age):
    print('hello', name, 'how r u?')
    print("I'm", age, 'years old')

say_hello_name2('Garam', 20)
# *의 역할? > uncap, 여러개 argument에 활용


###############################################################
# .8 Recap
def tax_calculator(money): # 함수의 정의는 def로 시작한다.
    print(money * 0.35)
    # pass # 들여쓰기로 함수 내 공간을 구분

tax_calculator(10000000000000)


###############################################################
# .9 Default Parameters
def say_hello_name(name = 'Anonymous'): # 변수의 default 값 지정
    print('hello', name, 'how r u?')

say_hello_name('Garam')
say_hello_name() # 아무것도 입력하지 않으면 default 값 출력

## 계산기 만들기
def plus(a, b):
    print(a + b)


def mius(a, b):
    print(a - b)


def multiple(a, b):
    print(a * b)


def divide(a, b):
    print(a / b)


def power(a,b):
    print(a ** b)


###############################################################
# .10 Return Values
def tax_calc(money):
    return money * 0.35

to_pay = tax_calc(150000000)


###############################################################
# .11 Return Recap
my_name = 'garam'
my_age = 12
my_colors_eyes = 'brown'

# f"" string
print(f"Hello I'm {my_name}, I have\
{my_age} years in the earth,\
{my_colors_eyes} is my eye color")