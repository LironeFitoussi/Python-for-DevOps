# Python Dictionaries Explained

# Creating a Dictionary
my_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

# Length
len(my_dictionary)  # Returns number of key-value pairs

# Accessing Dictionary Content
# Keys, Values, and Items
my_dictionary.keys()    # Returns dict_keys object
my_dictionary.values()  # Returns dict_values object
my_dictionary.items()   # Returns list of (key, value) tuples

# Iterating Through Items
for key, value in my_dictionary.items():
    print(f"{key}: {value}")

# Membership Tests
# Checking for Keys
'b' in my_dictionary       # True
'e' in my_dictionary       # False

# Checking for Values
1 in my_dictionary.values()  # True

# Note: Membership checks using in work on keys, not values.

# Accessing Elements
# Using Brackets
my_dictionary['b']  # Returns value if key exists, else KeyError

# Using get()
my_dictionary.get('b')        # Returns 2
my_dictionary.get('e')        # Returns None
my_dictionary.get('e', -1)    # Returns -1 (default if key missing)

# Difference:
# [] raises KeyError if key not found.
# .get() returns None (or default) if key not found.

# Setting and Updating
# Add New Key with Default
my_dictionary.setdefault('d', 4)

# Update with Another Dictionary
my_dictionary.update({'e': 5})

# Removing Items
# Using pop()
removed = my_dictionary.pop('a')  # Removes 'a', returns its value

# Using popitem()
last_removed = my_dictionary.popitem()  # Removes the last added item

# Note: popitem() respects insertion order since Python 3.7.

# Other Methods
# Clear All Entries
my_dictionary.clear()

# Create from Keys
keys = ['x', 'y', 'z']
default_dict = dict.fromkeys(keys, 0)

