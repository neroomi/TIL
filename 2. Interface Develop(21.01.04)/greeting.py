
# comment -- 주석

'''
변수 - 데이터를 담는 공간 또는 그릇
함수 - 행위 (업무 로직 및 알고리즘)


클래스
- 변수
- 함수
- 생성자


python 장점
- 상대적으로 쉽다
- interactive
- 분석, 통계 관련 library 풍부
- Open Source(무료)
- R에 비해 범용적


python 단점
- 하위호환성이 없다

'''

# keyword module laoding
import keyword
print(keyword.kwlist)

# 변수의 생성 및 삭제
# 인터프리터 기반의 언어
# 변수 선언 방법
# -Camel Case : 함수 정의 시 많이 사용하는 방법 numberofCollegeGraduates
# -Pascal Case : 클래스 정의시 사용하는 방법 NumberofCaollegeGraduates
# -Snake Case : 권장하지 않음(강사 성향) number_of_college_graduates

# int a = 100
# a = 100
# print(a)

# del (a)
# print(a)


# python data type(Built-in Types)
# - Numeric
# - Sequence (list, tuple, range)
# - Text Sequence (str)
# - Mapping (dict)
# - Set (Set)
# - Bool (True(T), False(F), not, and, or(논리), &, :, ~(비교))
# - date, timedate (날짜)


# 허용하는 변수 선업 법 ( 숫자로 시작할 수 없어서 )
# 오직 두가지 _ , $
_age = 49


# 변수로 사용할 수 없는 예약어
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""


year = 2021
month = 1
day = 4

print(year, month, day)
#today = lamda x: print(year, month, day)
#today x

# seperator 옵션
print('p', 'y', 't', 'h', 'o', 'n')
print('p', 'y', 't', 'h', 'o', 'n', sep="")
print('010', '4603', '2283', sep="-")
print('naver', 'kakako', 'samsung', sep='\n')

"""
참고 : Escape 코드
\n : 개행
\t : 탭 
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""


# end 옵션(print - println)
print('Welcome To', end=' ')
print('IT News', end=' ')
print('Web Sites')


# format 사용법(d, s, f)

one = 1
two = 2
print(one, two)
print('%d %d' % (one, two))

one = 'one'
two = 'two'
print('%s %s' % (one, two))      # 자릿수 제한 있을 때 활용

print( '{1} {0}'.format(one, two))  # 여러 개의 변수를 합쳐서 하나의 문장을 만들어낼 때 유용

print( '%10s' % ('hamburger', ))
print( '%10s' % ('nice', ))
print( '%-10s' % ('nice', ))

print('%1.8f' % (3.14159343493580348))
print('{:1.8f}'.format(3.14159343493580348))

