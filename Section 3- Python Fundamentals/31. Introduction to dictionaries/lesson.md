# **Python Dictionaries Explained**

## **Core Concepts of Dictionaries**

* **Dictionaries** in Python are **mutable**, **insertion-ordered collections** of **key-value pairs**.
* **Keys**:

  * Must be **unique** and **immutable** (e.g., strings, numbers, tuples).
  * **Lists** cannot be used as keys.
* **Values**:

  * Can be **any type**, including other dictionaries, lists, etc.
* **Insertion Order**:

  * Maintained since **Python 3.7**—new elements are added to the end.

---

## **Common Use Cases**

* Configuration files
* JSON-like structures
* API responses
* Fast key-based lookups

---

## **Dictionary Operations**

### **Creating a Dictionary**

```python
my_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}
```

### **Length**

```python
len(my_dictionary)  # Returns number of key-value pairs
```

---

## **Accessing Dictionary Content**

### **Keys, Values, and Items**

```python
my_dictionary.keys()    # Returns dict_keys object
my_dictionary.values()  # Returns dict_values object
my_dictionary.items()   # Returns list of (key, value) tuples
```

### **Iterating Through Items**

```python
for key, value in my_dictionary.items():
    print(f"{key}: {value}")
```

---

## **Membership Tests**

### **Checking for Keys**

```python
'b' in my_dictionary       # True
'e' in my_dictionary       # False
```

### **Checking for Values**

```python
1 in my_dictionary.values()  # True
```

> **Note**: Membership checks using `in` work on **keys**, not values.

---

## **Accessing Elements**

### **Using Brackets**

```python
my_dictionary['b']  # Returns value if key exists, else KeyError
```

### **Using `get()`**

```python
my_dictionary.get('b')        # Returns 2
my_dictionary.get('e')        # Returns None
my_dictionary.get('e', -1)    # Returns -1 (default if key missing)
```

### **Difference**

* `[]` raises **KeyError** if key not found.
* `.get()` returns **None** (or default) if key not found.

---

## **Setting and Updating**

### **Add New Key with Default**

```python
my_dictionary.setdefault('d', 4)
```

### **Update with Another Dictionary**

```python
my_dictionary.update({'e': 5})
```

---

## **Removing Items**

### **Using `pop()`**

```python
removed = my_dictionary.pop('a')  # Removes 'a', returns its value
```

### **Using `popitem()`**

```python
last_removed = my_dictionary.popitem()  # Removes the last added item
```

> **Note**: `popitem()` respects **insertion order** since Python 3.7.

---

## **Other Methods**

### **Clear All Entries**

```python
my_dictionary.clear()
```

### **Create from Keys**

```python
keys = ['x', 'y', 'z']
default_dict = dict.fromkeys(keys, 0)
```

---

## **Summary**

* Python dictionaries are powerful tools for storing and manipulating structured data.
* Understand the difference between keys and values and use built-in methods effectively for safe and efficient operations.
* Use `.get()` and `setdefault()` for safer access and insertion.
* For removal, prefer `pop()` when you know the key, and `popitem()` for last-in removals.
