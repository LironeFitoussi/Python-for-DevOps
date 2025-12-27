# Python Lists: Fundamentals and Usage

# Creating a list
servers = ["web01", "web02", "web03"]

# Accessing Items by Index
servers[0]     # "web01" - first item
servers[-1]    # "web03" - last item
servers[-2]    # "web02" - second-to-last item

# Using an invalid index (e.g., servers[3]) raises an IndexError.
# To avoid this, use:
index = 3
requested_index = index % len(servers)

# Slicing Lists
servers[:2]     # ['web01', 'web02']
servers[1:]     # ['web02', 'web03']
servers[-2:]    # ['web02', 'web03']
servers[::2]    # ['web01', 'web03']

# Lists with Mixed Types
mixed = ["config.yaml", 80, True]

# You can inspect types:
for item in mixed:
    print(type(item))

