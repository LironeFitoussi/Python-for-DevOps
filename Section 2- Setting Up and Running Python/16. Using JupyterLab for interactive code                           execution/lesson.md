# 📓 Using Jupyter Notebooks and JupyterLab for Python DevOps Projects

In addition to `.py` scripts and REPLs, another powerful and widely used way to write and run Python code is through **Jupyter Notebooks**, especially when working with **interactive DevOps demos, data exploration**, or **step-by-step documentation with live code**.

Let’s go through how to install, launch, and use **JupyterLab**, a modern interface for working with notebooks.

---

## 🧪 Step 1: Install JupyterLab and Dependencies

Make sure you're in the **active virtual environment** for your DevOps course.

Then install the necessary dependencies:

```bash
pip install jupyterlab ipython rich
```

* **`jupyterlab`**: Web-based environment for notebooks and documents
* **`ipython`**: Advanced REPL engine used by notebooks
* **`rich`**: For formatting output nicely in the terminal

These tools may install **dozens of dependencies**, so expect a large list when running `pip freeze`.

---

## 💾 Optional: Save Dependencies

After installation, save your environment's current package list:

```bash
pip freeze > requirements.txt
```

This ensures **reproducibility** across systems or team members.

---

## 🚀 Step 2: Launch JupyterLab

Start the server with:

```bash
jupyter lab
```

* This starts a **local web server** at: `http://localhost:8888`
* It opens a rich UI where you can create Python notebooks and more

---

## ✍️ Step 3: Create and Use a Notebook

### Create a New Notebook

1. Click **"Python 3 (ipykernel)"** under the **Notebook** section.
2. A new file opens: `Untitled.ipynb`.

### Add Python Code

Example cell:

```python
myvar = "hello"
print(myvar)
myvar
```

* Press **Shift + Enter** to execute the cell.
* The **last line** will be automatically displayed as output.
* Only **explicit `print()`** calls output to the terminal; others are shown as results in the notebook UI.

### Output Behavior:

| Code                  | Result                                     |
| --------------------- | ------------------------------------------ |
| `print(myvar)`        | Prints `"hello"`                           |
| `myvar`               | Displays `"hello"` (from eval, not print)  |
| `print(myvar); myvar` | Shows both print output and variable value |

---

## 📝 Markdown Support

Change a cell’s type to **Markdown** (from the dropdown or toolbar). Example:

```markdown
### My Variable

This section explains what `myvar` does.
```

Run with **Shift + Enter** — it renders nicely as documentation.

---

## 🧩 IDE Integration

You can also open `.ipynb` files inside VS Code or another IDE with Jupyter support.

* **Select kernel** when prompted, and choose:

  ```
  .venv/bin/python
  ```

* Use the **same shortcuts** (Shift + Enter, etc.) to execute cells.

> 🔁 Both the **browser UI** and **IDE UI** offer similar functionality if your IDE has full Jupyter integration.

---

## 🧹 Cleanup & Shutdown

1. **Delete test files** (e.g., `demo.py`, `Untitled.ipynb`) from within JupyterLab or your file explorer.
2. Stop the server with:

```bash
Ctrl + C
```

Then confirm shutdown by typing:

```bash
y
```

---

## 🧠 Summary

* **Jupyter Notebooks** combine code + markdown for interactive, documented workflows.
* Use **JupyterLab** for a full-featured web interface.
* Perfect for **exploratory coding**, **DevOps tutorials**, or **reproducible automation scripts**.
* You can run it in-browser or inside supported IDEs.

Throughout the course, we’ll alternate between `.py` files and notebooks depending on the context, so ensure your setup is ready.