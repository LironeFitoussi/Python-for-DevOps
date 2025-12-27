---

# 💬 Writing Comments in Python: Best Practices & Techniques

Although Python is known for its **readable syntax**, **comments** play an essential role in clarifying intent, explaining complex logic, and highlighting tasks or limitations in your code. In this lesson, we’ll explore the **two main ways to write comments** in Python and how to use them effectively.

---

## 📝 1. Single-Line Comments

Single-line comments are written using the `#` symbol.

```python
# This is a single-line comment
error_count = 0  # Initialize error counter
```

### ✅ Use Cases:

* Brief explanations for non-obvious logic
* Inline notes after a line of code
* Highlighting **TODOs** for incomplete logic:

```python
# TODO: Handle case when argument is None
```

> 💡 **IDE Tip:** Many editors like VS Code and PyCharm automatically highlight or index lines starting with `# TODO:` for easy tracking.

---

## ⚠️ Don’t Overuse Obvious Comments

Avoid writing comments that simply restate what the code already makes clear:

```python
error_count = 0  # Initializing error counter ❌ (too obvious)
```

Instead, **focus comments on *why* or *how***, not *what*:

```python
# Reset count to zero before processing next batch
error_count = 0
```

### ✅ Principle: Write *self-documenting code*

* Choose **descriptive variable and function names**
* Use comments only to explain complex logic, intent, or design decisions

---

## 🧱 2. Multi-Line (Block) Comments

You have two main options for writing comments over multiple lines:

### Option 1: Multiple `#` Symbols

```python
# This block checks the preconditions
# and logs a message if they are met
if ready:
    print("Executing...")
```

### Option 2: Triple Quotes (used sparingly)

```python
'''
This is a block comment
written using triple single quotes
'''
```

Or:

```python
"""
This is another multi-line comment
using triple double quotes
"""
```

> ⚠️ **Important:** Triple quotes are **technically treated as string literals**, not true comments. Python will ignore them only if they are **not assigned to any variable** or used as docstrings.

They are better reserved for **function/class/module documentation**, known as **docstrings** — which we’ll cover later when we explore functions.

---

## 🧠 Summary: Python Commenting Guidelines

| Type             | Syntax                        | Purpose                                               |
| ---------------- | ----------------------------- | ----------------------------------------------------- |
| Single-line      | `# comment`                   | Quick note or explanation                             |
| Inline comment   | `code  # explanation`         | Brief context after a line                            |
| Multi-line block | Multiple `#` or triple quotes | Longer context or temporary code disable              |
| TODO notes       | `# TODO: ...`                 | Reminders for unfinished logic                        |
| Avoid            | Obvious or redundant comments | Write clear code instead of explaining trivial things |

> 🔑 **Golden Rule**: Code should explain *what* is happening. Comments should explain *why*.

---

With that, you're ready to write clean, readable, and well-documented Python code! Up next, we’ll dive into **primitive data types** and **string manipulation**.

---
