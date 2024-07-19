
# JavaScript의 기초 2일차

## 목차

1. [객체](#객체-object)
2. [조건문](#조건문)
3. [반복문](#반복문)
4. [전개 구문](#전개-구문-spread-syntax)
5. [구조 분해 할당](#구조-분해-할당-destructuring)
6. [...의 중요성](#의-중요성)
7. [this](#this)
8. [this 사례 비교](#this를-사용할-때와-사용하지-않을-때의-차이를-비교해-드리겠습니다)

## 객체 (Object)

객체는 key와 값 가집니다.

* 객체 선언
  * 객체명 = { key1 : 값1 , key2 : 값2 }
* 객체 호출
  * 객체명[ key ]
  * 객체명.key

* 객체 추가, 수정
  * 객체명.key = 값;

* 객체 삭제
  * delete 객체명.key;

* 객체 검색
  * key in 객체명;

* 매서드
  1. Object.keys(객체명);
     * 객체의 key 들 배열로 반환
  2. Object.valus(객체명);
     * 객체의 valus 들 배열로 반환

## 조건문

조건문은 조건의 true, false로 조건문안에 코드를 실항 여부를 판단하는 문법 이다.

* 조건문 종류
  * if 문
    * if 조건 양식  

      ```js
      if (조건) { 
      실행 코드;
      return 반환값;
      }
      else if (다른 조건){
      실행 코드;
      }
      else {
      실행 코드;
      }
      ```

  * 문법 생략
    * 조건: 실행코드 1줄 일때

      ```js
      if (조건) 실행코드;
      ```

  * switch 문
    * switch 조건문 양식

      ```js
      switch (조건) {
        case 값1:
          실행코드
          break;
        case 값2:
          실행코드
          break;
        default:
          실행코드
          break;
      }
      ```

## 반복문

* 반복문 종류

* for 반목문 양식

     ```js
     for (휘발성 변수 선언& 초기값 설정; 조건 범위; 변수 증감) {
     1회 실행 코드;
     }
     ```

* for 반복문 종첩시 조건 변수 초기화 필요없다

* while 반복문 양식

     ```js
     조건 변수 선언;
     while (조건) {
     반복 코드;
     조건 변수 증감;// 조건 범위 벗어날때 까지 반복
     }
    ```

* while 반복문 종첨 조건 변수 초기화 해야 정상 작동

* 반복문 빠른 탈출 명령
  * break: 특정 조건에 빠른 탈출
  * continue: 특정 조건까지 생략, 범위 벗어날때 코드 실행

## 전개 구문 (Spread Syntax)

전개 구문은 배열이나 객체의 요소를 "펼치는" 기능을 합니다.

1. 배열에서의 사용:

   ```javascript
   const arr1 = [1, 2, 3];
   const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]
   ```

2. 객체에서의 사용:

   ```javascript
   const obj1 = { a: 1, b: 2 };
   const obj2 = { ...obj1, c: 3 }; // { a: 1, b: 2, c: 3 }
   ```

3. 함수 인자로 사용:

   ```javascript
   function sum(x, y, z) {
     return x + y + z;
   }
   const numbers = [1, 2, 3];
   console.log(sum(...numbers)); // 6
   ```

## 구조 분해 할당 (Destructuring)

구조 분해 할당은 배열이나 객체의 속성을 해체하여 그 값을 개별 변수에 담을 수 있게 하는 표현식입니다.

1. 배열 구조 분해:

   ```javascript
   const [a, b] = [1, 2];
   console.log(a); // 1
   console.log(b); // 2
   ```

2. 객체 구조 분해:

   ```javascript
   const { name, age } = { name: 'John', age: 30 };
   console.log(name); // 'John'
   console.log(age);  // 30
   ```

3. 함수 매개변수에서의 사용:

   ```javascript
   function greet({ name, age }) {
     console.log(`Hello, ${name}! You are ${age} years old.`);
   }
   greet({ name: 'Alice', age: 25 }); // "Hello, Alice! You are 25 years old."
   ```

## '...'의 중요성

1. 배열 복사 및 결합

   * '...' 사용:

     ```javascript
     const arr1 = [1, 2, 3];
     const arr2 = [...arr1, 4, 5];
     console.log(arr2); // [1, 2, 3, 4, 5]
     ```

   * '...' 미사용:

     ```javascript
     const arr1 = [1, 2, 3];
     const arr2 = [arr1, 4, 5];
     console.log(arr2); // [[1, 2, 3], 4, 5]
     ```

2. 객체 복사 및 병합

   * '...' 사용:

     ```javascript
     const obj1 = { a: 1, b: 2 };
     const obj2 = { ...obj1, c: 3 };
     console.log(obj2); // { a: 1, b: 2, c: 3 }
     ```

   * '...' 미사용:

     ```javascript
     const obj1 = { a: 1, b: 2 };
     const obj2 = { obj1, c: 3 };
     console.log(obj2); // { obj1: { a: 1, b: 2 }, c: 3 }
     ```

3. 함수 인자 전달

   * '...' 사용:

     ```javascript
     function sum(x, y, z) {
       return x + y + z;
     }
     const numbers = [1, 2, 3];
     console.log(sum(...numbers)); // 6
     ```

   * '...' 미사용:

     ```javascript
     function sum(x, y, z) {
       return x + y + z;
     }
     const numbers = [1, 2, 3];
     console.log(sum(numbers)); // "1,2,3undefinedundefined"
     ```

4. 나머지 매개변수 (Rest Parameters)

   * '...' 사용:

     ```javascript
     function myFunction(firstArg, ...restOfArgs) {
       console.log(firstArg); // 1
       console.log(restOfArgs); // [2, 3, 4, 5]
     }
     myFunction(1, 2, 3, 4, 5);
     ```

   * '...' 미사용:

     ```javascript
     function myFunction() {
       console.log(arguments[0]); // 1
       console.log(Array.from(arguments).slice(1)); // [2, 3, 4, 5]
     }
     myFunction(1, 2, 3, 4, 5);
     ```

## this

1. 기본 개념:
'this'는 간단히 말해서 "지금 이 코드가 누구의 것인지"를 가리키는 특별한 단어입니다. 하지만 이 "누구"가 상황에 따라 달라질 수 있어서 때로는 헷갈릴 수 있습니다.

    ```js
    javascriptCopyconst 고양이 = {
      이름: "나비",
      울기: function() {
        console.log(this.이름 + "가 야옹하고 웁니다.");
      }
    };
    고양이.울기(); // "나비가 야옹하고 웁니다."
    ```

2. 전역 컨텍스트:

   ```javascript
   console.log(this); // 브라우저에서는 Window 객체, Node.js에서는 global 객체
   ```

3. 함수 내부에서의 this:

   ```javascript
   function simpleFunction() {
     console.log(this);
   }
   simpleFunction(); // Window 객체 (strict mode에서는 undefined)
   ```

4. 메소드로서의 this:

   ```javascript
   const obj = {
     name: "MyObject",
     sayHello: function() {
       console.log("Hello, I'm " + this.name);
     }
   };
   obj.sayHello(); // "Hello, I'm MyObject"
   ```

5. 이벤트 핸들러에서의 this:

   ```javascript
   button.addEventListener("click", function() {
     console.log(this); // 클릭된 버튼 요소
   });
   ```

6. 생성자 함수에서의 this:

   ```javascript
   function Person(name) {
     this.name = name;
   }
   const john = new Person("John");
   console.log(john.name); // "John"
   ```

7. call, apply, bind 메소드:

   ```javascript
   function greet() {
     console.log("Hello, " + this.name);
   }
   const person = { name: "Alice" };
   greet.call(person); // "Hello, Alice"
   ```

8. 화살표 함수에서의 this:

   ```javascript
    const obj = {
    name: "MyObject",
    regularFunction: function() {
      console.log("Regular function:", this.name);
    },
    arrowFunction: () => {
      console.log("Arrow function:", this.name);
    }};
    
    obj.regularFunction(); // 출력: "Regular function: MyObject"
    obj.arrowFunction();   // 출력: "Arrow function: undefined"
    ```

이 예제에서 중요한 점은 다음과 같습니다:

1. 일반 함수(regularFunction)에서의 'this':
   * 일반 함수에서 'this'는 함수가 호출될 때 결정됩니다.
   * obj.regularFunction()으로 호출될 때, 'this'는 obj를 가리킵니다.
   * 따라서 this.name은 "MyObject"가 됩니다.

2. 화살표 함수(arrowFunction)에서의 'this':
   * 화살표 함수는 자신만의 'this'를 가지지 않습니다.
   * 대신, 화살표 함수는 그것이 정의된 곳의 'this'를 그대로 사용합니다.
   * 이 경우, 화살표 함수는 전역 스코프(브라우저에서는 window, Node.js에서는 global)에서 정의되었으므로, 'this'는 전역 객체를 가리킵니다.
   * 전역 객체에는 'name' 속성이 없으므로 (또는 빈 문자열), 'undefined'가 출력됩니다.

이 차이점 때문에 객체의 메소드로 화살표 함수를 사용할 때는 주의가 필요합니다. 객체의 속성에 접근해야 하는 메소드라면 일반 함수를 사용하는 것이 더 적절할 수 있습니다.

화살표 함수의 이런 특성은 특정 상황(예: 콜백 함수 내에서 외부 스코프의 'this'를 유지하고 싶을 때)에서는 매우 유용할 수 있지만, 객체의 메소드로 사용할 때는 예상치 못한 결과를 낳을 수 있습니다.

### 'this'를 사용할 때와 사용하지 않을 때의 차이를 비교해 드리겠습니다

 1. 객체 메서드
  
    * this 없을 때:

      ```javascript
      const 사람 = {
        이름: "홍길동",
        나이: 30,
        소개: function() {
          console.log("제 이름은 " + 사람.이름 + "이고, 나이는 " + 사람.나이 + "살입니다.");
        }
      };
      
      사람.소개(); // "제 이름은 홍길동이고, 나이는 30살입니다."
      ```

    * this 있을 때:

      ```javascript
      const 사람 = {
        이름: "홍길동",
        나이: 30,
        소개: function() {
          console.log("제 이름은 " + this.이름 + "이고, 나이는 " + this.나이 + "살입니다.");
        }
      };
      
      사람.소개(); // "제 이름은 홍길동이고, 나이는 30살입니다."
      ```

     차이점: 'this'를 사용하면 객체 이름을 직접 참조하지 않아도 되므로, 객체 이름이 변경되어도 메서드 내부 코드를 수정할 필요가 없습니다.

 2. 생성자 함수

    * this 없을 때:

      ```javascript
      function 사람(이름, 나이) {
        const 새사람 = {};
        새사람.이름 = 이름;
        새사람.나이 = 나이;
        새사람.소개 = function() {
          console.log("제 이름은 " + 새사람.이름 + "이고, 나이는 " + 새사람.나이 + "살입니다.");
        };
        return 새사람;
      }
      
      const 길동 = 사람("홍길동", 30);
      길동.소개(); // "제 이름은 홍길동이고, 나이는 30살입니다."
      ```

    * this 있을 때:

      ```javascript
      function 사람(이름, 나이) {
        this.이름 = 이름;
        this.나이 = 나이;
        this.소개 = function() {
          console.log("제 이름은 " + this.이름 + "이고, 나이는 " + this.나이 + "살입니다.");
        };
      }
      
      const 길동 = new 사람("홍길동", 30);
      길동.소개(); // "제 이름은 홍길동이고, 나이는 30살입니다."
      ```
  
    차이점: 'this'를 사용하면 새 객체를 명시적으로 생성하고 반환할 필요가 없어집니다. 'new' 키워드와 함께 사용하면 자동으로 새 객체가 생성되고   초기화됩니다.

 3. 생성자 함수

    * this 없을 때:

      ```javascript
      const 버튼 = document.querySelector("#myButton");
      버튼.addEventListener("click", function(event) {
        console.log("클릭된 버튼의 텍스트: " + event.target.textContent);
      });
      ```

    * this 있을 때:

      ```javascript
      const 버튼 = document.querySelector("#myButton");
      버튼.addEventListener("click", function() {
        console.log("클릭된 버튼의 텍스트: " + this.textContent);
      });
      ```

    차이점: 'this'를 사용하면 이벤트가 발생한 요소를 직접 참조할 수 있어, 코드가 더 간결해집니다.

결론:

* 'this'를 사용하면 코드의 재사용성과 유연성이 높아집니다.
* 객체 지향 프로그래밍에서 'this'는 더 직관적이고 효율적인 코드 작성을 가능하게 합니다.
* 그러나 'this'의 값이 컨텍스트에 따라 변할 수 있어 주의가 필요합니다.
* 'this'를 사용하지 않으면 때로는 코드가 더 명시적이고 예측 가능할 수 있지만, 재사용성과 유연성이 떨어질 수 있습니다.
