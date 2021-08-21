## Numpy 



#### Numpy란?

- **Numerial Python** (수치적 파이썬)

- Python에서 **대규모 다차원 배열***을 다룰 수 있게 도와주는 라이브러리  (*많은 2차원 이상의 데이터 나열)

- 주로 데이터 분석에서 데이터 셋을 효율적으로 다루기 위해 쓰임



#### 왜 Numpy?

- 반복문 없이 배열 처리 가능
- 파이썬 리스트에 비해, 빠른 연산을 지원하고 메모리를 효율적으로 사용



**list와 numpy 비교**



① 배열 생성 및 출력 형태



> list

```python
list_arr = list(range(5))

print(list_arr)
>>> [0, 1, 2, 3, 4]
print(type(list_arr))
>>> <class 'list'>
```

* 데이터가 콤마(,)로 구분
* class type은 list
* 1차원





> numpy

```python
import numpy as np
np_arr = np.array(range(5))

print(np_arr)
>>> [0 1 2 3 4]
print(type(np_arr))
>>> <class 'numpy.ndarray'>
```

- **ndarray** = n차원의 배열(n-diensional array)
- 데이터가 공백으로 구분
- class type은 numpy.ndarray
- n차원 



② 저장 가능한 데이터 타입



> list

```python
list_data = [1, 1.4, True, "S"]
```

- 다양한 데이터 타입 한번에 저장 가능



> numpy

```python
arr = np.array([0, 1, 2, 3, 4], dtype=float)

print(arr)
>>> [0. 1. 2. 3. 4]
print(arr.dtype)
>>> 'float64'
print(arr.astype(int))
>>> [0 1 2 3 4]
```

- 파이썬 리스트와 달리 **단일 데이터 타입**만 저장 가능

