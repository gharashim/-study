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