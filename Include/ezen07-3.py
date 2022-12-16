'''
  리스트 내 원소 중에서 가장 큰 값의 인덱스(위치)를 찾아서 반환하는 함수를 작성하시오.

  data = [7, 1, 5, 9, 3, 2, 4]

'''
data = [7, 1, 5, 9, 3, 2, 4]
max_num = max(data)
def max_data(i):
  for i in range(len(data)):
    if data[i] == max(data):
      print(i)

max_data(data)

print()


def find_index_largest(data):
    largest_index = 0
    for i in range(len(data)):
      # 더 큰 값을 찾은 경우
      if data[largest_index] < data[i]:
        largest_index = i
    return largest_index

data = [7, 1, 25, 20, 3, 2, 4]
largest_index = find_index_largest(data)
print(largest_index)

'''
  특정한 값을 가지는 원소의 인덱스를 찾는 함수를 작성해 보시오

  [3, 5, 7, 9], 2     ==> -1
  [3, 5, 7, 9], 7     ==> 2
  enumerate()
'''

print()



def find_specific_value(lis, value):
    for i, x in enumerate(lis):
        if x == value:
            return i
    return -1 # 찾지 못 한 경우


print(find_specific_value([3, 5, 7, 9], 2))
print(find_specific_value([3, 5, 7, 9], 7))
    

'''
  하나의 자연수가 주어졌을 때, 소수인지 아닌지 판별하는 함수를 작성하시오.
'''
print()




def determine_num(x):
  for y in range(2, x):
    if x % y == 0:
      return "소수가 아닙니다."
  return "소수"


print(determine_num(5))

print()

def determine_prime(x):
  # 1 이하인 경우 소수가 아님
  if x <= 1:
    return False
  # 1과 자기 자신 외의 자연수로 나누어지면 소수가 아님
  for divisor in range(2, x):
    if x & divisor == 0:
      return False
  return True

print(determine_prime(3))
  

print("숫자 찾기")

def find_num(data,num):
    find_numlist = [] 
    for number in enumerate(data):
        print(number)
        if num == number[1]:
            find_numlist.append(number[0])

    if len(find_numlist) == 0 :
        return -1
    else:
        return find_numlist

num_data = [3,5,7,9,5]
print(f"찾은숫자의 인덱스: {find_num(num_data,5)}")






