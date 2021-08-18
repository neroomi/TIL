**[Python]**



## 매개변수와 인자



### 매개변수(parameter)

**함수 정의시** 사용되는 변수(variable)

```python
def addNumber(a, b):
    return a + b
```

이 때, `a, b`가 **매개변수**이다. 




### 인자(argument)

**함수 호출시** 함수로 넘겨주는 자료, 값(value)

```python
addNumber(2, 5)
```

여기에선 `2, 5`가 인자가 된다.

즉, 정의된 함수로 넘겨주는 실제 자료를 **인자**라고 한다.






## 사용자 함수 정의(return과 print)



우선 프로그래밍의 작동원리를 살펴보면 

무언가를 **입력**했을 때, 컴퓨터는 **기능**을 통해 어떤 결과를 **출력**한다. 

이 때, 특정기능을 수행하는 코드 혹은 코드의 모임을 **함수**라고 한다.



python에선 이미 개발자들이 만들어 둔 **내장함수**를 편하게 가져다 쓸 수 있다.

대표적으로 입출력 함수를 예시로 들면 다음과 같다.

`input()` - 자료를 입력하는 함수
`print()` - 자료를 출력하는 함수



사용자는 `def`를 이용해 **사용자 정의 함수**를 만들 수도 있다.

```python
def 함수이름(매개변수):
	수행할 명령
	코드들의 모임
	...
	return 반환값
```

즉 **매개변수**를 통해 *입력*하면 함수 속 코드가 *기능(작동)*하여 **return**을 통해 *반환(출력)*된다.



함수 내부에서 일어난 일은 함수 외부에서는 알 수 없기 때문에 반환을 통해 외부로 전달한다.

하지만 주의할 점은 이를 출력으로 보여주지 않으면 함수가 기능은 하지만 사용자 눈으로 확인은 할 수 없다.

다음의 예시를 보자.



```python
def plus(a, b):
    c = a + b
    return c
```



위의 코드를 통해 다음의 두 가지를 실행하면 어떤 결과값이 나올까? (둘의 결과값은 같을까?)

1. `plus(3, 4)`
2. `print(plus(3, 4))`



정답은 No. 

1번은 화면에 아무것도 출력되지 않고

2번은 화면에 7이 출력된다.



1번은 plus 함수를 통해 7이라는 값을 반환하지만 화면에 출력하는(보여주는) 함수를 사용하지 않았기 때문에 우리가 보는 화면에는 보이지 않는 것이다.



반면, 2번의 경우에는 plus 함수가 반환한 값 7을 화면에 출력하는 코드 `print()`를 사용했기 때문에 화면에 `plus(3 ,4)`의 반환값 7이 출력되는 것이다.



---



##### 함수정의 시 `print()`와 `return`의 개념을 헷갈리는 경우가 많다.



만약 함수의  `return`(반환값)이 없으면 이를 print 했을 때 `None`이 출력된다.

```python
def plus(a, b):
    c = a+b
```

```python
print(plus(3, 4))
>>> None

plus(3, 4)
>>> 아무것도 출력되지 않음
```



반면 함수 내용 자체에 `print()`가 있는 경우를 보자.

​	(1) 반환값이 없는 경우

```python
def plus(a, b):
    c = a+b
    print(c)
```

```python
plus(3, 4)
>>> 7

print(plus(3, 4))
>>> 7
>>> None
```



​	(2) 반환값이 있는 경우

```python
def plus(a, b):
    c = a+b
    print(c)
    return c
```

```python
plus(3, 4)
>>> 7

print(plus(3, 4))
>>> 7   # 함수 속 print에 의한 출력
>>> 7   # return에 의한 출력
```



함수를 print() 했을 때, 함수 내 기능(print())에 의한 값이 먼저 출력되며, 이후 return 값이 없는 경우 반환값이 None으로 출력되고 있는 경우 해당 return 값이 차례로 출력된다.





---



### 기본 인수

`addto`를 이용해 기본값으로 지정해둔 매개변수가 있다면 인자(인수)를 모두 넘겨주지 않아도 된다.

```python
def add(a, addto=1):
	return a + addto


result1 = add(10)
result2 = add(10, 5)

print(result1)
>>> 11
print(result2)
>>> 15
```



주의할 점은 `addto`를 이용한 기본값을 가지는 매개변수는 맨 마지막에 위치해야 한다.

```python
def add(addto=1, a):
	return a + addto

result3 = add(10)

print(result3)
>>> SyntaxError: non-default argument follows default argument
```







### 가변인수 리스트



함수 설계 시, 몇 개의 인자를 받게될 지 모르는 때가 있다.

이 때, 내장 함수를 이용해 가변으로 받는 인자를 배열이나 리스트로 선언하여 넘길 수 있다. 

고정 인수를 나열 후, 나머지는 **튜플(Tuple)**형식으로 한꺼번에 받을 수 있다.

```python
def argsList(a, *args):
    print(a, args)
    
argsList(1)
>>> 1 ()
argsList(1, 2, 3, 4)
>>> 1 (2, 3, 4)
argsList(1, 'a', [1, 2, 3], {1:'a', 2:'b'})
>>> 1, ('a', [1, 2, 3], {1:'a', 2:'b'})
```



당연히 함수 정의를 통해 하나씩 나오게 할 수도 있다.

```python
def argsList(a, *args):
    print(a)
    for arg in args:
        print(arg)
    
argsList(1)
>>> 1
argsList(1, 2, 3)
>>> 1
>>> 2
>>> 3
argsList(1, 'a', [1, 2, 3], {1:'a', 2:'b'})
>>> 1
>>> 'a'
>>> [1, 2, 3]
>>> {1:'a', 2:'b'}
```





## 함수와 메서드



### 함수

앞서 말한 바와 같이 함수는 **특정 기능**을 한다.

(매개변수를 이용해 자료를 전달해준다)

```python
my_list = [1, 2, 3]
len(my_list)
sum(my_list)
min(my_list)
```

`함수(매개변수)`의 형태



### 메서드

반면 메서드는 **특정 자료(객체)**와 연관지어 기능을 한다.

(따라서 자료 뒤에 `.`을 찍어 사용한다)

```python
my_list = [1, 2, 3]
my_list.sort()
my_list.pop()
my_list.clear()
```

