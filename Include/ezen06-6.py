import pandas as pd

agg_prd_pd = pd.DataFrame({
    'L' : [5141, 5365, 5084],
    'M' : [4968, 4977, 4915],
    'S' : [5012, 4991, 5029],
    'XL' : [5071, 4976, 5023],
    'XS' : [5195, 4954, 5088]
}, index = {'Jacket', 'Shirt', 'Trousers'})

print(agg_prd_pd)

print()
'''
  - 데이터 삭제 : drop()
    - 필요없는 데이터를 삭제
    - 행(index), 열(column)단위로 삭제
  
  - 중복 데이터 삭제 :
    - duplicated() :  데이터 중복 여부를 true, false로 반환
                      keep: 중복이 있다면 처음과 마지막 값 중 어떤 것을 중복이라고 판단
    - drop_duplicates() : 중복된 데이터를 삭제
'''

df = pd.DataFrame({
    'SIZE' : ['L', 'M', 'L', 'S', 'XS'],
    'product_type' : ['Jacket', 'Shirt', 'Jacket', 'Trousers', 'Shirt'],
    'color' : ['red', 'black', 'black', 'red', 'blue'],
    'quantity' : [5, 15, 10, 20, 15]

})
# axis = 0 (세로), axis = 1 (가로)
print(df)
print()
print(df.drop(['color'], axis=1))

print()
print(df.drop(['color', 'quantity'], axis=1))

print()
print(df.drop(['SIZE', 'product_type'], axis=1))


print()
# print(df.drop(['SIZE', 'product_type]))
print(df)
print(df.drop([0], axis=0))

print()
print(df.drop([1, 4]))


print('----------------------------------------')
print(df)

#   duplicated는 단일 값은 false로, 중복된 값을 Ture로 반환
print()
print(df.duplicated(['product_type'], keep='first'))

# last 는 first의 반대로 false 값이 true로 반환한다.
print()
print(df.duplicated(['product_type'], keep='last'))

print()
print(df)

print()
print(df.drop_duplicates(['product_type'], keep='first'))


print()
print(df)


print()
print(df.drop_duplicates(['product_type'], keep="last"))