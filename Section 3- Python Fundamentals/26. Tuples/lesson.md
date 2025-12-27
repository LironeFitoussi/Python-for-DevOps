# 🔐 Python Tuples: Immutable Sequences

## What is a Tuple?

A **tuple** is an **ordered, immutable** collection of values.
Once created, the contents of a tuple **cannot be changed**—you cannot add, remove, or modify its elements.

```python
host_port = ("127.0.0.1", 3000)
```

Tuples are defined using **parentheses `()`**, and are ideal for representing **fixed structures** such as:

* Coordinates
* RGB color values
* Host-port pairs
* Version numbers

---

## Tuple Characteristics

* **Ordered**: Elements maintain insertion order
* **Immutable**: Cannot modify after creation
* **Indexable and sliceable**
* Use parentheses `()` (though optional in some contexts)

---

## Tuple Examples

```python
host_port = ("127.0.0.1", 3000)
rgb_red = (255, 0, 0)
```

## Accessing and Slicing Tuples

```python
host = host_port[0]           # "127.0.0.1"
last_two = host_port[-2:]     # ("127.0.0.1", 3000)
```

Slicing a tuple returns **a new tuple**, not a list.

---

## Creating a Single-Item Tuple

Use a **trailing comma** to define a tuple with one item:

```python
value = ("only value")        # ➜ This is a string, not a tuple
value_tuple = ("only value",) # ✅ This is a tuple
```

```python
type(value)         # <class 'str'>
type(value_tuple)   # <class 'tuple'>
```

---

## Immutability in Practice

Tuples **do not support item assignment**:

```python
host_port[1] = 8080
# ❌ Raises TypeError: 'tuple' object does not support item assignment
```

```python
# Comment for clarity
# This will raise a TypeError because tuples are immutable
```

---

## Hands-On Example

```python
service_endpoint = ("auth-server.dev.local", 80)

print(f"Host: {service_endpoint[0]}")
print(f"Port: {service_endpoint[1]}")
```

Attempting to reassign:

```python
# service_endpoint[1] = 443  → ❌ TypeError
```

---

## Summary Notes

* Use tuples for **fixed, unchanging data**.
* Always use a **comma for single-element tuples**.
* Tuple slices return a **new tuple**, not a list.
* Reassigning or mutating tuple items results in a **TypeError**.

