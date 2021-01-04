
# Numeric(숫자, 정수, 실수)

a = 123
b = 3.14
c = 3.12E10

# e = 0o34
# F = 0xAB

# type()
print(type(a))
print(type(b))
print(type(c))

div = 3/4
print(div)

result = 3 ** 3
print(result)

result = 10 % 3   # 나머지
print(result)

result = 10 // 3   # 몫
print(result)


# Sequence - list
# 임의의 값을 순서대로 저장하는 집합 자료형(index 부여 및 값 변경 가능)
# 함수를 이용하는 방법과 []를 이용하는 방법
# range() 이용하여 리스트를 생성하는 방법

print('''
Sequence -list
함수를 이용하는 방법과 []를 이용하는 방법
range() 이용하여 리스트를 생성하는 방법
''')

a = []
print(type(a))

a = list()
print(type(a))

a = [1, 2, 3]
print(a)

# indexing
print(a[0])
print(a[1])
print(a[2])

# slicing
print(a[0:2])


a = [1, 2, 'hello', 3.14]
a = [1, 2, ['lac', 'to', 'fit'], 3.14]
print(a)
print(type(a[2][2:]))
print(type(a[2][1:3]))


a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
print(a * 3)
# numpy의 경우에는 숫자 연산이 될 수도 있지만 파이썬의 list는 달라


# index로 list 값 변경
a[0] = 5
print(a)


# tuple
# () 활용하여 만들기

a = ()
print(type(a))

a = (1)
print(type(a))   # 숫자 하나만 하면 int형으로 인지
a = (1,)
print(type(a))   # 뒤에 콤마 하나 넣으면 tuple로 인지


a = (1, 2, 3)
print(a[0])   # tuple도 indexing, slicing 가능


# type casting => tuple을 list로 변환 가능
a = list(a)
print(type(a))