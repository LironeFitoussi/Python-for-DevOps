# Python Sets: Unordered Collections of Unique Items

# Creating a set
ports = {80, 443, 8080}

# You can also create a set from a list or other iterable using the set() constructor:
unique_ports = set([8443, 22, 81, 8080, 443])
# All duplicates are automatically removed.

# Creating Sets
# From a list
ports = set([8443, 22, 81, 8080, 443, 8443])
# → {81, 8080, 22, 443, 8443}

# With curly braces
server_names = {"web01", "web02", "web03"}

# Membership Testing
22 in unique_ports         # → True
22 in server_names         # → False

# Adding Items
unique_ports.add(3000)
# Adds item to the set if not present
# Does nothing if item already exists

# Removing Items
# remove(item) - Removes item; raises KeyError if not found.
unique_ports.remove(22)  # Works if 22 exists

# discard(item) - Removes item; no error if item is missing.
unique_ports.discard(22)  # Safe removal

# Set Behavior: Order Not Guaranteed
print(unique_ports)
# → Order of elements may change between runs

