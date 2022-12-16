'''
  ezen07-2


  * Default parameter (기본 인자)
      - 함수의 파라미터에 기본값 지정 가능
      - 파라미터를 명시하지 않을 경우, 지정된 기본값으로 대체
      - 디폴트 파라미터 뒤에 일반 파라미터가 위치할 수 없다
          - e.g) def test(a, b, c = 1)
                 def test(a, b = 1, c = 2)
                 def test(a = 1, b = 1, c = 3)

                 올바르지 않은 예)
                  def test(a, b = 1, c)
                  def test(a=1, b, c)
                  def test(a=1 , b=1 , c)
'''

print('test')
help(print)

def plus_ver2(number_01, number_02 = 100):
    print(number_01 + number_02)
    return plus_ver2

print(plus_ver2(11))
plus_ver2(11)
print(plus_ver2(number_01= 0, number_02= 77))

print()

'''
    *agrs : 함수를 호출할 때 아규먼트의 갯수를 특정지을 수 없을 때 사용함
            불특정한 수의 숫자들은 'agrs'라는 튜플에 추가된다.
'''
def plus_unlimited(*args):
    print(type(args), args)
    sum(args)
    print(sum(args))


plus_unlimited(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ,15, 16, 17)

print()

'''
  **kwargs : 함수를 호출할 때 키워드 아규먼트의 갯수를 특정지을 수 없을 때 사용한다
             불특정한 수의 키워드 아규먼트들은 'kwargs' 라는 딕셔너리에 추가된다.
'''
def plus__unlimeited(*args, **kwargs):
    '''
    *args과 **kwargs라는 딕셔너리의 형태로 값을 받는 함수
    전체 합의 결과를 출력합니다.
    '''

    print(type(kwargs), kwargs)
    sum(kwargs.values())              # 키워드 아규먼트의 합
    sum(args)                         # 아규먼트의 합
    print(sum(args) + sum(kwargs.values()))
    print(sum(args), sum(kwargs.values()))

plus__unlimeited(1, 2, 3, 4, 5, num1= 100, num2= 200, num3 = 300)


'''
    list를 함수의 파라미터로 넣어 실행하는 경우
'''
print()
list_numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plus__unlimeited(*list_numbers)

'''
    딕셔너리를 함수의 파라미터로 넣어 실행하는 경우
'''
dict_heights = {'ezen_height' : 178, 'ezenyoung_height' : 180, 'sugiezen_height' : 176 }
plus__unlimeited(**dict_heights)

'''
    Docstring : 함수의 설명을 작성해놓은 기술 문서
                수 많은 파이썬 함수의 사용법과 정보를 나타낸다.
'''
#help(plus__unlimeited)
print()
#help(print)
print()
#help(input)


'''
   * Lambda 함수
      - 단일문으로 표현되는 익명 함수
          - 익명함수란 이름이 없는 구현체만 존재하는 간단한 함수를 의미
      - 코드 상에서 한번만 사용되는 기능이 있을 때,
        굳이 함수로 만들지 않고 1회성으로 만들어서 쓸 때 사용
      
      - lambda가 유용하게 사용되는 대표적 함수(3가지)
          - 함수형 프로그래밍의 기본 요소이기도 하다.
          - filter() : 특정 조건을 만족하는 요소만 남기고 필터링
          - map() : 각 원소를 주어진 수식에 따라 변형하여 새로운 리스트를 반환
          - reduce() : 앞 2개의 원소를 가지고 연산
                       연산의 결과가 또 다음 연산의 입력으로 진행된다.
                       따라서 마지막까지 진행되면 최종 출력은 한개의 값만 남게된다.

'''
print()

square = lambda x:x**2
print(square(5))

def add(x, y):
  return x + y

add =lambda x, y : x + y
print(add(10, 20))

print()

def pythagoras(num1, num2):
  return (num1**2 + num2**2)**0.5

pythagoras_lamdba = lambda num1, num2: (num1**2 + num2**2)**0.5

print(pythagoras_lamdba(4, 5))


'''
   키가 180cm이상인 사람들의 경우 "키가 정말 큽니다."라는 메시지가 출력하고,
   그렇지 않은 경우를 "계속 키가 클 겁니다." 라는 메시지로 출력하는 함수를 작성하시오.

   height_high(181)
   height_high(178)
'''
def height_high(x):
    if x >= 180:
      print("키가 정말 큽니다.")
    else:
      print("키가 계속 클 겁니다.")

height_high(178)
height_high(180)

def height_high(x):
    return "키가 정말 큽니다." if x >= 180 else "계속 키가 클 겁니다."
print()
# 리턴문이기 때문에 변수에 값을 넣어서 출력해야 함.
result = height_high(180)
print(result)

'''
    다섯 사람의 키입니다.   
    height_high() 함수를 이용하여 실행해보기
    
    map(함수, 입력들) 함수
    map(function, *lterables) 형태로 사용 가능하다.
        - *iterables : 원소를 하나씩 차례로 반환 가능한 object를 의미한다. (list, str, tuple ...)

'''
print()
# map(함수, 입력들)

def calc(x):
    return x*x

for i in range(1, 6):
  print(calc(i))



print()
re = list(map(calc, range(1, 6)))
print(re)

print()

dict_heights = {'ezen_height' : 178, 'ezenyoung_height' : 180, 'sugiezen_height' : 176, 'ezensun_height' : 180, 'sunge_height' : 175 }
result = list(map(height_high, dict_heights.values()))
print(result)
