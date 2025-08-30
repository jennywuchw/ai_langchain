# Python 基礎教學：變數與數學運算

## 目錄
1. [變數的概念](#變數的概念)
2. [變數的命名規則](#變數的命名規則)
3. [基本資料型別](#基本資料型別)
4. [數學運算](#數學運算)
5. [練習題](#練習題)

---

## 變數的概念

### 什麼是變數？
變數就像是一個**容器**，用來儲存資料。在Python中，我們可以將資料指派給變數，之後就可以透過變數名稱來存取這些資料。

### 變數的基本語法
```python
變數名稱 = 值
```

**範例：**
```python
name = "小明"
age = 18
height = 175.5
is_student = True
```

---

## 變數的命名規則

### 命名規則
1. **只能包含**：英文字母、數字、底線(_)
2. **不能以數字開頭**
3. **區分大小寫**：`name` 和 `Name` 是不同的變數
4. **不能使用Python關鍵字**：如 `if`, `for`, `while` 等

### 好的命名範例
```python
student_name = "小華"      # 使用底線分隔單字
age = 20                  # 簡潔明瞭
total_score = 95.5        # 描述性名稱
is_active = True          # 布林值使用is_開頭
```

### 不好的命名範例
```python
1name = "小明"            # 不能以數字開頭
student-name = "小華"     # 不能使用連字號
if = "條件"               # 不能使用關鍵字
```

---

## 基本資料型別

### 1. 整數 (int)
```python
age = 25
year = 2024
temperature = -5
```

### 2. 浮點數 (float)
```python
height = 175.5
weight = 65.8
pi = 3.14159
```

### 3. 字串 (str)
```python
name = "小明"
message = '你好，世界！'
address = """台北市
信義區
101大樓"""
```

### 4. 布林值 (bool)
```python
is_student = True
is_working = False
```

### 5. 檢查資料型別
```python
x = 42
print(type(x))        # 輸出：<class 'int'>

y = "Hello"
print(type(y))        # 輸出：<class 'str'>
```

---

## 數學運算

### 基本運算符號

| 運算符號 | 說明 | 範例 |
|---------|------|------|
| `+` | 加法 | `5 + 3 = 8` |
| `-` | 減法 | `10 - 4 = 6` |
| `*` | 乘法 | `6 * 7 = 42` |
| `/` | 除法 | `15 / 3 = 5.0` |
| `//` | 整數除法 | `15 // 3 = 5` |
| `%` | 取餘數 | `17 % 5 = 2` |
| `**` | 次方 | `2 ** 3 = 8` |

### 運算範例
```python
# 基本運算
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"加法：{a} + {b} = {a + b}")
print(f"減法：{a} - {b} = {a - b}")
print(f"乘法：{a} * {b} = {a * b}")
print(f"除法：{a} / {b} = {a / b}")
print(f"整數除法：{a} // {b} = {a // b}")
print(f"餘數：{a} % {b} = {a % b}")
print(f"次方：{a} ** {b} = {a ** b}")
```

### 運算優先順序
Python遵循數學運算的優先順序：
1. 括號 `()`
2. 次方 `**`
3. 乘法 `*`、除法 `/`、整數除法 `//`、餘數 `%`
4. 加法 `+`、減法 `-`

**範例：**
```python
result = 2 + 3 * 4 ** 2
print(result)  # 輸出：50 (3 * 16 + 2)

# 使用括號改變優先順序
result2 = (2 + 3) * 4 ** 2
print(result2)  # 輸出：80 ((5) * 16)
```

### 複合指派運算符
```python
x = 10

x += 5      # 等同於 x = x + 5
print(x)    # 輸出：15

x -= 3      # 等同於 x = x - 3
print(x)    # 輸出：12

x *= 2      # 等同於 x = x * 2
print(x)    # 輸出：24

x /= 4      # 等同於 x = x / 4
print(x)    # 輸出：6.0
```

---

## 練習題

### 練習1：基本變數操作
```python
# 請完成以下程式碼
# 1. 建立變數儲存你的姓名、年齡、身高
# 2. 印出這些資訊
# 3. 檢查每個變數的資料型別

# 你的程式碼在這裡：

```

### 練習2：數學運算
```python
# 請完成以下計算
# 1. 計算圓的面積 (半徑 = 5)
# 2. 計算梯形的面積 (上底 = 3, 下底 = 7, 高 = 4)
# 3. 計算 2 的 10 次方

# 你的程式碼在這裡：

```

### 練習3：溫度轉換
```python
# 請將攝氏溫度 25 度轉換為華氏溫度
# 公式：華氏 = 攝氏 * 9/5 + 32

# 你的程式碼在這裡：

```

---

## 解答

### 練習1解答
```python
name = "小明"
age = 20
height = 175.5

print(f"姓名：{name}")
print(f"年齡：{age}")
print(f"身高：{height}")

print(f"name的型別：{type(name)}")
print(f"age的型別：{type(age)}")
print(f"height的型別：{type(height)}")
```

### 練習2解答
```python
import math

# 圓的面積
radius = 5
circle_area = math.pi * radius ** 2
print(f"圓的面積：{circle_area:.2f}")

# 梯形的面積
top = 3
bottom = 7
height = 4
trapezoid_area = (top + bottom) * height / 2
print(f"梯形的面積：{trapezoid_area}")

# 2的10次方
power_result = 2 ** 10
print(f"2的10次方：{power_result}")
```

### 練習3解答
```python
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"攝氏{celsius}度 = 華氏{fahrenheit}度")
```

---

## 總結

在這堂課中，我們學習了：
- ✅ 變數的概念和命名規則
- ✅ Python的基本資料型別
- ✅ 數學運算符號和優先順序
- ✅ 複合指派運算符
- ✅ 實際的程式練習

**下一堂課預告：**
我們將學習字串操作、列表(list)和字典(dict)的使用方法！

---

*有任何問題都可以詢問老師喔！*
