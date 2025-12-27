# 🔧 Modifying Python Lists: Mutation Methods & Behavior

## Common List Mutation Methods

Python provides several **built-in methods** to **mutate lists** in-place:

### `append(item)`

Adds an item to the **end** of the list.

```python
ports.append(5000)
```

### `insert(index, item)`

Inserts an item **before** the specified index.

```python
ports.insert(1, 3000)  # Inserts 3000 before index 1
```

### `remove(item)`

Removes the **first occurrence** of the specified item.

```python
ports.remove(443)
```

* Raises a `ValueError` if the item is **not in the list**.

### `pop(index)`

Removes and **returns** the item at the specified index.

```python
removed = ports.pop(2)
```

* If no index is provided, `.pop()` removes and returns the **last item**.
* Useful when you want to **store or log** the removed value.

---

## Example: Step-by-Step Mutation

```python
ports = [80, 443, 8080]

ports.append(5000)
# → [80, 443, 8080, 5000]

ports.insert(1, 3000)
# → [80, 3000, 443, 8080, 5000]

ports.remove(80)
# → [3000, 443, 8080, 5000]

removed = ports.pop(2)
# removed → 8080
# ports → [3000, 443, 5000]
```

No reassignment is needed—these methods mutate the original list **in-place**.

---

## Behavior in Jupyter Notebooks

* Variables declared in previous cells remain available unless the **kernel is reset**.
* If a list is mutated in a later cell (e.g. `remove()`), that mutation affects all subsequent cells that reference the list.
* To reset a list to its original state, rerun the cell where it is first declared.

---

## ⚠️ Mutation Side Effects in Functions

Mutating a list passed into a function **modifies the original list** outside the function:

```python
def mutate_list(l):
    l.pop()

my_list = ['a', 'b', 'c']
mutate_list(my_list)

print(my_list)  # → ['a', 'b']
```

This can cause **unexpected side effects**, especially in large or shared codebases.

### ✅ Best Practice

If you need to modify a list **inside a function** but want to preserve the original, make a copy:

```python
def safe_mutation(l):
    copy = l.copy()
    copy.pop()
    return copy
```

---

## Summary Notes

* All methods discussed (`append`, `insert`, `remove`, `pop`) **mutate the list** directly.
* Always check whether your operation should mutate the original list or work on a **copy**.
* Mutation inside functions can have **side effects** that are hard to track.