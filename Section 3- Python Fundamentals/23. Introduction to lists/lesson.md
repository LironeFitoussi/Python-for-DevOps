# 🔢 Python Lists: Fundamentals and Usage

## What is a List?

A list is an **ordered, mutable collection** used to store multiple items.
It is defined using square brackets `[]`, with elements separated by commas.

```python
servers = ["web01", "web02", "web03"]
```

## Key Characteristics

* **Ordered**: Items maintain insertion order.
* **Mutable**: Items can be added, removed, or changed.
* **Indexable**: Supports both positive and negative indexing.
* **Mixed types allowed**, but discouraged for clarity.

## Accessing Items by Index

```python
servers[0]     # "web01" - first item
servers[-1]    # "web03" - last item
servers[-2]    # "web02" - second-to-last item
```

Using an invalid index (e.g., `servers[3]`) raises an `IndexError`.

To avoid this, use:

```python
index = requested_index % len(servers)
```

## Slicing Lists

Slicing returns a **new list** from a specific range.

```python
servers[:2]     # ['web01', 'web02']
servers[1:]     # ['web02', 'web03']
servers[-2:]    # ['web02', 'web03']
servers[::2]    # ['web01', 'web03']
```

Syntax: `list[start:stop:step]`

* Start is inclusive
* Stop is exclusive
* Step is optional and allows skipping elements

## Lists with Mixed Types

Python allows different data types in a single list:

```python
mixed = ["config.yaml", 80, True]
```

You can inspect types:

```python
for item in mixed:
    print(type(item))
```

This is valid, but best avoided unless needed, as it impacts readability and maintainability.

## Mutation Behavior

Lists are mutable. Operations like slicing produce **new lists**, but other methods like `.append()`, `.remove()` mutate in-place. These will be covered in more detail later.