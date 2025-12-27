# Summary: Differences Between Lists, Tuples, and Sets in Python

# Lists
# Syntax: Square brackets []
# Ordered: Yes — maintains insertion order
# Mutable: Yes — can add, remove, or update elements
# Duplicates: Allowed
# Use Cases: Editable, position-aware sequences
# Examples: Deployment steps, File reads/log lines, Task queues

# Tuples
# Syntax: Parentheses ()
# Ordered: Yes — maintains insertion order
# Mutable: No — immutable after creation
# Duplicates: Allowed
# Use Cases: Fixed and positional data, Multiple ordered values forming a logical group
# Examples: Host-port pairs, RGB color values, Multi-value function returns (stdout, stderr, etc.)

# Sets
# Syntax: Curly braces {} or set() constructor
# Ordered: No — unordered, no guaranteed order
# Mutable: Yes — can add/remove items
# Duplicates: Not allowed — duplicates are automatically removed
# Element Requirement: Must contain only immutable items
# Use Cases: Fast membership testing, Deduplication of data
# Examples: Whitelist of allowed ports, Unique user IDs, Unique IP extraction from access logs

