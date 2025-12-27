# Python Fundamentals: Strings and Their Operations

# String Creation Examples
single_quote_str = 'Python'
double_quote_str = "DevOps"
multi_line_str = """Line 1
Line 2"""

# String Interpolation with f-Strings
name = "Alice"
print(f"Hello, {name}!")

# You can also evaluate expressions directly:
print(f"7 / 2 = {7 / 2}")  # 7 / 2 = 3.5

# Whitespace Handling: .strip(), .lstrip(), .rstrip()
s = "   Python for DevOps   "
print(s.strip())   # Removes both sides
print(s.lstrip())  # Removes leading spaces
print(s.rstrip())  # Removes trailing spaces

# Case Conversion
s = "DevOps"
print(s.upper())  # DEVOPS
print(s.lower())  # devops

# String Inspection: .startswith(), .endswith()
filename = "config.yaml"
print(filename.startswith("config"))  # True
print(filename.endswith(".yaml"))     # True

# Splitting and Joining
# Splitting a String:
path = "/usr/local/bin"
parts = path.split("/")  # ['', 'usr', 'local', 'bin']

# Joining a List into a String:
new_path = "\\".join(parts)  # '\\usr\\local\\bin'

# String Concatenation
path = "/usr/local"
path += "/bin"
print(path)  # /usr/local/bin

# Indexing and Slicing Strings
s = "DevOps"
print(s[0])      # 'D'
print(s[-1])     # 's' (last char)
print(s[1:4])    # 'evO' (slice from index 1 to 3)
print(s[:3])     # 'Dev'
print(s[3:])     # 'Ops'

# Measuring String Length
s = "automation"
print(len(s))  # 10

# Strings Are Immutable
# You cannot change characters of a string in place:
s = "DevOps"
# s[0] = "d"  # ❌ TypeError: 'str' object does not support item assignment

# Instead, create a new string:
s = "d" + s[1:]  # "devOps"

