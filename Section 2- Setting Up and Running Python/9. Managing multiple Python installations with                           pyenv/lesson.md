---

# ⚙️ Installing and Verifying `pyenv` for Python Version Management

In previous lessons, we introduced **`pyenv`** as the recommended tool for managing multiple Python versions. Here, we’ll walk through the installation steps and how to verify that `pyenv` is working correctly on your system.

---

## 📥 Installing `pyenv`

The official `pyenv` repository provides instructions for various platforms. You can find it on GitHub (link available in the lecture resources).

### 🔹 macOS and Linux Installation

For **macOS** and **Linux**, you have multiple options:

* Use **Homebrew** (macOS):

  ```bash
  brew update
  brew install pyenv
  ```

* Or follow **manual installation** instructions from the GitHub page, which include:

  * Cloning the repository
  * Adding `pyenv` to your shell startup files (e.g., `.bashrc`, `.zshrc`)
  * Running initialization commands

These steps are detailed under the **Installation** section of the GitHub repo.

---

## 🪟 What About Windows?

`pyenv` **does not officially support native Windows**. If you're working on Windows, you have two options:

1. **Use Windows Subsystem for Linux (WSL):**

   * Install a Linux distro in WSL (e.g., Ubuntu)
   * Follow the standard Linux installation steps

2. **Use the `pyenv-win` fork:**

   * Visit the [pyenv-win GitHub repository](https://github.com/pyenv-win/pyenv-win) (linked in lecture resources)
   * Follow its specific Windows installation instructions
   * This tool provides similar functionality for managing Python versions on Windows

---

## ✅ Verifying the Installation

Once installed, you can verify that `pyenv` is working correctly by running the following commands:

### Check `pyenv` Version:

```bash
pyenv --version
```

### Check Python Location:

```bash
pyenv which python
```

This should return a Python path **under the `~/.pyenv` directory**, confirming that it's not using the system Python.

### Confirm Python Version:

```bash
python --version
```

This version should **match** the output from `pyenv which python`, indicating that your shell is now using the Python version managed by `pyenv`.

---

## 🧠 Recap: `pyenv` Version Scopes

Once `pyenv` is working, you can start managing Python versions at different levels:

* **Global version** (applies system-wide):

  ```bash
  pyenv global 3.11.6
  ```

* **Local (per-project) version:**

  ```bash
  pyenv local 3.8.10
  ```

* **Shell-only version (for temporary sessions):**

  ```bash
  pyenv shell 3.10.4
  ```

No additional setup is required beyond installation — as long as the correct paths are configured, you're ready to use `pyenv` across all your DevOps Python projects.

---
