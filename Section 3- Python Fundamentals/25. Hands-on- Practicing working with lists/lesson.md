# 🧪 List Exercise: Practicing Indexing, Appending, and Assignment

## Objective

Use a list called `deployment_targets` to:

* Access elements by index
* Append new elements
* Modify an existing element

---

## Step-by-Step Code Breakdown

### 1. Create the Initial List

```python
deployment_targets = ["us-east-1", "eu-west-1", "ap-southeast-1"]
```

### 2. Print the First Deployment Target

```python
print(deployment_targets[0])
# Output: "us-east-1"
```

### 3. Append a New Region

```python
deployment_targets.append("us-west-2")
```

### 4. Print the Updated List

```python
print(deployment_targets)
# Output: ['us-east-1', 'eu-west-1', 'ap-southeast-1', 'us-west-2']
```

### 5. Modify the Second Region

```python
deployment_targets[1] = "eu-central-1"
```

### 6. Final Print

```python
print(deployment_targets)
# Output: ['us-east-1', 'eu-central-1', 'ap-southeast-1', 'us-west-2']
```

---

## Concepts Practiced

* **List indexing** to access or update elements
* **`.append()`** to add a new element to the end
* **Direct assignment** using `list[index] = value` to modify an element in-place

---

## Notes

* Use **consistent string quoting** (either single or double) for cleaner code.
* Indexing starts at **0**.
* Lists grow dynamically—no need to declare the size in advance.