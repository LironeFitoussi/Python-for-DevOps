# 🧪 Working with Multiple Virtual Environments and Dependency Management

Now that you're comfortable creating a virtual environment, let's explore how to **manage multiple environments**, install libraries in them, and ensure reproducibility using `requirements.txt`.

---

## 📁 Creating and Activating Multiple Virtual Environments

Let’s assume we are working inside a folder named `virtual_envs`.

### 🔹 Step 1: Create a New Environment

```bash
python -m venv .venv2
```

This creates a new environment named `.venv2` in the current directory.

### 🔹 Step 2: Activate the New Environment

```bash
source .venv2/bin/activate
```

You'll now see your prompt update (e.g., `(.venv2)`), showing you're inside the new virtual environment.

---

## 📦 Installing and Isolating Dependencies

Inside `.venv2`, install a package like `boto3`:

```bash
pip install boto3
```

After installation, run:

```bash
pip list
```

You'll see all dependencies installed in `.venv2`. Now, deactivate:

```bash
deactivate
```

Activate your first environment:

```bash
source .venv/bin/activate
pip list
```

This environment shows **only its own installed packages** (perhaps just `pip`), proving that dependencies are **completely isolated** per environment.

---

## 🔄 Verifying Version Isolation

Let’s say you upgrade `pip` in `.venv`:

```bash
pip install --upgrade pip
```

Now check versions:

* In `.venv`: `pip==25.1`
* In `.venv2`: `pip==25.0.1`

Each environment has its own version of `pip`—what happens in one **stays in that one**.

---

## 🗑️ Deleting a Virtual Environment

To delete a virtual environment:

```bash
rm -rf .venv2
```

There is **no special command** to uninstall a virtual environment—**just delete its folder**.

---

## 🚫 Best Practice: Don’t Commit Virtual Environments

It's considered **bad practice to commit `.venv/`** into version control. Instead, include it in your `.gitignore`:

```
.venv/
```

Why? Because virtual environments are **machine-specific**. Instead, we use a **`requirements.txt`** file to describe the environment.

---

## 📋 Exporting Dependencies with `pip freeze`

1. Activate your environment:

   ```bash
   source .venv/bin/activate
   ```

2. Export installed packages:

   ```bash
   pip freeze > requirements.txt
   ```

This generates a list like:

```
boto3==1.34.28
botocore==1.34.28
...
```

This file is your **source of truth** for the project’s dependencies.

---

## ♻️ Re-creating Environments from `requirements.txt`

Let’s say you deleted `.venv` and want to recreate it.

1. Create the environment again:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. Verify:

   ```bash
   pip list
   ```

Everything is restored exactly as before—**no need to commit the environment** folder.

---

## 🧠 Summary

* You can create multiple virtual environments for different projects or experiments.
* Each environment holds its **own interpreter and dependencies**.
* Use `pip freeze > requirements.txt` and `pip install -r requirements.txt` to **ensure reproducibility**.
* **Never commit `.venv/`**, always use `requirements.txt`.

Virtual environments make it easy to manage isolated and reproducible setups for each Python project in your DevOps workflows.