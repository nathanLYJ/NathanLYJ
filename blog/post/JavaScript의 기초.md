## 목차
1. [JavaScript의 기초](#javascript의-기초)
2. [실습 도우미 DOM](#실습-도우미-dom)
3. [변수 선언 및 사용](#javascript-변수-선언-및-사용)
4. [원시 타입](#원시-타입)
5. [문자열 (String)](#문자열-string)
6. [숫자 (Number)](#숫자-number)
7. [논리 자료형 (Boolean)](#논리-자료형-boolean)
8. [함수 (Function)](#함수-function)
9. [객체 타입](#객체-타입)

# JavaScript의 기초

## 개요
- 1995년 브랜든 아이크에 의해 개발됨
- 주요 역할: HTML과 CSS를 프로그래밍적으로 제어

## JavaScript의 특징
- 웹 브라우저 환경 외에도 다양한 분야에서 활용 (예: 게임 서버)
- 웹어셈블리(WebAssembly)도 웹 프로그래밍에 사용됨

## 역사
- 초기 이름 변경: Mocha > LiveScript > JavaScript
- 현재 ECMAScript 2021(ES12)까지 발표됨

## JavaScript의 주요 기능

### 1. 데이터 저장
- 변수 선언: `var`, `let`, `const`
- 저장 가능한 데이터 타입:
  - 숫자
  - 문자열
  - 빈 값 (`null`, `undefined`)
  - 불리언 (Boolean)
  - 배열
  - 객체

### 2. 값 연산
- 사칙 연산
- 논리 연산
- 조건문
- 반복문
- 자료형의 내장 함수

### 3. 결과 반영
- DOM (Document Object Model) API 사용
- BOM (Browser Object Model) API 사용
- 사용자 반응 처리
- 연산 결과 값 반영

### 4. 통신
- 다른 디바이스와의 통신 기능

# 실습-도우미-dom

## 웹에서 DOM 호출하는 명령어

### 브라우저 오브젝트 모델 (BOM) 관련 명령어

- `window.alert()`
  - 브라우저에 알림 메시지를 표시하는 대화 상자를 띄웁니다.

- `window.prompt()`
  - 사용자로부터 입력을 받을 수 있는 대화 상자를 띄웁니다.

- `window.confirm()`
  - 사용자에게 확인이나 취소를 요청하는 대화 상자를 띄웁니다.
  - 'true' 또는 'false' 값을 반환합니다.
  - 예: "~~에 동의 합니까?"

### 콘솔 관련 명령어

- `console.log()`
  - 콘솔 창에 일반 메시지를 출력합니다.

- `console.error()`
  - 콘솔 창에 에러 메시지를 출력합니다.

- `console.table()`
  - 콘솔 창에 데이터를 테이블 형태로 출력합니다.
  - 예: `console.table({'one':1,'two':2})`

이러한 명령어들은 웹 개발 과정에서 디버깅, 사용자 상호작용, 데이터 시각화 등 다양한 목적으로 사용됩니다.

## JavaScript 변수 선언 및 사용

### 변수 선언 방법

1. `let`
   - 블록 스코프 변수
   - 재할당 가능
   - 블록 {} 밖에서 호출 불가
   
2. `const`
   - 블록 스코프 상수
   - 재할당 불가
   - 블록 {} 밖에서 호출 불가
   - 현업에서 많이 사용됨

3. `var` (권장하지 않음)
   - 함수 스코프 변수
   - 재할당 가능
   - 블록 {} 밖에서도 호출 가능
   - 초기화가 필요 없음
   - 선언이 겹쳐 이전 코드에 문제를 일으킬 수 있음

4. 변수 타입 확인
   ```javascript
   typeof(값 또는 변수)
   ```

### 변수와 값의 관계

변수는 값의 주소를 가리킵니다:

```javascript
let x = 10
let y = x  // y = 10 (y는 x를 참조하는 것이 아님)
let z = y  // z = 10

y = 20
console.log(z)  // 출력: 10 (z는 여전히 10)
```

### 변수 이름 짓기 규칙

1. 특수문자 사용 가능하나 권장하지 않음
2. 숫자로 시작할 수 없음
3. 예약어(키워드, 함수명 등)는 사용할 수 없음
4. 대소문자 구분됨
5. 관습:
   - 첫 문자는 소문자
   - 사용하지 않는 변수는 `_`로 시작
   - 클래스명은 첫 문자를 대문자로
   - 주로 카멜 표기법 사용 (예: `myVariableName`)

### 변수의 타입

JavaScript는 동적 타입 언어로, 변수의 타입을 자동으로 구분합니다.

```javascript
typeof(값 또는 변수)  // 타입 출력
```

### 변수 값 변경

```javascript
변수명 = 새로운 값
```

이러한 개념들은 JavaScript 프로그래밍의 기초를 이루며, 코드 작성 시 변수의 효과적인 사용과 관리에 중요합니다.

## 원시 타입

JavaScript에는 7가지 원시 타입이 있습니다: string, number, bigint, boolean, undefined, symbol, null

### 타입 확인

- `Object.prototype.toString.call()` 메서드를 사용하여 타입을 확인할 수 있습니다.
- 타입 체크 함수 예시:

```javascript
function typeCheck(value) {
    const return_value = Object.prototype.toString.call(value);
    const type = return_value.substring(
        return_value.indexOf(" ") + 1,
        return_value.indexOf("]")
    );
    return type.toLowerCase();
}
```

### 원시 타입의 특징

- 원시 타입의 값은 불변(immutable)입니다.

## 문자열 (String)

### 문자열 생성

- 작은따옴표(`''`), 큰따옴표(`""`), 백틱(` `` `)으로 문자열을 생성할 수 있습니다.
- 템플릿 리터럴 사용 (백틱 사용 시):

```javascript
let name = 'Jack'
let age = 15
let text = `안녕하세요 저는 ${name}이라고 합니다, 제 나이는 ${age}입니다`
```

### 특수 문자

- `\n`: 줄바꿈
- `\t`: 탭
- `\`: 특수문자 앞에 사용하여 해당 문자를 출력

### 문자열 특징

1. 인덱스로 접근 가능 (0부터 시작)
2. `length` 속성으로 길이 확인 가능
3. 불변성: 한 번 생성된 문자열은 변경 불가능

```javascript
let 불멸자 = "immortal";
불멸자[0] = 'l';
console.log(불멸자);  // 여전히 "immortal"
```

4. 문자열 연결: `+` 연산자 사용

```javascript
let lyrics1 = '광야로 걸어가 ';
let lyrics2 = '알아 네 home ground';
console.log(lyrics1 + lyrics2);  // "광야로 걸어가 알아 네 home ground"
```

### 문자열 메서드

1. `indexOf('찾을 문자', 시작 위치)`: 문자열 검색
2. `replace('변경할 문자','변경 될 문자')`: 첫 번째 일치 항목 대체
3. `slice(start, end)`: 부분 문자열 추출
4. `split('기준')`: 문자열을 배열로 분할
5. `toLowerCase()`, `toUpperCase()`: 대소문자 변환
6. `trim()`: 앞뒤 공백 제거
7. `length`: 문자열 길이 확인

예시:
```javascript
'010-0000-0001'.split('-')[2]  // "0001"
```

이러한 문자열 조작 방법들은 JavaScript에서 텍스트 데이터를 다룰 때 매우 유용합니다.

## 숫자 (Number)

JavaScript에서 숫자 처리는 다른 많은 프로그래밍 언어와 다른 독특한 특징이 있습니다.

### JavaScript의 숫자 타입 특징

1. **단일 숫자 타입**: JavaScript는 정수, 실수, 소수를 모두 하나의 'Number' 타입으로 표현합니다.

2. **64비트 부동소수점**: 모든 숫자는 내부적으로 64비트 부동소수점 형식(IEEE 754 표준)으로 표현됩니다.

3. **정밀도**: 정수는 -(2^53 - 1)부터 (2^53 - 1) 사이에서 정확하게 표현됩니다.

예시:
```javascript
let integerNumber = 42;
let floatNumber = 3.14;
let scientificNotation = 5e-4;  // 0.0005

console.log(typeof integerNumber);  // "number"
console.log(typeof floatNumber);    // "number"
console.log(typeof scientificNotation);  // "number"
```

### 주의사항

1. **정밀도 손실**: 매우 큰 숫자나 매우 작은 소수를 다룰 때 정밀도 손실이 발생할 수 있습니다.

2. **특별한 값들**:
   - `Infinity`: 양의 무한대
   - `-Infinity`: 음의 무한대
   - `NaN`: 'Not a Number', 잘못된 연산 결과를 나타냄

3. **BigInt**: ES2020부터 도입된 새로운 원시 타입으로, 아주 큰 정수를 다룰 때 사용합니다.

```javascript
let bigNumber = 1234567890123456789012345678901234567890n;  // 끝에 'n'을 붙여 BigInt로 표현
```

### 산술 연산

- 기본 연산: `+`, `-`, `*`, `/`
- 승수 연산: `**` (예: `10 ** 3 = 1000`, `10 ** 0.5 = 2` (제곱근))
- 나머지 연산: `%`
- 음수 표시: `-2`, 음수의 음수 표시: `-(-2)`
- 증감 연산자: `++`, `--`
  - 전위 연산자 (`++x`, `--x`): 즉시 증가/감소 후 반환
  - 후위 연산자 (`x++`, `x--`): 현재 값 반환 후 증가/감소

예제:
```javascript
let a = 5, b = 5;
console.log(++a);  // 6
console.log(b++);  // 5
console.log(b);    // 6

let x = 3;
let y = ++x * 2;   // x는 4, y는 8
let p = 3;
let q = p++ * 2;   // q는 6, 그 후 p는 4
```

- 비교 연산자: `>`, `>=`, `<`, `<=`, `==`(타입 무시), `!=`, `===`(타입까지 확인), `!==`
- 특수 값: `Infinity` (양의 무한), `-Infinity` (음의 무한)
- 지수 표기법: `3e10` = 3 * 10^10

## 증감 연산자

증감 연산자는 변수의 값을 1 증가시키거나 감소시키는 연산자입니다. JavaScript에서는 `++`(증가)와 `--`(감소) 두 가지 증감 연산자를 제공합니다.

### 증감 연산자의 위치

증감 연산자는 변수의 앞(전위)이나 뒤(후위)에 위치할 수 있으며, 위치에 따라 동작이 달라집니다.

1. **전위 연산자** (++x 또는 --x):
   - 변수의 값을 즉시 증가/감소시킨 후, 해당 줄의 나머지 연산을 수행합니다.
   - 증가/감소된 값이 즉시 반환됩니다.

2. **후위 연산자** (x++ 또는 x--):
   - 해당 줄의 다른 연산을 모두 수행한 후에 변수의 값을 증가/감소시킵니다.
   - 증가/감소되기 전의 원래 값이 반환됩니다.

### 예제

```javascript
let a = 5;
let b = 5;

console.log(++a);  // 출력: 6 (a의 값이 즉시 증가하고 그 값이 출력됨)
console.log(a);    // 출력: 6 (a는 이미 증가된 상태)

console.log(b++);  // 출력: 5 (b의 원래 값이 출력된 후 b가 증가됨)
console.log(b);    // 출력: 6 (이제 b가 증가된 상태)

// 복합 예제
let x = 3;
let y = ++x * 2;   // x는 즉시 4가 되고, y는 8이 됩니다 (4 * 2)

let p = 3;
let q = p++ * 2;   // q는 6이 되고 (3 * 2), 그 후 p가 4가 됩니다
```

### 주의사항

- 증감 연산자를 사용할 때는 코드의 가독성을 고려해야 합니다. 복잡한 표현식 내에서 증감 연산자를 사용하면 코드를 이해하기 어려워질 수 있습니다.
- 가능하면 별도의 줄에서 증감 연산을 수행하는 것이 코드의 명확성을 높일 수 있습니다.

```javascript
// 권장하지 않는 방식
let result = ++x + y--;

// 더 명확한 방식
x++;
let result = x + y;
y--;
```

증감 연산자의 동작을 정확히 이해하면 더 효율적이고 간결한 코드를 작성할 수 있지만, 과도한 사용은 코드의 복잡성을 증가시킬 수 있으므로 적절히 사용하는 것이 중요합니다.

### 숫자 메소드

1. `parseInt()`, `parseFloat()`: 문자열을 정수 또는 실수로 변환
2. `toString()`: 숫자를 문자열로 변환 (예: `(42).toString()`)
3. `Number.isNaN()`: 값이 NaN인지 확인

### Math 내장 객체

1. `Math.PI`: 원주율(π)
2. `Math.round(숫자)`: 반올림
3. `Math.pow(숫자, 승수)`: 거듭제곱
4. `Math.sqrt(숫자)`: 제곱근
5. `Math.abs(숫자)`: 절댓값
6. `Math.random()`: 0과 1 사이의 난수 생성
7. `Math.max()`: 최대값
8. `Math.min()`: 최소값

이러한 특징과 메소드들을 이해하면 JavaScript에서 숫자를 효과적으로 다룰 수 있습니다.



## 논리 자료형 (Boolean)

Boolean 타입은 `true` 또는 `false` 두 가지 값 중 하나만을 가질 수 있는 자료형입니다. 주로 조건문(if)의 조건으로 사용되며, 프로그램의 흐름을 제어하는 데 중요한 역할을 합니다.

### 비교 연산자

비교 연산자는 두 값을 비교하여 Boolean 값을 반환합니다.

- `>` : 크다
- `>=` : 크거나 같다
- `<` : 작다
- `<=` : 작거나 같다
- `==` : 동등하다 (타입 무시)
- `!=` : 동등하지 않다 (타입 무시)
- `===` : 일치한다 (타입까지 확인)
- `!==` : 일치하지 않는다 (타입까지 확인)

예시:
```javascript
console.log(5 > 3);   // true
console.log(5 == "5");  // true
console.log(5 === "5");  // false
```

### 논리 연산자

논리 연산자는 Boolean 값들을 조합하여 새로운 Boolean 값을 생성합니다.

1. `&&` (논리곱, AND)
   - 두 조건이 모두 참일 때만 `true`를 반환합니다.
   - 하나라도 거짓이면 `false`를 반환합니다.

   ```javascript
   console.log(true && true);   // true
   console.log(true && false);  // false
   console.log(false && true);  // false
   console.log(false && false); // false
   ```

2. `||` (논리합, OR)
   - 두 조건 중 하나라도 참이면 `true`를 반환합니다.
   - 두 조건이 모두 거짓일 때만 `false`를 반환합니다.

   ```javascript
   console.log(true || true);   // true
   console.log(true || false);  // true
   console.log(false || true);  // true
   console.log(false || false); // false
   ```

3. `!` (부정, NOT)
   - 주어진 Boolean 값의 반대 값을 반환합니다.

   ```javascript
   console.log(!true);   // false
   console.log(!false);  // true
   ```

### 주의사항

1. 단락 평가 (Short-circuit Evaluation)
   - `&&`와 `||` 연산자는 왼쪽에서 오른쪽으로 평가되며, 결과가 확정되면 나머지 표현식은 평가하지 않습니다.

   ```javascript
   console.log(false && someFunction());  // false (someFunction은 호출되지 않음)
   console.log(true || someFunction());   // true (someFunction은 호출되지 않음)
   ```

2. Truthy와 Falsy
   - JavaScript에서는 Boolean 타입이 아닌 값도 조건문에서 `true` 또는 `false`로 평가될 수 있습니다.
   - Falsy 값: `false`, `0`, `''` (빈 문자열), `null`, `undefined`, `NaN`
   - 그 외의 값들은 모두 Truthy로 평가됩니다.

   ```javascript
   if (1) {
     console.log("This will be printed");  // 1은 Truthy
   }

   if (0) {
     console.log("This won't be printed");  // 0은 Falsy
   }
   ```

논리 연산자와 Boolean 타입을 잘 이해하면 복잡한 조건문을 효과적으로 작성할 수 있으며, 프로그램의 흐름을 정확하게 제어할 수 있습니다.

## 함수 (Function)

함수는 반복되는 작업을 단순화하고 코드를 구조화하는 데 사용되는 중요한 개념입니다.

### 함수 구조

기본적인 함수의 구조는 다음과 같습니다:

```javascript
function 함수명(parameter1, parameter2, ...) {
    // 실행 코드
    return 반환값;
}
```

함수 사용 (호출):
```javascript
함수명(argument1, argument2, ...);
```

예시:
```javascript
function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("Alice"));  // 출력: Hello, Alice!
```

### 함수의 장점

1. **재사용성**: 한 번 정의한 함수를 여러 번 사용할 수 있습니다.
2. **유지보수**: 함수 내부의 코드만 수정하면 되므로 유지보수가 용이합니다.
3. **구조 파악**: 복잡한 로직을 함수로 분리하면 전체 코드의 구조를 쉽게 파악할 수 있습니다.

### 화살표 함수 (Arrow Function)

ES6에서 도입된 화살표 함수는 함수를 더 간결하게 작성할 수 있게 해줍니다.

기본 문법:
```javascript
let 함수명 = (parameter1, parameter2, ...) => 표현식;
```

예시:
1. 기존 함수 표현:
   ```javascript
   let sum = function(x, y) {
       return x + y;
   };
   ```

2. 화살표 함수로 변환:
   ```javascript
   let sum = (x, y) => x + y;
   ```

3. 여러 줄의 코드가 필요한 경우:
   ```javascript
   let sum = (x, y) => {
       let result = x + y;
       console.log(`${x} + ${y} = ${result}`);
       return result;
   };
   ```

### 주의사항

1. **파라미터와 아규먼트**: 
   - 파라미터(Parameter)는 함수 정의 시 사용되는 변수입니다.
   - 아규먼트(Argument)는 함수 호출 시 전달되는 실제 값입니다.

2. **return 문**:
   - `return`문은 함수의 실행을 종료하고 값을 반환합니다.
   - `return`문이 없으면 함수는 `undefined`를 반환합니다.

3. **함수 스코프**:
   - 함수 내부에서 선언된 변수는 함수 외부에서 접근할 수 없습니다.

4. **화살표 함수의 this**:
   - 화살표 함수는 자신만의 `this`를 생성하지 않고, 외부 스코프의 `this`를 사용합니다.


## 객체 타입

객체 타입은 원시 타입과 달리 값을 변경할 수 있습니다.

### 배열 (Array)

배열은 여러 값을 순서대로 저장하는 객체 타입입니다.

#### 배열 선언

```javascript
const arr1 = [];
const arr2 = [1, 2, 3];
const arr3 = new Array(4, 5, 6);
const arr4 = new Array(3);  // 길이가 3인 빈 배열
const arr5 = Array.from('hello');  // ['h', 'e', 'l', 'l', 'o']
```

#### 배열의 특징

1. 인덱스를 통한 접근: 배열의 각 요소는 0부터 시작하는 인덱스를 통해 접근할 수 있습니다.
2. 다차원 배열: 배열 안에 배열을 포함할 수 있습니다.

```javascript
const arr = [
    [1, 2],
    [3, 4],
    [5, [10, 20, 30, [100, 200]]]
];
console.log(arr[2][1][3][0]);  // 100
```

3. 참조 타입: 배열을 다른 변수에 할당하면 참조가 복사됩니다.

```javascript
let arr1 = [1, 2, 3];
let arr2 = arr1;
arr1[0] = 10;
console.log(arr2);  // [10, 2, 3]
```

#### 배열 메소드

1. `push(item)`: 배열 끝에 항목 추가
2. `pop()`: 배열 끝 항목 제거 및 반환
3. `shift()`: 배열 첫 항목 제거 및 반환
4. `unshift(item)`: 배열 앞에 항목 추가
5. `splice(start, deleteCount, items...)`: 배열의 기존 요소를 삭제 또는 교체하거나 새 요소를 추가
6. `slice(start, end)`: 배열의 일부를 추출, 원본 배열은 변경되지 않음
7. `sort()`: 배열 정렬. 기본적으로 유니코드 순서로 정렬됨
   ```js
   arr.sort((a, b) => a - b);  // 오름차순 정렬
   arr.sort((a, b) => b - a);  // 내림차순 정렬
   ```
8. `includes(item)`: 배열에 특정 요소가 포함되어 있는지 확인
9. `join(separator)`: 배열의 모든 요소를 연결해 하나의 문자열로 만듦

### forEach() 메소드

`forEach()` 메소드는 배열의 각 요소에 대해 주어진 함수를 실행합니다.

#### 기본 구문

```javascript
array.forEach(function(currentValue, index, array) {
    // 실행할 코드
});
```

- `currentValue`: 현재 처리 중인 요소
- `index`: 현재 요소의 인덱스
- `array`: forEach()를 호출한 배열

#### 예제

1. 배열의 모든 요소 출력:
   ```javascript
   const fruits = ['apple', 'banana', 'cherry'];
   fruits.forEach(fruit => console.log(fruit));
   ```

2. 배열의 합계 구하기:
   ```javascript
   let sum = 0;
   [1, 2, 3, 4, 5].forEach(num => sum += num);
   console.log(sum);  // 15
   ```

#### 특징
- 배열을 변경하지 않습니다.
- 모든 요소를 순회합니다 (중간에 중단할 수 없음).
- 새로운 배열을 반환하지 않습니다.

### map() 메소드

`map()` 메소드는 배열의 모든 요소에 대해 주어진 함수를 호출한 결과로 새로운 배열을 생성합니다.

#### 기본 구문

```javascript
const newArray = array.map(function(currentValue, index, array) {
    // 반환할 요소
});
```

#### 예제

1. 숫자 배열의 각 요소를 두 배로:
   ```javascript
   const numbers = [1, 2, 3, 4, 5];
   const doubled = numbers.map(num => num * 2);
   console.log(doubled);  // [2, 4, 6, 8, 10]
   ```

2. 객체 배열에서 특정 속성만 추출:
   ```javascript
   const users = [
       { name: 'Alice', age: 25 },
       { name: 'Bob', age: 30 }
   ];
   const names = users.map(user => user.name);
   console.log(names);  // ['Alice', 'Bob']
   ```

#### 특징
- 새로운 배열을 반환합니다.
- 원본 배열은 변경되지 않습니다.
- 각 요소에 대해 변환 작업을 수행할 때 유용합니다.

`forEach()`와 `map()`의 주요 차이점은 `map()`이 새로운 배열을 반환한다는 점입니다. 데이터 변환이 필요한 경우 `map()`을, 단순히 각 요소에 대해 작업을 수행해야 할 경우 `forEach()`를 사용하는 것이 적합합니다.
