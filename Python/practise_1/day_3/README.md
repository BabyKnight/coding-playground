# Day 3 – Generators, Iterators, and Lazy Evaluation

## Snap Package Streaming Processor

**Difficulty:** Intermediate  
**Estimated Time:** 45–60 minutes  
**Python Version:** Python 3.10+  
**Dependencies:** Python standard library and pytest

## Background

Imagine that we are building a package processing service for the Snap Store.

The service receives package metadata from different sources. The input may contain thousands or even millions of packages.

Loading and processing all packages at once can consume a significant amount of memory.

Instead, we want to process packages lazily using Python generators and iterators.

In this exercise, you will implement a small streaming processor that can:

1. Filter packages without creating an additional list.
2. Split an iterable into smaller batches.
3. Combine generators to build a lazy processing pipeline.

The goal is to understand how generators work and when lazy evaluation is useful in real-world applications.

---

## Input Data

Use the following sample package data:

```python
packages = [
    {
        "name": "firefox",
        "version": "120.0",
        "architecture": "amd64",
        "channel": "stable",
    },
    {
        "name": "firefox",
        "version": "121.0",
        "architecture": "amd64",
        "channel": "candidate",
    },
    {
        "name": "chromium",
        "version": "119.0",
        "architecture": "arm64",
        "channel": "stable",
    },
    {
        "name": "vlc",
        "version": "3.0.20",
        "architecture": "amd64",
        "channel": "stable",
    },
    {
        "name": "git",
        "version": "2.43.0",
        "architecture": "arm64",
        "channel": "edge",
    },
]
```

You can use this data for development and testing.

---

## Task 1 – Implement a Package Filter Generator

Implement a function that filters packages by channel and architecture.

### Function Signature

```python
from collections.abc import Iterable, Iterator

def iter_packages(
    packages: Iterable[dict],
    channel: str | None = None,
    architecture: str | None = None,
) -> Iterator[dict]:
    pass
```

### Requirements

1. Filter packages by `channel` when a channel is provided.
2. Filter packages by `architecture` when an architecture is provided.
3. If a filter argument is `None`, ignore that filter.
4. Use `yield` to return matching packages.
5. Do not create a new list containing all matching packages.
6. Support different iterable inputs, including:
   - list
   - tuple
   - generator
7. Preserve the original order of packages.
8. Do not modify the original package data.

### Example

```python
result = iter_packages(
    packages,
    channel="stable",
    architecture="amd64",
)

for package in result:
    print(package["name"])
```

Expected output:

```text
firefox
vlc
```

### Important

The function should return a generator, not a list.

Consider what happens when the input contains one million packages. We should only process packages as they are requested.

---

## Task 2 – Implement a Batch Generator

Implement a generator that splits an iterable into smaller batches.

### Function Signature

```python
from collections.abc import Iterable, Iterator

def iter_batches(
    items: Iterable,
    batch_size: int,
) -> Iterator[list]:
    pass
```

### Requirements

1. Split the input into batches of at most `batch_size` items.
2. The last batch may contain fewer items.
3. Do not convert the entire input into a list.
4. Support generator inputs.
5. Use `yield` to return each batch.
6. An empty input should produce no batches.
7. `batch_size` must be a positive integer.
8. Reject `bool` values, even though `bool` is a subclass of `int` in Python.
9. Raise `ValueError` or `TypeError` for invalid batch sizes. Choose a consistent approach and document it.

### Example

```python
items = [1, 2, 3, 4, 5, 6, 7]

for batch in iter_batches(items, batch_size=3):
    print(batch)
```

Expected output:

```text
[1, 2, 3]
[4, 5, 6]
[7]
```

### Edge Cases to Consider

```python
iter_batches([], 3)
iter_batches([1, 2], 1)
iter_batches([1, 2, 3], 3)
iter_batches([1, 2, 3, 4], 3)
iter_batches([1, 2, 3], 0)
iter_batches([1, 2, 3], -1)
iter_batches([1, 2, 3], True)
iter_batches([1, 2, 3], 1.5)
```

---

## Task 3 – Build a Lazy Processing Pipeline

Combine the two generators from Task 1 and Task 2.

The goal is to filter packages first and then process them in batches.

### Example

```python
filtered_packages = iter_packages(
    packages,
    channel="stable",
    architecture="amd64",
)

batches = iter_batches(
    filtered_packages,
    batch_size=2,
)

for batch in batches:
    print(batch)
```

Expected output:

```text
[
    {"name": "firefox", ...},
    {"name": "vlc", ...}
]
```

### Requirements

1. Do not create an intermediate list of filtered packages.
2. The processing pipeline should remain lazy.
3. Packages should be processed only when the next batch is requested.
4. Preserve the original package order.
5. The pipeline should work with generator inputs, not just lists.

---

## Testing Requirements

Write pytest tests in `test_package_processor.py`.

Your tests should cover the following cases.

### Task 1 – Package Filter Generator

- Filter by channel.
- Filter by architecture.
- Filter by both channel and architecture.
- No filters provided.
- Empty input.
- Generator input.
- Preserve input order.
- Original package data is not modified.

### Task 2 – Batch Generator

- Split a list into multiple batches.
- Last batch contains fewer items.
- Input size is exactly divisible by batch size.
- Batch size is larger than the input.
- Empty input.
- Generator input.
- Invalid batch sizes:
  - `0`
  - negative integer
  - `True`
  - float value

### Task 3 – Lazy Processing Pipeline

- Combine filtering and batching.
- Verify that the pipeline works with generator inputs.
- Verify that the input is not consumed before iteration begins.
- Verify that packages are consumed incrementally rather than all at once.

**Important:** Do not only test the returned values. Also test the lazy behavior of your generators.

---

## Optional Questions

After completing the implementation, try to answer these questions.

1. What is the difference between an `Iterable` and an `Iterator`?
2. What is the difference between `yield` and `return`?
3. What is lazy evaluation? Why is it useful?
4. Can a generator be iterated more than once? Why or why not?
5. What happens when you call `list()` on a generator?
6. What are the memory advantages of generators compared with lists?
7. What happens if a generator raises an exception during iteration?

---

## Technical Requirements

- Use Python 3.10+.
- Use only the Python standard library.
- Do not use Django, FastAPI, or a database.
- Do not use third-party libraries for batching or filtering.
- Use generators and `yield` where required.
- Add appropriate type hints.
- Write unit tests using pytest.
- Keep the implementation simple and readable.

---

## Suggested Project Structure

```text
day03/
├── README.md
├── package_processor.py
└── test_package_processor.py
```

---

## Running Tests

Install pytest if it is not already installed:

```bash
python -m pip install pytest
```

Run all tests:

```bash
python -m pytest -v
```

Run tests with coverage:

```bash
python -m pytest --cov=package_processor --cov-report=term-missing
```

---

## Code Review Checklist

Before considering the exercise complete, review your implementation.

- [ ] Do the functions return generators instead of lists?
- [ ] Is the input processed lazily?
- [ ] Does the implementation avoid unnecessary memory allocation?
- [ ] Does it support different iterable types?
- [ ] Are edge cases handled correctly?
- [ ] Are invalid arguments handled consistently?
- [ ] Are type hints clear and accurate?
- [ ] Do the tests cover both normal and boundary cases?
- [ ] Is the code easy to read and maintain?

## Learning Objectives

By completing this exercise, you should understand:

- How Python generators and iterators work.
- How to use `yield`.
- How lazy evaluation works.
- How to build a generator pipeline.
- How to process large datasets with limited memory.
- How to test generator behavior with pytest.

These concepts are useful when implementing backend services that process large package indexes, API responses, database query results, and streaming data.
