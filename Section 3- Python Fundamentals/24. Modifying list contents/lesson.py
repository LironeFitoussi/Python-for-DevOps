# Modifying Python Lists: Mutation Methods & Behavior

# Common List Mutation Methods

# append(item) - Adds an item to the end of the list
ports = [80, 443, 8080]
ports.append(5000)

# insert(index, item) - Inserts an item before the specified index
ports.insert(1, 3000)  # Inserts 3000 before index 1

# remove(item) - Removes the first occurrence of the specified item
ports.remove(443)
# Raises a ValueError if the item is not in the list.

# pop(index) - Removes and returns the item at the specified index
removed = ports.pop(2)
# If no index is provided, .pop() removes and returns the last item.

# Example: Step-by-Step Mutation
ports = [80, 443, 8080]

ports.append(5000)
# → [80, 443, 8080, 5000]

ports.insert(1, 3000)
# → [80, 3000, 443, 8080, 5000]

ports.remove(80)
# → [3000, 443, 8080, 5000]

removed = ports.pop(2)
# removed → 8080
# ports → [3000, 443, 5000]

# Mutation Side Effects in Functions
# Mutating a list passed into a function modifies the original list outside the function:
def mutate_list(l):
    l.pop()

my_list = ['a', 'b', 'c']
mutate_list(my_list)

print(my_list)  # → ['a', 'b']

# Best Practice
# If you need to modify a list inside a function but want to preserve the original, make a copy:
def safe_mutation(l):
    copy = l.copy()
    copy.pop()
    return copy

