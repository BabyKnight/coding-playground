# Day 2 – Snap Package Data Modeling with Python

**Difficulty:** Beginner to Intermediate  
**Estimated Time:** 45–60 minutes  
**Topic:** `dataclass`, OOP, Dictionary, Data Modeling, Exception Handling

## 1. Background

Imagine you are developing a simplified package management system similar to Snap Store.

A package can have multiple revisions. Each revision represents a specific release and contains:

- `number`: Revision number
- `version`: Package version
- `architecture`: CPU architecture

A package can also publish different revisions to different channels:

- `stable`
- `candidate`
- `beta`
- `edge`

For example:

```text
Package: firefox

Revision 101
  Version: 120.0
  Architecture: amd64
  Channel: stable

Revision 102
  Version: 121.0
  Architecture: arm64
  Channel: beta

Revision 103
  Version: 122.0
  Architecture: amd64
  Channel: edge
```

Your task is to implement a simple package management module using Python classes and data structures.

## 2. Tasks

### Task 1: Implement the Revision Data Model

Use Python's `dataclasses` module.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Revision:
    number: int
    version: str
    architecture: str
```

Requirements:

1. `number` must be a positive integer.
2. `bool` must not be accepted as a valid integer.
3. `version` must be a non-empty string.
4. `architecture` must be a non-empty string.
5. A Revision instance must be immutable after creation.

### Task 2: Implement the Package Class

Implement the following class:

```python
class Package:
    def __init__(self, name: str):
        pass

    def add_revision(self, revision: Revision) -> None:
        pass

    def promote(self, revision_number: int, channel: str) -> None:
        pass

    def get_release(
        self,
        channel: str,
        architecture: str
    ) -> Revision | None:
        pass
```

#### Requirements

**`__init__(name)`**

- Initialize a package.
- Package name must not be empty.

**`add_revision(revision)`**

- Add a Revision to the package.
- Duplicate revision numbers are not allowed.
- Only valid Revision objects can be added.

**`promote(revision_number, channel)`**

- Assign an existing revision to a channel.
- Only the following channels are allowed:
  - `stable`
  - `candidate`
  - `beta`
  - `edge`
- Raise an exception if the revision does not exist.
- Raise an exception if the channel is invalid.
- Publishing a new revision to the same channel and architecture should update the existing release.
- Releases for different architectures must remain independent.

**`get_release(channel, architecture)`**

- Return the Revision associated with the specified channel and architecture.
- Return `None` if no matching release exists.

## 3. Expected Usage

Your implementation should support the following operations:

```python
firefox = Package("firefox")

firefox.add_revision(
    Revision(101, "120.0", "amd64")
)

firefox.add_revision(
    Revision(102, "121.0", "arm64")
)

firefox.add_revision(
    Revision(103, "122.0", "amd64")
)

firefox.promote(101, "stable")
firefox.promote(102, "beta")
firefox.promote(103, "stable")

print(firefox.get_release("stable", "amd64"))
# Revision(number=103, version='122.0', architecture='amd64')

print(firefox.get_release("beta", "arm64"))
# Revision(number=102, version='121.0', architecture='arm64')

print(firefox.get_release("stable", "arm64"))
# None
```

## 4. Constraints and Edge Cases

Your implementation should handle the following cases:

- [ ] Empty package name.
- [ ] Revision number is zero.
- [ ] Revision number is negative.
- [ ] Revision number is a boolean value (`True` or `False`).
- [ ] Empty version string.
- [ ] Empty architecture string.
- [ ] Adding a duplicate revision number.
- [ ] Adding an invalid object instead of a Revision.
- [ ] Promoting a non-existent revision.
- [ ] Using an unsupported channel.
- [ ] Promoting multiple revisions to the same channel and architecture.
- [ ] Promoting different architectures to the same channel.
- [ ] Querying a channel or architecture without a release.

## 5. Testing Requirements

Use `pytest` to write unit tests.

Suggested test cases:

| Test | Expected Result |
|---|---|
| Create a valid package | Success |
| Create a package with an empty name | Raise exception |
| Create a valid revision | Success |
| Create revision with number 0 | Raise exception |
| Create revision with `True` as number | Raise exception |
| Modify a frozen Revision | Raise exception |
| Add a valid revision | Success |
| Add duplicate revision | Raise exception |
| Promote an existing revision | Success |
| Promote a non-existent revision | Raise exception |
| Promote to an invalid channel | Raise exception |
| Query an existing release | Return Revision |
| Query a missing release | Return None |
| Update an existing channel release | Return the newly promoted Revision |
| Publish different architectures | Keep releases independent |

## 6. Additional Questions (Optional)

Think about the following questions after completing the implementation.

### 6.1 Data Modeling

Why is `@dataclass(frozen=True)` a good choice for the Revision class?

What are the advantages of using a dataclass instead of a regular Python class?

### 6.2 Data Structures

How would you store revisions inside the Package class?

Consider these two options:

```python
revisions = []
```

```python
revisions = {}
```

Which one is more suitable if you frequently look up revisions by revision number? Why?

### 6.3 Channel Management

How would you design the internal data structure to efficiently retrieve a revision by channel and architecture?

For example:

```python
get_release("stable", "amd64")
```

Consider the advantages of using nested dictionaries.

### 6.4 Software Design

Why should business validation be implemented inside the data model or business methods rather than relying only on API-level validation?

## 7. Technical Requirements

- Python 3.10+
- Use Python standard library only.
- Use `dataclasses` where appropriate.
- Use type hints.
- Use meaningful exception types.
- Do not use Django, FastAPI, SQLAlchemy, or a database.
- Write unit tests using `pytest`.

## 8. Code Review Checklist

After implementation, review your code against the following criteria:

- [ ] Correctness: All business requirements are implemented.
- [ ] Pythonic: Use appropriate Python features and idioms.
- [ ] Data Structures: Choose efficient data structures.
- [ ] Complexity: Consider lookup and update time complexity.
- [ ] Validation: Handle invalid inputs correctly.
- [ ] Exceptions: Use meaningful exception types.
- [ ] Type Hints: Provide clear type annotations.
- [ ] Maintainability: Keep responsibilities well separated.
- [ ] Testing: Cover normal cases and edge cases.

---

**Submission**

Submit the following files for review:

```text
day02/
├── package.py
└── test_package.py
```

The goal is not to write as much code as possible. Focus on clean data modeling, correct business logic, appropriate data structures, and reliable tests.

Do not look for a complete reference implementation before attempting the exercise. Once you submit your code, perform a code review focusing on correctness, Pythonic style, performance, maintainability, and test coverage.
