# 🔤 Python Fundamentals: Strings and Their Operations

In this lesson, we explore **strings** in Python — one of the most essential data types. Strings are used constantly in scripting, configuration parsing, file paths, logging, and CLI tools, making them critical in DevOps automation.

---

## 📌 What Are Strings?

* **Strings** are **ordered, immutable sequences of characters**.
* They behave like lists (support indexing/slicing), but **cannot be modified in place**.
* Can be defined using:

  * **Single quotes**: `'Hello'`
  * **Double quotes**: `"Hello"`
  * **Triple quotes**: `'''Hello'''` or `"""Hello"""` for multi-line strings

✅ Use **consistent quoting** in your codebase; code formatters like `black` will enforce a standard.

---

## 🧱 String Creation Examples

```python
single_quote_str = 'Python'
double_quote_str = "DevOps"
multi_line_str = """Line 1
Line 2"""
```

---

## 🧑‍💻 String Interpolation with f-Strings

**f-Strings** make it easy to embed expressions inside strings:

```python
name = "Alice"
print(f"Hello, {name}!")
```

You can also evaluate expressions directly:

```python
print(f"7 / 2 = {7 / 2}")  # 7 / 2 = 3.5
```

---

## 🧹 Whitespace Handling: `.strip()`, `.lstrip()`, `.rstrip()`

Trim unwanted spaces from strings:

```python
s = "   Python for DevOps   "
print(s.strip())   # Removes both sides
print(s.lstrip())  # Removes leading spaces
print(s.rstrip())  # Removes trailing spaces
```

---

## 🔠 Case Conversion

```python
s = "DevOps"
print(s.upper())  # DEVOPS
print(s.lower())  # devops
```

---

## 🔍 String Inspection: `.startswith()`, `.endswith()`

```python
filename = "config.yaml"
print(filename.startswith("config"))  # True
print(filename.endswith(".yaml"))     # True
```

---

## ✂️ Splitting and Joining

### 🔸 Splitting a String:

```python
path = "/usr/local/bin"
parts = path.split("/")  # ['', 'usr', 'local', 'bin']
```

### 🔸 Joining a List into a String:

```python
new_path = "\\".join(parts)  # '\\usr\\local\\bin'
```

> ⚠️ Remember: to print or use backslashes (`\`), you must **escape** them (`\\`), or use **raw strings**: `r"path\to\file"`

---

## ➕ String Concatenation

```python
path = "/usr/local"
path += "/bin"
print(path)  # /usr/local/bin
```

---

## 🔎 Indexing and Slicing Strings

Strings are like lists — you can access characters by index:

```python
s = "DevOps"
print(s[0])      # 'D'
print(s[-1])     # 's' (last char)
print(s[1:4])    # 'evO' (slice from index 1 to 3)
print(s[:3])     # 'Dev'
print(s[3:])     # 'Ops'
```

---

## 🔢 Measuring String Length

```python
s = "automation"
print(len(s))  # 10
```

---

## 🛑 Strings Are Immutable

You **cannot change characters** of a string in place:

```python
s = "DevOps"
s[0] = "d"  # ❌ TypeError: 'str' object does not support item assignment
```

Instead, **create a new string**:

```python
s = "d" + s[1:]  # "devOps"
```

All string methods like `.strip()`, `.upper()`, `.lower()`, etc., return **new strings** and **do not mutate the original**.

---

## 🧠 Summary

| Feature              | Method / Syntax                    | Description                        |
| -------------------- | ---------------------------------- | ---------------------------------- |
| Whitespace cleanup   | `strip()`, `lstrip()`, `rstrip()`  | Removes unwanted spaces            |
| Case manipulation    | `upper()`, `lower()`               | Converts string case               |
| Prefix/suffix checks | `startswith()`, `endswith()`       | Checks start/end substrings        |
| Splitting & joining  | `split()`, `'sep'.join(list)`      | Converts between strings and lists |
| Indexing & slicing   | `s[0]`, `s[1:4]`, `s[:3]`, `s[3:]` | Extracts parts of the string       |
| Length               | `len(s)`                           | Counts number of characters        |
| Immutability         | `s = new_str`                      | Strings can't be modified in-place |

> These string operations are especially valuable when **parsing logs, processing paths, handling filenames**, or **formatting output** in DevOps scripts.

Next up, we'll explore **lists**, Python's versatile and mutable data structure.