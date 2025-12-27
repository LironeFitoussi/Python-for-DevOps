# 🧪 Practicing with Virtual Environments in Python

Now that we understand the **importance and purpose of virtual environments**, let's walk through how to **create**, **activate**, and **switch** between them in a hands-on way.

For this demo, we’ll use a folder named `virtual_envs` to host different virtual environments.

---

## 📁 Step 1: Create a New Virtual Environment

In your terminal, navigate to the `virtual_envs` folder (or any directory of your choice):

```bash
cd virtual_envs
```

Then create a virtual environment using the built-in `venv` module:

```bash
python -m venv .venv
```

* `.venv` is the **name of the folder** that will hold the virtual environment.
* You can also use a different name, or provide an **absolute or relative path**.
* This creates a `.venv/` directory containing:

  * A copy of the **Python interpreter**
  * The **`bin/` (or `Scripts/` on Windows) folder** with activation scripts
  * An isolated **`site-packages/` directory**

---

## 🚀 Step 2: Activate the Virtual Environment

### 🔹 On Linux/macOS:

```bash
source .venv/bin/activate
```

* This command **activates** the virtual environment.
* You'll see your prompt change (e.g., `(.venv)`), indicating activation.
* Now, any `python` or `pip` commands will use the versions inside `.venv`.

### 🔹 On Windows (CMD or PowerShell):

Depending on the shell you're using:

#### CMD:

```cmd
.venv\Scripts\activate.bat
```

#### PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

> 💡 **Tip:** If you face script execution issues in PowerShell, you may need to adjust your execution policy:
>
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

---

## 🔍 Step 3: Confirm the Environment Is Active

Use `which` (or `where` on Windows) to verify the current Python path:

```bash
which python
```

Expected output should point to:

```
/path/to/virtual_envs/.venv/bin/python
```

Instead of:

```
~/.pyenv/versions/3.x.x/bin/python
```

This confirms that your shell is now using the **virtual environment's Python interpreter**.

---

## 🔁 Step 4: Deactivate and Switch Back

To exit the virtual environment and return to the global Python installation:

```bash
deactivate
```

* Your shell prompt will return to normal (the `(.venv)` prefix disappears).
* Running `which python` again should show the **global or `pyenv`-managed Python**.

---

## 🧠 Recap

| Action               | Command (Linux/macOS)       | Command (Windows)                      |
| -------------------- | --------------------------- | -------------------------------------- |
| Create venv          | `python -m venv .venv`      | `python -m venv .venv`                 |
| Activate venv        | `source .venv/bin/activate` | `.venv\Scripts\activate.bat` or `.ps1` |
| Check Python version | `which python`              | `where python`                         |
| Deactivate venv      | `deactivate`                | `deactivate`                           |

Using virtual environments is essential for maintaining **clean, conflict-free project setups**, especially when working with **multiple Python projects** in DevOps workflows.