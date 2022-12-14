# ezen03-1
# 파이썬 데이터 타입(자료형)
# 데이터 타입, 숫자형, 숫자형 연산


'''
  int : 정수
    - Python은 컴퓨터의 메모리가 허용하는 한, 정수 데이터의 크기 제한은 없다.
  float : 실수
    - 실수 데이터와 정수 데이터 사이에서 연산 시, 데이터의 형 변환(정수 => 실수)이 이루어짐.
  complex : 복소수
  bool : 불린
  str : 문자열 (시퀀스)
    - 문자열을 사용할 때 작은 따옴표나 큰 따옴표를 사용한다.
    - 문자열 안에서 큰 따옴표나 작은 따옴표를 출력해야 한다면 이스케핑을 사용할 수 있다.
        - 역 슬래시 (\) 기호를 사용함
    - 이스케이프(escape) 문자
        - \" : 큰 따옴표 출력.
        - \' ; 작은 따옴표 출력.
        - \n : 줄 바꿈(new line) 문자 출력함.
        - \t : 탭(tab)문자를 출력한다.
        - \\ : 백슬래시(backslash) 문자를 출력한다.
  list : 리스트 (시퀀스) - 숫자형 가능
  tuple : 튜플 (시퀀스)
  set : 집합
  dict : 사전

'''

a = 7000
b = 75000
print(a+b)

x = 1234567890123455667788
print(x)

a = 2.5
b = 4
print(a+b)
print(a*b)

# 데이터 타입
v_str1 = "NiceYear"
v_bool = True
v_str2 = "happay new year"
v_float = 10.0
v_int = 7
v_list = [v_str1, v_str2]
v_dict = {
    "name" : "NiceYear",
    "age" : 25
}
#read only
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

# 데이터 타입 출력
print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_list))
print(type(v_dict))
print(type(v_tuple))
print(type(v_set))

print()

print(" \"일상\" 의 연속은 \"결과\" 이다. ")


a = 5.
b = 4
c = .4
d = 7.7


# 형 변환
print(float(b))         # 정수 - > 실수
print(int(c))           # 실수 - > 정수
print(int(d))           # 실수 - > 정수
print(int(True))        # bool - > 정수
print(float(True))      # bool - > 실수
print(int(False))        # bool - > 정수
print(float(False))      # bool - > 실수

print()


#외부 모듈
import math

#ceil
print(math.ceil(5.1))           # x이상의 수 중에서 가장 작은 정수
print(math.ceil(8.999))       

#floor
print(math.floor(3.874))       # x이하의 수 중에서 가장 큰 정수
print(math.floor(-25.5))

