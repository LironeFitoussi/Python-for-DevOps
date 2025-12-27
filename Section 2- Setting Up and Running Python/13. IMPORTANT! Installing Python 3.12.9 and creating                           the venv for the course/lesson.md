# ⚙️ Setting Up Your Python 3.12.9 Virtual Environment for DevOps Automation

To ensure consistency and avoid environment-related bugs, it's critical to align on the **exact Python version and dependencies** across all learners. The steps below guide you in creating an **isolated virtual environment** using **Python 3.12.9** and `pyenv`, ensuring smooth execution of DevOps automation scripts throughout the course.

---

## 🧭 Step-by-Step Setup

### ✅ Step 1: Verify `pyenv` Installation

Make sure `pyenv` is installed correctly:

```bash
pyenv --version
```

If you see a version number, you're good to go. If you see "command not found", revisit the `pyenv` installation steps from previous lectures.

---

### 🐍 Step 2: Install Python 3.12.9 with `pyenv`

Install the specific version of Python needed for the course:

```bash
pyenv install 3.12.9
```

> ⏱ This may take several minutes as `pyenv` compiles Python from source.

Verify installation:

```bash
pyenv versions
```

You should see `3.12.9` in the list.

---

### 📁 Step 3: Set Local Python Version for Your Project

Navigate to your course’s project folder and set Python 3.12.9 as the local version:

```bash
cd ~/your-devops-course-folder
pyenv local 3.12.9
# or
pyenv global 3.12.9
```

This creates a `.python-version` file, ensuring all shells inside this folder (and subfolders) use Python 3.12.9.

Check that it's active:

```bash
python --version
# Should return: Python 3.12.9
```

---

### 🔒 Step 4: Create a Virtual Environment

Still inside your project folder:

```bash
python -m venv .venv
```

This creates a `.venv/` folder containing an isolated Python interpreter and environment.

---

### ▶️ Step 5: Activate the Virtual Environment

#### macOS / Linux:

```bash
source .venv/bin/activate
```

Check the Python binary:

```bash
which python
# Should point to: ./venv/bin/python
```

#### Windows:

**Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

**PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

> 🛡️ If you get a PowerShell script execution error, run:
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> ```

Check Python location:

```cmd
where python
```

First path should point to `.venv\Scripts\python.exe`.

---

### 📦 Step 6: Install Course Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

This installs tools like:

* `pytest`
* `requests`
* `PyYAML`
* `jupyterlab`

Verify installation:

```bash
pip list
```

You should see all packages listed with the exact versions from the `requirements.txt` file.

---

## ✅ You're Ready!

You now have:

* **Python 3.12.9** installed
* A **project-scoped virtual environment**
* All course **dependencies installed**
* A clean, reproducible setup for **DevOps scripting and automation**

This setup prevents the classic "it works on my machine" issues and keeps your environment **clean, isolated, and version-controlled**.