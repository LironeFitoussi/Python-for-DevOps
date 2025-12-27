# Quiz 1: Python Core Concepts

# Question 1: Variable Naming
# A DevOps engineer needs to store a sensitive API key in a variable.
# According to Python's conventions and syntax rules, which of the following is a valid and appropriately named variable?
# Correct answer: api_key

# Question 2: Floor Division
# A script is calculating how many full batches of servers can be patched from a given total.
total_servers = 25
batch_size = 8
num_batches = total_servers // batch_size
print(f"Full batches: {num_batches}")
# Output: Full batches: 3
# The // operator performs floor division, meaning it divides and then rounds down to the nearest integer.

# Question 3: String Manipulation
# You are parsing a log file where entries are formatted as "LEVEL: Message".
log_entry = "   INFO: User 'admin' logged in successfully.   \n"
parts = log_entry.strip().split(':')
message_text = parts[1].strip()
# Value of message_text: "User 'admin' logged in successfully."
# .strip() removes leading/trailing whitespace including \n
# .split(':') splits the string into ['INFO', " User 'admin' logged in successfully."]
# parts[1].strip() gives the final clean message

# Question 4: F-String Percentage Formatting
# A script needs to report a service's success rate.
success_rate = 0.9751
# Correct f-string: f"Success rate: {success_rate:.1%}"
# Using :.1% multiplies the float by 100, formats it to one decimal place, and appends %.
# This results in 97.5%

# Question 5: String Immutability
hostname = "server-a"
# hostname[7] = "b"  # ❌ This would raise a TypeError
# print(hostname)
# Strings in Python are immutable, meaning their contents cannot be changed in place.
# Attempting to assign a character to an index in a string raises a TypeError.

