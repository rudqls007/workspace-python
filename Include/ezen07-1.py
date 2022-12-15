# ezen07
# 파이썬 함수 및 람다(lambda)


'''
  1. 함수 정의
  def function_name(parameter):
      code

  2. 함수 호출
  def function_name():
'''

# 함수 1
def hello(world):
    print("Hello, ", world)

hello("NiceYear")


print()

# 함수 2
def hello_return(world):
    value ="Hello, " + str(world)
    return value

str = hello_return("Ezen!")
print(str)

print()
# 함수 3 다중 리턴

def func_mul(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1, y2, y3

val1, val2, val3 = func_mul(3)

print(val1, val2, val3)
print(type(val1))

print()
# 튜플 리턴 - 함수 3 다중 리턴
def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return (y1, y2, y3)

tup = func_mul2(5)

print(tup)
print(type(tup))

tup = func_mul2(4)
print(type(tup), tup, list(tup))


print()
#리스트 리턴
def func_mul3(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return [y1, y2, y3]
  
lis = func_mul3(6)
print(type(lis), lis, set(lis))

print()
# 딕셔너리 리턴
def func_mul4(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return {'ret1' : y1, 'ret2' : y2, 'ret3' : y3}

dic = func_mul4(5)
print(type(dic), dic, dic.get('ret3'), dic.items(), dic.keys(), dic.values())

# 함수4 (*args, **kwargs)
print()
# *args tuple type
def args_function(*args):             # 매개변수명은 자유롭게 변경 가능 ex) args => argss
  for i,v in enumerate(args):
    print('{}'.format(i), v, end=' ')

args_function('ezen')
print()
args_function('ezen', 'ezenit')
print()
args_function('ezen', 'ezenit', 'ezenit1')


print()

# **kwargs  dict type
def args_function2(**kwargs):             # 매개변수명은 자유롭게 변경 가능 ex) kwargs => kwargss
  for v in kwargs.keys():
    print('{}'.format(v), kwargs[v], end=' ')

print()
args_function2(name1='lee')
print()
args_function2(name1='lee', name2 = 'park')
print()
args_function2(name1='lee', name2 = 'park', name3 = 'kim')

print()
# 함수5 - 전체 혼합
def func_ezen(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)

func_ezen(10, 20)
print()
func_ezen(10, 20, 'snow', 'snow2', 'snow3')
print()
func_ezen(10, 20, 'snow', 'snow2', 'snow3', age1='30', age2='31', age3='32')

print()
# 함수 6 - 중첩 함수
def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In function")
    func_in_func(num + 100)

# 중첩 함수일 때 자식 함수는 값을 정의할 수 없다. 무조건 부모 함수만이 가능함
nested_func(20)

print()
# 함수7 - hint
def tot_length(word: str, num: int) -> int:
    return len(word) * num
print(" hint func: " , tot_length("Heavy snow falls in Seoul", 10))
