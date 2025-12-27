# 📝 Writing and Running Python Scripts with `.py` Files

Welcome back! After experimenting with Python interactively through **REPL** and **IPython**, it's time to explore how to write **actual Python scripts** using `.py` files — the foundation for real-world development and DevOps automation.

---

## 📁 Step 1: Create a Python Script

In your code directory, create a new file:

```bash
touch demo.py
```

Inside `demo.py`, add the following:

```python
1 + 1
```

Now run the script:

```bash
python demo.py
```

### 🔍 What Happens?

Nothing is printed. That’s expected.

Why? Because:

* Python scripts are **not interactive**.
* There's no REPL cycle (Read → Eval → Print → Loop).
* Expressions like `1 + 1` are **evaluated but not displayed** unless explicitly printed.

---

## 🖨️ Step 2: Print Output to the Terminal

Update `demo.py`:

```python
print(1 + 1)
```

Now rerun:

```bash
python demo.py
# Output: 2
```

### ✅ Key Concept:

```python
print(expression)
```

* This **evaluates the expression** and sends the result to **stdout** (the terminal).
* This is how you make your scripts produce visible output.

---

## 🔄 Python Script Execution Flow

* Python executes scripts **top to bottom**
* Each line is run **once** (no loops unless explicitly written)
* There is **no memory** of previous commands as in REPL

---

## 🧠 Summary

* Use `.py` files to write reusable, multi-line Python scripts.
* Python files **do not print anything unless you tell them to**.
* Use `print()` to inspect values and debug your code.
* You can run a Python script using:

```bash
python filename.py
```

Scripts provide the **structure and control** you need for automation, testing, and production-ready code — essential for any serious Python development, especially in DevOps.

Next, we’ll continue expanding on script structure and Python fundamentals.