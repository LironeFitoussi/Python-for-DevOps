# Python Tuples: Immutable Sequences

# Creating a tuple
host_port = ("127.0.0.1", 3000)

# Tuple Examples
host_port = ("127.0.0.1", 3000)
rgb_red = (255, 0, 0)

# Accessing and Slicing Tuples
host = host_port[0]           # "127.0.0.1"
last_two = host_port[-2:]     # ("127.0.0.1", 3000)

# Creating a Single-Item Tuple
# Use a trailing comma to define a tuple with one item:
value = ("only value")        # ➜ This is a string, not a tuple
value_tuple = ("only value",) # ✅ This is a tuple

type(value)         # <class 'str'>
type(value_tuple)   # <class 'tuple'>

# Immutability in Practice
# Tuples do not support item assignment:
# host_port[1] = 8080
# ❌ Raises TypeError: 'tuple' object does not support item assignment

# Comment for clarity
# This will raise a TypeError because tuples are immutable

# Hands-On Example
service_endpoint = ("auth-server.dev.local", 80)

print(f"Host: {service_endpoint[0]}")
print(f"Port: {service_endpoint[1]}")

# Attempting to reassign:
# service_endpoint[1] = 443  → ❌ TypeError

