# 🧩 Python Sets: Unordered Collections of Unique Items

## What is a Set?

A **set** is an **unordered**, **mutable** collection that only holds **unique items**.

```python
ports = {80, 443, 8080}
```

You can also create a set from a list or other iterable using the `set()` constructor:

```python
unique_ports = set([8443, 22, 81, 8080, 443])
```

All duplicates are **automatically removed**.

---

## Key Characteristics

* **Unordered**: No guaranteed order of elements
* **Mutable**: Can add or remove items
* **Unique values only**: Duplicate entries are discarded
* **Cannot contain mutable elements** (e.g., lists or sets)
* **Can contain immutable items**, such as tuples

---

## Set Use Cases

* Removing duplicates
* Membership testing (`in`)
* Performing **set operations** like:

  * **Union**
  * **Intersection**
  * **Difference**

---

## Creating Sets

### From a list

```python
ports = set([8443, 22, 81, 8080, 443, 8443])
# → {81, 8080, 22, 443, 8443}
```

### With curly braces

```python
server_names = {"web01", "web02", "web03"}
```

---

## Membership Testing

```python
22 in unique_ports         # → True
22 in server_names         # → False
```

---

## Adding Items

```python
unique_ports.add(3000)
```

* Adds item to the set if not present
* Does nothing if item already exists

---

## Removing Items

### `remove(item)`

Removes item; raises `KeyError` if not found.

```python
unique_ports.remove(22)  # Works if 22 exists
```

### `discard(item)`

Removes item; **no error** if item is missing.

```python
unique_ports.discard(22)  # Safe removal
```

---

## Set Behavior: Order Not Guaranteed

```python
print(unique_ports)
# → Order of elements may change between runs
```

Sets do **not preserve insertion order**. Don’t rely on order when working with sets.

---

## Summary Notes

* Use sets when you need **uniqueness**, not order.
* Set elements must be **immutable** (e.g., numbers, strings, tuples).
* Prefer `discard()` over `remove()` when item presence is uncertain.
* Leverage `set()` to **deduplicate** other collections quickly.
