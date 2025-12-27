# Valid Set Elements in Python & Set Operations

# Invalid Set Elements
# 1. Lists in Sets – Not Allowed
# Lists are mutable, so they are not hashable and cannot be used as set elements.
# set([[1, 2], [3, 4]])
# → ❌ TypeError: unhashable type: 'list'

# 2. Sets in Sets – Also Invalid
# Sets themselves are mutable, so trying to create a set of sets will also fail:
# set([{1, 2}, {3, 4}])
# → ❌ TypeError: unhashable type: 'set'

# Valid Set Elements
# Tuples in Sets – Allowed
# Tuples are immutable, so they can be added to sets.
set_of_tuples = {(1, 2), (3, 4)}
print(set_of_tuples)
# → {(1, 2), (3, 4)}

# Tuple Membership Testing
(1, 2) in set_of_tuples   # → True
(1, 3) in set_of_tuples   # → False

# Set Operations in Practice
# Let's define two sets:
developers = set(["Alice", "Bob", "Charlie"])
admins = set(["Alice", "David"])

# Membership Test
"Alice" in developers  # → True
"Alice" in admins      # → True

# Set Operations (Method Style)
# Union: Combine Elements
developers.union(admins)
# → {'Alice', 'Bob', 'Charlie', 'David'}

# Intersection: Common Elements
developers.intersection(admins)
# → {'Alice'}

# Difference: Elements in First Set, Not in Second
developers.difference(admins)
# → {'Bob', 'Charlie'}

# Set Operations (Operator Style)
# Union: developers | admins
# Intersection: developers & admins
# Difference: developers - admins

# Mutation vs Copy
# Set methods have mutating versions that update the original set:
# intersection_update()
# difference_update()

# These methods change the original set rather than returning a new one.
developers.intersection_update(admins)
# developers is now {'Alice'}

