# 🧪 Set Exercise: Working with Required and Installed Packages

## 🎯 Goal

Practice creating sets, checking membership, performing mutation, and using set operations (`-`, `&`).

---

## 1. Create the `required_packages` Set

```python
required_packages = set([
    "python3", "pip", "requests", "boto3", "pip"
])
```

> ✅ Duplicate `"pip"` will be removed automatically.

### Print to Confirm Uniqueness

```python
print(required_packages)
# Output: {'boto3', 'python3', 'requests', 'pip'}
```

---

## 2. Membership Checks

```python
"requests" in required_packages  # → True
"ansible" in required_packages   # → False
```

### Output with f-strings:

```python
print(f"Is 'requests' required? { 'requests' in required_packages }")
print(f"Is 'ansible' required? { 'ansible' in required_packages }")
```

---

## 3. Add & Safely Remove Items

```python
required_packages.add("paramiko")     # ✅ Adds new package
required_packages.discard("pip")      # ✅ Safely removes pip
```

### Print Resulting Set

```python
print(required_packages)
# → {'boto3', 'python3', 'requests', 'paramiko'}
```

---

## 4. Define `installed_packages` Set

```python
installed_packages = set([
    "docker", "python3", "pip"
])
```

---

## 5. Set Operations

### 🔻 Missing Packages

Packages **required** but not installed:

```python
missing_packages = required_packages - installed_packages
# → {'boto3', 'paramiko', 'requests'}
```

### 🔺 Extra Packages

Packages **installed** but not required:

```python
extra_packages = installed_packages - required_packages
# → {'pip', 'docker'}
```

### 🔁 Common Packages

Packages both required and installed:

```python
common_packages = required_packages & installed_packages
# → {'python3'}
```

---

## 6. Display the Results

```python
print(f"Missing packages: {missing_packages}")
print(f"Extra packages: {extra_packages}")
print(f"Common packages: {common_packages}")
```

---

## ✅ Summary Output

```text
Missing packages: {'boto3', 'paramiko', 'requests'}
Extra packages: {'pip', 'docker'}
Common packages: {'python3'}
```

---

## 🧠 Concepts Practiced

* Creating and printing sets
* Automatic deduplication
* Membership checks with `in`
* Adding/removing with `.add()` and `.discard()`
* Set difference `-` and intersection `&`
* Clear naming improves readability (`required_packages`, `installed_packages`)