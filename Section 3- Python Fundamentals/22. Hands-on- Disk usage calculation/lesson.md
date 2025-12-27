# 🧪 Exercise Recap: Calculating and Formatting Disk Usage in Python

Now that you've learned about **variables**, **numbers**, **f-strings**, **string methods**, and **formatting**, it's time to bring them together in a **practical DevOps-style exercise**.

---

## 📊 Goal

Calculate the **disk usage percentage** and output a **human-readable summary** that includes:

* The **server name in uppercase**
* The number of **CPU cores**
* The amount of **RAM in GB**
* The **disk usage percentage**, rounded and formatted

---

## 📦 Step-by-Step Walkthrough

### 🔹 Step 1: Define the Inputs

Let’s assume some example values:

```python
server_name = "dev-server-01"
cpu_cores = 8
memory_gb = 32
disk_used_gb = 350
disk_total_gb = 500
```

### 🔹 Step 2: Calculate Disk Usage Percentage

```python
disk_usage_percentage = disk_used_gb / disk_total_gb
print(disk_usage_percentage)  # Output: 0.7
```

By default, this prints the **raw float value** (e.g., `0.7`).

---

## 🖨️ Step 3: Build a Human-Readable Summary

We can use an **f-string** to generate a clean, readable status report:

```python
summary = (
    f"Server '{server_name.upper()}' "
    f"({cpu_cores} CPU cores, {memory_gb}GB RAM): "
    f"Disk usage = {disk_usage_percentage}"
)
print(summary)
```

**Output:**

```
Server 'DEV-SERVER-01' (8 CPU cores, 32GB RAM): Disk usage = 0.7
```

---

## 🎯 Step 4: Add Float Formatting

### 🧾 Format with One Decimal Place

```python
summary_formatted = (
    f"Server '{server_name.upper()}' "
    f"({cpu_cores} CPU cores, {memory_gb}GB RAM): "
    f"Disk usage = {disk_usage_percentage:.1f}"
)
print(summary_formatted)
```

**Output:**

```
Disk usage = 0.7
```

### 📈 Format as a Percentage

```python
summary_percentage = (
    f"Server '{server_name.upper()}' "
    f"({cpu_cores} CPU cores, {memory_gb}GB RAM): "
    f"Disk usage = {disk_usage_percentage:.1%}"
)
print(summary_percentage)
```

**Output:**

```
Disk usage = 70.0%
```

* `:.1%` multiplies by 100 and appends `%`, rounding to **1 decimal place**.
* You can adjust the number of decimals by changing `.1` to `.2`, etc.

---

## ✅ Summary

| Concept                    | Example                              |
| -------------------------- | ------------------------------------ |
| Basic division             | `used / total`                       |
| f-String with variable     | `f"Disk = {value}"`                  |
| f-String with formatting   | `f"{value:.2f}"` or `f"{value:.1%}"` |
| String method (`.upper()`) | `server_name.upper()`                |

> This exercise mirrors real-world scenarios where you format system metrics (CPU, RAM, disk) for logs, dashboards, or alerts.

Next, we’ll explore **Python collections**, starting with **lists**.