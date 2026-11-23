# Day 1 – Python Coding Practice: Package Management

## Background

Before introducing Django, FastAPI, or any database, we will start with pure Python.

The goal of this exercise is to practice Python fundamentals, data structures, filtering, grouping, sorting, and handling edge cases.

We will use a simple list of dictionaries to simulate a software package repository.

**Restrictions:**
- Use Python standard library only.
- Do not use Django or FastAPI.
- Do not use any database.
- Do not modify the original input data.

## Sample Data

```python
packages = [
    {
        "name": "firefox",
        "version": "120.0",
        "architecture": "amd64",
        "channel": "stable",
    },
    {
        "name": "vlc",
        "version": "3.0.20",
        "architecture": "amd64",
        "channel": "stable",
    },
    {
        "name": "firefox",
        "version": "121.0",
        "architecture": "arm64",
        "channel": "beta",
    },
    {
        "name": "chromium",
        "version": "119.0",
        "architecture": "amd64",
        "channel": "stable",
    },
    {
        "name": "firefox",
        "version": "122.0",
        "architecture": "amd64",
        "channel": "edge",
    },
]
```

---

## Task 1: Implement a Package Query Function

Implement a function that allows users to filter packages using multiple optional conditions.

### Function Signature

```python
def find_packages(packages, name=None, architecture=None, channel=None):
    pass
```

### Requirements

1. Filter packages by `name`.
2. Filter packages by `architecture`.
3. Filter packages by `channel`.
4. Support combining multiple filtering conditions.
5. If all conditions are `None`, return all packages.
6. Do not modify the original `packages` list.

### Examples

```python
find_packages(packages, name="firefox")

find_packages(packages, architecture="amd64")

find_packages(packages, name="firefox", channel="stable")

find_packages(packages, name="firefox", architecture="amd64", channel="edge")
```

Think about how to implement multiple optional conditions without unnecessary code duplication.

---

## Task 2: Count Packages by Architecture

Implement a function that counts how many packages belong to each architecture.

### Function Signature

```python
def count_packages_by_architecture(packages):
    pass
```

### Expected Result

```python
{
    "amd64": 4,
    "arm64": 1
}
```

### Requirements

1. Count packages based on their `architecture` field.
2. Return a dictionary containing architecture names and their counts.
3. Consider how to handle packages with a missing `architecture` field.

---

## Task 3: Find the Latest Version of Each Package

Implement a function that groups packages by name and keeps only the latest version of each package.

### Function Signature

```python
def get_latest_packages(packages):
    pass
```

### Requirements

1. Group packages by their `name`.
2. Compare versions and identify the latest version.
3. Return only one package per package name.
4. Do not modify the original input data.

For this exercise, assume version numbers follow a simple dot-separated numeric format, such as:

- `3.0.20`
- `120.0`
- `121.0`
- `122.0`

You can use `packaging.version` if you choose to install an external dependency, or implement a simple version comparison function yourself.

**Note:** If you want to strictly follow the Python standard library restriction, implement the version comparison yourself.

### Hint

Consider the difference between comparing version strings directly and comparing their numeric components.

For example:

```python
"120.0"
"9.0"
"10.0"
```

String comparison does not always produce the expected version ordering.

---

## Task 4: Handle Edge Cases

Think about how your functions should behave in the following situations.

| Scenario | Question |
|---|---|
| Empty input list | What should the functions return? |
| Missing `architecture` field | Should the package be skipped or counted separately? |
| Non-existent package name | Should the function return an empty list? |
| Invalid version format | Should the function raise an exception or skip the invalid package? |
| Missing `name` field | How should the package be handled? |
| Duplicate package versions | Which package should be returned? |

You do not need to implement complicated error handling, but your decisions should be consistent and documented.

---

## Completion Criteria

The goal is not to write complicated code. Focus on writing clean, maintainable Python.

Your implementation should satisfy the following criteria:

- [ ] Clear function responsibilities.
- [ ] No modification of the original input data.
- [ ] No unnecessary code duplication.
- [ ] Reasonable use of Python data structures.
- [ ] Proper handling of edge cases.
- [ ] Working implementation with your own tests.

## Testing

Write your own test cases to verify the behavior of all four tasks.

You can use Python's built-in `unittest` module.

At a minimum, test:

- Normal filtering.
- Multiple filtering conditions.
- Empty input.
- Missing dictionary fields.
- Non-existent package names.
- Version comparison.
- Original input data remains unchanged.

---

## Code Review

Once you finish all four tasks, share your implementation for review.

The code will be reviewed from the perspective of a Canonical software engineer, focusing on:

1. **Python Idioms** – Is the code written in a Pythonic way?
2. **Data Structures & Algorithms** – Are the chosen data structures and algorithms appropriate?
3. **Correctness** – Are there hidden bugs or edge cases?
4. **Code Quality** – Are type hints, exception handling, and function responsibilities appropriate?
5. **Testing** – Are the unit tests sufficient?
6. **Performance** – Is there a simpler or more efficient implementation?

**Important:** Try to complete the exercises independently before looking for alternative implementations.

The focus is not just on getting the correct output, but also on understanding why a particular implementation is better than another.
