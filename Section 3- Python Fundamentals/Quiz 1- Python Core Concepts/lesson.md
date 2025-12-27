### ✅ **Question 1: Variable Naming**

**Question:**
A DevOps engineer needs to store a sensitive API key in a variable. According to Python's **conventions and syntax rules**, which of the following is a valid and appropriately named variable?

**Options:**

* `ApiKey`
* `api-key`
* `2_factor_auth`
* `api key`
* ✅ **`api_key`** (Correct)

**Explanation:**
This is a syntactically valid name that follows the **snake_case** convention in Python. It's readable, does not start with a digit, contains no spaces or special characters, and is conventionally correct.

---

### ✅ **Question 2: Floor Division**

**Question:**
A script is calculating how many full batches of servers can be patched from a given total. What is the output of the following code?

```python
total_servers = 25
batch_size = 8
num_batches = total_servers // batch_size
print(f"Full batches: {num_batches}")
```

**Options:**

* Full batches: 3.125
* ✅ **Full batches: 3** (Correct)
* Full batches: 1
* A `TypeError` is raised
* Full batches: 4

**Explanation:**
The `//` operator performs **floor division**, meaning it divides and then **rounds down** to the nearest integer. `25 // 8` equals `3`.

---

### ✅ **Question 3: String Manipulation**

**Question:**
You are parsing a log file where entries are formatted as `"LEVEL: Message"`. What will be the value of `message_text` after this code runs?

```python
log_entry = "   INFO: User 'admin' logged in successfully.   \n"
parts = log_entry.strip().split(':')
message_text = parts[1].strip()
```

**Options:**

* An `IndexError` will be raised
* `INFO`
* `INFO: User 'admin' logged in successfully.`
* ✅ **`User 'admin' logged in successfully.`** (Correct)

**Explanation:**

* `.strip()` removes leading/trailing whitespace including `\n`
* `.split(':')` splits the string into `['INFO', " User 'admin' logged in successfully."]`
* `parts[1].strip()` gives the final clean message

---

### ✅ **Question 4: F-String Percentage Formatting**

**Question:**
A script needs to report a service's success rate. Which f-string correctly formats the rate variable to display as a **percentage with one decimal place**?

```python
success_rate = 0.9751
```

**Options:**

* `f"Success rate: {success_rate * 100:.1f}%"`
* ✅ **`f"Success rate: {success_rate:.1%}"`** (Correct)
* `f"Success rate: {success_rate:1%}"`
* `f"Success rate: {success_rate} %"`
* `f"Success rate: {.1%success_rate}"`

**Explanation:**
Using `:.1%` multiplies the float by 100, formats it to one decimal place, and appends `%`. This results in `97.5%`.

---

### ✅ **Question 5: String Immutability**

**Question:**
What is the result of running the following Python code?

```python
hostname = "server-a"
hostname[7] = "b"
print(hostname)
```

**Options:**

* The code prints `server-a`
* The code prints `server-b`
* A `NameError` is raised
* ✅ **A `TypeError` is raised** (Correct)
* An `IndexError` is raised

**Explanation:**
Strings in Python are **immutable**, meaning their contents **cannot be changed in place**. Attempting to assign a character to an index in a string raises a `TypeError`.