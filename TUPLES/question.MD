
# 📝 16. Practice Questions

## Level 1: Basics

### Question 1

```python
student = ("Rahul", 20, "Delhi")
print(student[1])
```

**What will print?**

<details>
<summary>Answer</summary>
`20`

Explanation: Index 1 refers to the second element, which is 20.

</details>

---

### Question 2

```python
numbers = (10, 20, 30)
print(numbers[-1])
```

**What will print?**

<details>
<summary>Answer</summary>
`30`

Explanation: -1 refers to the last element.

</details>

---

### Question 3

```python
single = (5)
print(type(single))
```

**What will print?**

<details>
<summary>Answer</summary>
`<class 'int'>`

Explanation: Without a comma, it's just an integer in parentheses, not a tuple!

</details>

---

### Question 4

```python
fruits = ("Apple", "Banana", "Mango")
print(fruits[1:3])
```

**What will print?**

<details>
<summary>Answer</summary>
`('Banana', 'Mango')`

Explanation: Slicing starts at index 1 (included) and stops at index 3 (excluded).

</details>

---

## Level 2: Intermediate

### Question 5

```python
colors = ("Red", "Green", "Blue", "Yellow")
print(colors[::2])
```

**What will print?**

<details>
<summary>Answer</summary>
`('Red', 'Blue')`

Explanation: `[::2]` means start from 0, go to end, skip every 2nd element.

</details>

---

### Question 6

```python
coordinates = (27.17, 78.04)
coordinates[0] = 30
```

**What will happen?**

<details>
<summary>Answer</summary>
`TypeError: 'tuple' object does not support item assignment`

Explanation: Tuples are immutable and cannot be modified.

</details>

---

### Question 7

```python
t1 = (1, 2)
t2 = (3, 4)
result = t1 + t2
print(result)
```

**What will print?**

<details>
<summary>Answer</summary>
`(1, 2, 3, 4)`

Explanation: Tuples can be concatenated (combined) using the + operator.

</details>

---

### Question 8

```python
numbers = (10, 20, 30, 20, 10)
print(numbers.count(20))
```

**What will print?**

<details>
<summary>Answer</summary>
`2`

Explanation: `count()` returns how many times the value 20 appears in the tuple.

</details>

---

### Question 9 (NEW!)

```python
x, y, z = (10, 20, 30)
print(x, z)
```

**What will print?**

<details>
<summary>Answer</summary>
`10 30`

Explanation: Unpacking assigns each element to a variable. x=10, y=20, z=30.

</details>

---

### Question 10 (NEW!)

```python
data = ([1, 2], "name")
data[0][0] = 99
print(data)
```

**What will print?**

<details>
<summary>Answer</summary>
`([99, 2], 'name')`

Explanation: Shallow immutability - the tuple is immutable, but the list inside can be modified.

</details>

---

## Level 3: Practical

### Question 11

You need to store your location's latitude and longitude, which never changes.

**Should you use a List or Tuple? Why?**

<details>
<summary>Answer</summary>
**Tuple** — Because coordinates don't change. They should be fixed and protected from accidental modification.

```python
location = (27.1751, 78.0421)
```

</details>

---

### Question 12

You're building a shopping list app where users add/remove items.

**Should you use a List or Tuple? Why?**

<details>
<summary>Answer</summary>
**List** — Because the shopping list changes frequently as users add or remove items.

```python
shopping_list = ["milk", "bread", "eggs"]
shopping_list.append("butter")  # Can modify
```

</details>

---

### Question 13 (NEW!)

```python
cache = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}
print(cache[(10, 20)])
```

**What will print and why use tuples here?**

<details>
<summary>Answer</summary>
`Point A`

Explanation: Tuples are immutable and hashable, so they can be dictionary keys. Lists cannot be used as keys.

</details>

---

### Question 14 (NEW!)

Create a function that swaps two values and returns them.
<details>
<summary>Answer</summary>
```python
def swap(a, b):
    return b, a  # Tuple packing

x, y = swap(5, 10) # Tuple unpacking
print(x, y) # 10 5


</details>


