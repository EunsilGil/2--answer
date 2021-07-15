# **YMB COS Pro (파이썬 치트시트)**


## 표기법 설명

 `<id>` : identifier, 식별자

`<expr>` : expression, 식

`<stmt>` : statement, 문

----


## 변수 선언문, 대입문  
`<id> = <expr>`

	ex)
	name = “파이썬"  
	age = 10
  
  
	age += 1 >> 1 증가  
	age -= 2 >> 2 감소  
	age *= 3 >> 3 배  
	age /= 4 >> 4로 나눔  

----
## 연산자  
### 산술연산자

| 연산자 | 뜻 | 예제 | 결과 |
|:------:|:-----:|:------:|:------:|
| + |덧셈|1 + 1|2|
|-|뺄셈|1 - 1|0|
|*|곱셈|1 * 1|1|
|/|나눗셈|3 / 2|1.5|
|//|몫|3 // 2|1|
|%|나머지|3 % 2|1|
|**|제곱|5 ** 2|25|



### 비교연산자
| 연산자 | 뜻 | 예제 | 결과 |
|:------:|:-----:|:------:|:------:|
|==|같다|3 == 4|False|
|!=|다르다|3 != 4|True|
|>|크다|3 > 4|False|
|<|작다|3 < 4|True|
|>=|크거나같다|3 >= 3|True|
|<=|작거나같다|3 <= 4|True|


### 논리연산자
| 연산자 | 뜻 | 예제 | 결과 |
|:------:|:-----:|:------:|:------:|
|and|둘 다 참이면 참|True and False|False|
|or|둘 중 하나라도 참이면 참|True or False|True|
|not|참이면 거짓, 거짓이면 참|not True|False|

----


## 리스트

numbers = [ 1, 2, 3, 4, 5 ]  
empty = []  ( 빈 리스트)

### 인덱스
  *  0부터 시작하는 원소의 번호
  *  0 ~ (len(리스트) - 1) 까지  

	[자주 사용되는 expr] 
	numbers[0] == 1 >> 첫번째 원소
	numbers[3] == 4 >>  네번째 원소
	numbers[-1] == 5 >> 뒤에서 첫번째 원소
	numbers[1:3] => [2,3] 출력 >> 슬라이싱, [시작:끝:스텝] 
	numbers[::-1] => [5,4,3,2,1] 출력 >> 뒤집기

	len(numbers) == 5 ( 리스트의 길이 구하기 )

	numbers.append(6) => [1,2,3,4,5,6] 출력 >> 맨 뒤에 추가하기
	numbers.pop() => [1,2,3,4,5] 출력 >> 맨 뒤에서부터 빼기

----


## 조건문
* 조건에 따른 실행  
#### 패턴
	if <expr>:
		참이면 실행할 <stmt>
	--------------------------

	if <expr>:
		<stmt>
	else:
		<stmt>
	--------------------------	
	if <expr>:
		<stmt>
	elif <조건2>:
		<stmt>
	…
	elif <expr>:
		<stmt>
	else:
		<stmt>

----

## 반복문
### while 반복문

		while <expr>:
			<stmt>

### for 반복문
* 순서가 중요할 때는 range
* 순서가 필요 없을 땐 <배열,문자열>

		for <id> in <expr>:
			<stmt>

		for <id> in range(<expr>):
			<stmt>



**예시** 
	
	for i in range(n, m):  
		n 부터 m - 1 까지 하나씩 i 에 저장해 실행`
----

## 함수
### 기본함수

	def <id>(<id>, <id>, ...):
		<stmt>
--------------
### 값을 반환하는 함수
	def func1(인자1, … , 인자n):
		<stmt>
		return <expr>
--------------
### 함수의 호출
	<id>(<expr>, ...) 
	>> 값을 반환하면 그 값, 안하면 None
-----
---

## 한 줄 수정하기
`기회가 여러 번 있기 때문에 아래 조건들을 하나씩 해보면서 답을 찾아 보세요!!`
* 부등호 고치기
  * \>, >=, <, <=, ==, !=
* and or 바꾸기
* if 가 두 개 있는 경우
  * if <-> elif 바꾸기
* continue <-> break 바꾸기
* range(len(xxx)) <-> range(1, len(xxx)) 바꾸기
* 수학 공식 확인 
  * ex) average = total / len(xxx) 
* 리스트의 인덱스를 꼼꼼하게 확인하기!

---
## 빈칸채우기 패턴


### 합 구하기
``` 
def func(arr):
	sum = 0
	for i in range(len(arr)):
		sum += arr[i] 	

	return sum
```

OR
```
def func(arr):
	sum = 0
	for i in arr:
		sum += i
	
	return sum
```



### 최대값 구하기
```
def func(arr):
	max = -9999
	for i in arr:
		if max < i:
			max = i

	return max
```


### 최소값 구하기

```
def func(arr):
	min = 9999
	for i in arr:
		if min > i:
			min = i

	return min
```
### 리스트에서 n 제외하기
```
def func(arr, n):
	result = []
	for i in arr:
		if i != n:
			result.append(i)

	return result
```

### 차이 구하기

```
def func(a, b):
	if a > b:
		return a - b
	else:
		return b - a
```

### 개수 세기
```
def func(arr):
	count = [ 0 for i in range(1000) ]
	for i in arr:
		count[i] += 1
	
	return count
```

### 각 자리수 합 구하기
```
def func_c(n):
	ret = 0
	while n > 0:
		ret += n%10  # n % 10 는 현재 자리의 숫자를 뜻함
		n //= 10
	return ret
```