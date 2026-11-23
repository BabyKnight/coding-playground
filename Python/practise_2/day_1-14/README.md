# Python 面试能力恢复计划：第一阶段（Day 1--Day 14）

> 训练方式：每天独立完成题目，提交代码进行
> Review；重点检查正确性、边界条件、异常处理、性能、复杂度和 pytest。

## 一、14 天训练路线

  天数     核心主题                           主要训练目标
  -------- ---------------------------------- -------------------------------
  Day 1    Python 基础、数据类型              数据处理与边界条件
  Day 2    List / Dict / Set / Tuple          数据结构操作
  Day 3    Comprehension / Lambda / Sorting   Pythonic 编码
  Day 4    Collections                        Counter / defaultdict / deque
  Day 5    Iterator                           迭代协议与自定义迭代器
  Day 6    Generator                          yield、惰性计算
  Day 7    Iterator + Generator               流式处理与批处理
  Day 8    Decorator                          装饰器、闭包、参数传递
  Day 9    Context Manager                    with、资源管理
  Day 10   itertools                          高级迭代工具
  Day 11   JSON                               数据序列化与校验
  Day 12   File Processing                    大文件、流式读写
  Day 13   pytest                             单元测试、Fixture、Mock
  Day 14   Type Hints + 综合项目              工程化代码能力

------------------------------------------------------------------------

# Day 1：Python 基础与数据类型

**知识点：** Mutable vs Immutable、None/bool/int/float/str、`is` vs
`==`、Truthy/Falsy、`*args`/`**kwargs`、Shallow Copy/Deep
Copy、异常处理、常见 Python 陷阱。

## 题目 1：数据类型与输入清洗

实现：

``` python
def normalize_value(value):
    """
    Normalize input values.

    Rules:
    1. None -> None
    2. String -> strip whitespace
    3. Empty string -> None
    4. Integer / Float -> return unchanged
    5. Boolean -> return unchanged
    6. Other types -> raise TypeError
    """
```

要求： - 正确区分 `bool` 和 `int`。 - 不允许将数字 `0` 错误地处理成
`None`。 - 不允许修改原始对象。

## 题目 2：Mutable Object 陷阱

分析并修复：

``` python
def add_item(item, items=[]):
    items.append(item)
    return items
```

要求： 1. 解释为什么多次调用会产生意外结果。 2. 修复代码。 3. 编写
pytest 测试验证修复。 4. 分析以下写法的区别：

``` python
a = [1, 2, 3]
b = a
c = a.copy()
```

## 题目 3：Shallow Copy vs Deep Copy

实现：

``` python
import copy

def clone_config(config, deep=False):
    """
    Clone a nested configuration dictionary.

    deep=False: shallow copy
    deep=True: deep copy
    """
```

测试数据：

``` python
config = {
    "app": "monitor",
    "settings": {
        "theme": "dark",
        "features": ["cpu", "memory"]
    }
}
```

要求： - 修改 shallow copy 的嵌套对象，观察原始对象是否变化。 - 修改
deep copy 的嵌套对象，观察原始对象是否变化。 - 解释两种复制的区别。

## 题目 4：`is` vs `==`

判断输出并解释原因：

``` python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

x = None
y = None

print(x is y)

a = 1000
b = 1000

print(a == b)
print(a is b)
```

额外问题：为什么判断 None 推荐使用 `if value is None:`，而不是
`if value == None:`？

## 题目 5：函数参数设计

实现：

``` python
def create_user(username, *roles, active=True, **metadata):
    """
    Create a user dictionary.

    Example:
    create_user(
        "vincent",
        "admin",
        "developer",
        active=True,
        department="engineering",
        location="Shanghai"
    )
    """
```

要求： - `roles` 保存成 tuple。 - `metadata` 保存成 dict。 - `active`
必须是 bool。 - username 不能为空。 - 解释 positional-only、keyword-only
参数的区别。

## 题目 6：异常处理

实现：

``` python
def safe_divide(a, b):
    """
    Return a / b.

    Handle:
    - ZeroDivisionError
    - TypeError
    - ValueError
    """
```

要求： - 不要使用过度宽泛的 `except Exception`。 -
不要吞掉异常后返回不明确的值。 - 对异常进行合理处理。 - 解释 `raise` 和
`raise e` 的区别。

------------------------------------------------------------------------

# Day 2：List / Dict / Set / Tuple

**知识点：** List、Dict、Set、Tuple、时间复杂度、Hashable、Dict Key、Set
去重、嵌套数据结构、Dict 合并、数据转换。

## 题目 1：List 去重并保持顺序

实现：

``` python
def unique_items(items):
    """
    Remove duplicates while preserving original order.
    """
```

输入：

``` python
[3, 1, 2, 3, 2, 4, 1]
```

输出：

``` python
[3, 1, 2, 4]
```

要求： - 不允许排序。 - 尽量达到 O(n) 时间复杂度。 - 额外考虑不可 Hash
的元素，例如嵌套 list。

## 题目 2：Dict 合并

实现：

``` python
def merge_configs(default, user):
    """
    Merge user configuration into default configuration.

    User configuration overrides default values.
    """
```

输入：

``` python
default = {
    "theme": "light",
    "timeout": 30,
    "features": {
        "cpu": True,
        "memory": True
    }
}

user = {
    "theme": "dark",
    "features": {
        "cpu": False
    }
}
```

期望：

``` python
{
    "theme": "dark",
    "timeout": 30,
    "features": {
        "cpu": False,
        "memory": True
    }
}
```

要求： - 实现递归 Deep Merge。 - 不修改输入的两个 dict。 -
处理不同类型的同名字段。 - 考虑 list 应该合并还是覆盖，并说明设计。

## 题目 3：查找重复元素

实现：

``` python
def find_duplicates(items):
    """
    Return all duplicated values.

    Each duplicated value should appear only once
    in the result.
    """
```

输入：

``` python
["a", "b", "c", "a", "b", "d", "a"]
```

输出：

``` python
["a", "b"]
```

要求： - 使用 Set 优化。 - 保持重复元素首次被确认时的顺序。 -
分析时间和空间复杂度。

## 题目 4：Dict 反转

实现：

``` python
def invert_dict(data):
    """
    Invert dictionary keys and values.

    If multiple keys have the same value,
    group original keys into a list.
    """
```

输入：

``` python
{
    "alice": "admin",
    "bob": "developer",
    "charlie": "admin"
}
```

输出：

``` python
{
    "admin": ["alice", "charlie"],
    "developer": ["bob"]
}
```

要求：考虑 value 不可 Hash 的情况，并解释为什么普通 dict 不能直接使用
list 作为 key。

## 题目 5：嵌套数据提取

实现：

``` python
def flatten_list(items):
    """
    Flatten arbitrarily nested lists.
    """
```

输入：

``` python
[1, [2, 3], [4, [5, 6]], 7]
```

输出：

``` python
[1, 2, 3, 4, 5, 6, 7]
```

要求： - 使用递归实现。 - 不修改原始数据。 - 额外考虑 tuple
是否也应该展开。 - 讨论递归深度过大时的问题。

## 题目 6：数据结构选择

下面场景应该选择什么数据结构？解释理由及复杂度。

1.  保存唯一的 package name。
2.  保存 package name 到 version 的映射。
3.  保存需要保持顺序的历史记录。
4.  保存不可变的坐标信息。
5.  快速检查某个用户是否具有指定权限。
6.  实现先进先出的任务队列。

------------------------------------------------------------------------

# Day 3：Comprehension / Lambda / Sorting

**知识点：** List/Dict/Set Comprehension、Generator
Expression、Lambda、`sorted()` vs `list.sort()`、`key`
Function、多字段排序、`enumerate()`/`zip()`、`any()`/`all()`。

## 题目 1：List Comprehension

给定：

``` python
packages = [
    {"name": "firefox", "version": "120", "arch": "amd64"},
    {"name": "kernel", "version": "6.8", "arch": "amd64"},
    {"name": "firefox", "version": "121", "arch": "arm64"},
    {"name": "vim", "version": "9.0", "arch": "amd64"},
]
```

实现：

``` python
def get_amd64_package_names(packages):
    ...
```

输出：

``` python
["firefox", "kernel", "vim"]
```

分别使用普通 for 循环和 List Comprehension 实现。

## 题目 2：Dict Comprehension

实现：

``` python
def package_version_map(packages):
    """
    Return package name -> version mapping.
    """
```

输出：

``` python
{
    "firefox": "121",
    "kernel": "6.8",
    "vim": "9.0"
}
```

要求：同名 package 出现多次时，保留最后一次出现的版本。

## 题目 3：多条件排序

实现：

``` python
def sort_packages(packages):
    """
    Sort packages by:
    1. architecture: amd64 before arm64
    2. name: alphabetical
    3. version: descending
    """
```

要求： - 使用 `sorted()`。 - 不修改原始 list。 -
不要直接对版本号字符串使用普通降序排序后就认为语义正确。 - 考虑版本号
`1.9`、`1.10`、`1.11`。

## 题目 4：Lambda 与 Key Function

给定：

``` python
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
]
```

分别实现：

1.  按 age 升序。
2.  按 age 升序，name 降序。
3.  使用 `operator.itemgetter` 实现多字段排序。
4.  解释 Lambda 和普通函数作为 key 的区别。

## 题目 5：any() / all()

实现：

``` python
def validate_packages(packages):
    """
    Return True only if:
    - packages is not empty
    - every package has a non-empty name
    - every package has a valid architecture
    """
```

合法架构：

``` python
{"amd64", "arm64"}
```

要求： - 使用 `any()` 和 `all()`。 - 考虑空 list 的特殊行为。 -
考虑短路求值。

## 题目 6：Generator Expression

给定一百万条日志记录：

``` python
logs = [...]
```

提取所有 ERROR 日志，分别使用 List Comprehension 和 Generator
Expression。

解释： - 内存使用区别。 - 什么时候应该使用 Generator Expression。 -
为什么生成器只能被完整消费一次。

------------------------------------------------------------------------

# Day 4：Collections

**知识点：**
`collections.Counter`、`defaultdict`、`deque`、`namedtuple`、`OrderedDict`、`ChainMap`、频率统计、分组、滑动窗口。

## 题目 1：Counter 统计

实现：

``` python
from collections import Counter

def count_architectures(packages):
    ...
```

输入：

``` python
[
    {"name": "firefox", "architecture": "amd64"},
    {"name": "vim", "architecture": "amd64"},
    {"name": "kernel", "architecture": "arm64"},
    {"name": "curl", "architecture": "amd64"},
]
```

输出：

``` python
{
    "amd64": 3,
    "arm64": 1
}
```

要求： - 使用 Counter。 - 使用 `most_common()`。 - 解释 Counter
相加、相减、交集、并集的行为。

## 题目 2：defaultdict 分组

实现：

``` python
def group_packages(packages):
    """
    Group package names by architecture.
    """
```

要求： - 使用 defaultdict(list)。 - 不使用 `if key not in dict`。 - 解释
defaultdict 和 dict.setdefault() 的区别。

## 题目 3：defaultdict 陷阱

解释：

``` python
from collections import defaultdict

data = defaultdict(list)

print(data["ubuntu"])
print(data)
print("debian" in data)
```

问题： 1. 为什么访问不存在的 key 后，dict 内容发生了变化？ 2. `get()` 和
`[]` 访问有什么区别？ 3. 什么时候不应该使用 defaultdict？

## 题目 4：Deque 实现任务队列

实现：

``` python
class TaskQueue:
    def add_task(self, task):
        ...

    def get_task(self):
        ...

    def get_pending_count(self):
        ...
```

要求： - 使用 deque。 - FIFO。 - 队列为空时合理处理。 -
解释为什么不建议使用 list 的 `pop(0)` 实现高性能队列。

## 题目 5：滑动窗口

实现：

``` python
def moving_average(numbers, window_size):
    """
    Return moving averages for each complete window.
    """
```

输入：

``` python
[1, 2, 3, 4, 5]
```

窗口大小为 `3`，输出：

``` python
[2.0, 3.0, 4.0]
```

要求： - 使用 deque。 - 时间复杂度 O(n)。 - 不允许每次重新计算整个窗口的
sum。

## 题目 6：Counter 高级应用

给定：

``` python
logs = [
    "ERROR",
    "INFO",
    "ERROR",
    "WARNING",
    "INFO",
    "ERROR"
]
```

实现：

``` python
def analyze_logs(logs):
    """
    Return:
    - total count
    - frequency by level
    - most common level
    - levels appearing more than once
    """
```

------------------------------------------------------------------------

# Day 5：Iterator

**知识点：** Iterable vs
Iterator、`iter()`、`next()`、`StopIteration`、`__iter__()`、`__next__()`、Iterator
Protocol、Iterator Exhaustion、`iter(callable, sentinel)`。

## 题目 1：Iterable 与 Iterator

解释并验证：

``` python
numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

继续执行：

``` python
print(next(iterator))
```

问题： 1. 为什么会出现 StopIteration？ 2. List 和 Iterator
的区别是什么？ 3. 为什么 list 可以重复遍历，而 iterator 通常不行？

## 题目 2：自定义 Iterator

实现：

``` python
class Countdown:
    def __init__(self, start):
        ...

    def __iter__(self):
        ...

    def __next__(self):
        ...
```

示例：

``` python
for number in Countdown(5):
    print(number)
```

输出：

``` python
5
4
3
2
1
```

要求： - 正确实现 Iterator Protocol。 - 到达结束条件时抛出
StopIteration。 - 解释 `iter(obj) is obj` 的意义。

## 题目 3：自定义可迭代对象

实现：

``` python
class PackageCollection:
    def __init__(self, packages):
        ...

    def __iter__(self):
        ...
```

要求： - 可以重复遍历。 - 不应该直接让 PackageCollection 本身成为一次性
Iterator。 - 支持 `for`、`list()` 和 `sum()` 等操作。

## 题目 4：Iterator 消费问题

分析：

``` python
iterator = iter([1, 2, 3])

print(list(iterator))
print(list(iterator))
```

解释为什么第二次为空。

实现：

``` python
def inspect_iterator(iterator):
    """
    Return the first item and all remaining items.
    """
```

要求：不能错误地丢失已经读取的元素。

## 题目 5：iter(callable, sentinel)

使用：

``` python
iter(callable, sentinel)
```

实现一个从文件或数据源逐条读取内容的示例。

解释： - callable 如何被调用？ - sentinel 的作用是什么？ - 和普通 for
循环有什么区别？

------------------------------------------------------------------------

# Day 6：Generator

**知识点：** `yield`、`yield from`、Generator Function、Generator
Object、Lazy Evaluation、`send()`、`close()`、`throw()`、Generator
State。

## 题目 1：基础 Generator

实现：

``` python
def generate_numbers(start, end):
    """
    Generate numbers from start to end inclusive.
    """
```

要求： - 使用 yield。 - 不允许先创建完整 list。 - 支持大范围数据。

## 题目 2：Generator 与 List 对比

分别实现：

``` python
def get_even_numbers_list(numbers):
    ...

def get_even_numbers_generator(numbers):
    ...
```

要求： - 对比内存占用。 - 解释执行时机。 - 使用 `sys.getsizeof()`
进行实验，并解释为什么它不能准确代表生成器实际会使用的总内存。

## 题目 3：yield from

实现：

``` python
def flatten(items):
    """
    Flatten nested lists using yield from.
    """
```

输入：

``` python
[1, [2, 3], [4, [5, 6]]]
```

输出：

``` python
[1, 2, 3, 4, 5, 6]
```

要求： - 使用 yield from。 - 对比普通 yield。 - 解释 yield from
的委托行为。

## 题目 4：Generator send()

实现一个简单的累加器：

``` python
def accumulator():
    ...
```

期望使用：

``` python
acc = accumulator()

next(acc)
acc.send(10)
acc.send(20)
acc.send(5)
```

理解： - `send()` 的作用。 - 为什么首次调用通常需要 `next()` 或
`send(None)`。 - yield 表达式如何接收 send 传入的值。

## 题目 5：Generator 生命周期

分析：

``` python
def sample():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Cleanup")
```

测试： - 正常遍历。 - `close()`。 - `throw()`。 - 提前停止遍历。

解释 finally
什么时候执行，以及为什么不能依赖生成器被垃圾回收时才释放重要资源。

------------------------------------------------------------------------

# Day 7：Iterator + Generator 综合实战

**场景：** Linux 软件包管理、日志处理和数据处理。

## 题目 1：批量数据处理

实现：

``` python
def iter_batches(items, batch_size):
    """
    Yield items in batches.

    Example:
    [1, 2, 3, 4, 5], batch_size=2

    Output:
    [1, 2]
    [3, 4]
    [5]
    """
```

要求： - 使用 Generator。 - 不创建完整的批次列表。 - batch_size 必须大于
0。 - 处理空输入。

## 题目 2：Package Iterator Pipeline

实现：

``` python
def iter_packages(
    packages,
    channel=None,
    architecture=None
):
    """
    Filter packages lazily.
    """
```

测试数据：

``` python
packages = [
    {
        "name": "firefox",
        "channel": "stable",
        "architecture": "amd64"
    },
    {
        "name": "vim",
        "channel": "stable",
        "architecture": "arm64"
    },
    {
        "name": "kernel",
        "channel": "edge",
        "architecture": "amd64"
    }
]
```

要求： - 支持 channel 过滤。 - 支持 architecture 过滤。 -
支持两个过滤条件同时使用。 - 惰性处理。 - 不修改原始数据。

## 题目 3：Pipeline 组合

实现：

``` python
def filter_errors(logs):
    ...

def extract_timestamps(logs):
    ...

def iter_batches(items, batch_size):
    ...
```

将三个函数组合成处理 Pipeline：

``` text
Log Source
    ↓
Filter ERROR
    ↓
Extract Timestamp
    ↓
Batch Processing
```

要求： - 每个阶段独立。 - 使用 Generator。 - 不创建中间完整 list。 -
支持百万条日志。

## 题目 4：无限序列

实现：

``` python
def fibonacci():
    """
    Generate an infinite Fibonacci sequence.
    """
```

要求： - 使用 yield。 - 不允许生成完整序列。 - 使用 `itertools.islice()`
获取前 20 项。 - 解释如何安全地消费无限生成器。

## 题目 5：综合代码 Review

分析以下代码中的所有问题：

``` python
def process_packages(packages):
    result = []

    for pkg in packages:
        if pkg["architecture"] == "amd64":
            result.append(pkg["name"])

    return result
```

要求： 1. 改造成惰性 Generator。 2. 使用 `.get()` 处理缺失字段。 3. 支持
architecture 参数。 4. 支持批量处理。 5. 考虑输入本身是 Iterator
的情况。 6. 解释原代码在处理大型数据时的内存问题。

------------------------------------------------------------------------

# Day 8：Decorator

**知识点：** Function as First-Class
Object、Closure、Decorator、`*args`/`**kwargs`、`functools.wraps`、Parameterized
Decorator、Stacking Decorators、Decorator Execution Order。

## 题目 1：基础 Decorator

实现：

``` python
def log_execution(func):
    ...
```

要求：调用函数前打印函数名，调用结束后打印执行完成；支持任意参数和返回值。

## 题目 2：functools.wraps

分析：

``` python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

比较：

``` python
@my_decorator
def calculate(a, b):
    """Calculate sum."""
    return a + b
```

与使用 `@wraps(func)` 的区别。

要求： - 查看 `__name__`。 - 查看 `__doc__`。 - 查看
`inspect.signature()`。

## 题目 3：带参数的 Decorator

实现：

``` python
@retry(max_attempts=3, delay=1)
def fetch_data():
    ...
```

要求： - 最多执行指定次数。 - 成功时返回结果。 - 失败时重试。 -
超过次数后抛出最后一次异常。 - 不要捕获 KeyboardInterrupt
等不应该重试的异常。

## 题目 4：执行时间统计

实现：

``` python
@measure_time
def process_data():
    ...
```

要求： - 使用 `time.perf_counter()`。 - 支持有返回值的函数。 -
支持异常。 - 不改变原函数的返回行为。

## 题目 5：Decorator 执行顺序

分析：

``` python
@decorator_a
@decorator_b
def test():
    pass
```

问题： 1. 实际执行顺序是什么？ 2. 等价于什么代码？ 3.
如果交换两个装饰器，可能产生什么变化？

------------------------------------------------------------------------

# Day 9：Context Manager

**知识点：**
`with`、`__enter__`、`__exit__`、`contextlib.contextmanager`、Resource
Management、Exception Suppression、File/Lock/Database Resource。

## 题目 1：自定义 Context Manager

实现：

``` python
class Timer:
    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_value, traceback):
        ...
```

使用：

``` python
with Timer():
    process_data()
```

要求： - 记录执行时间。 - 无论是否发生异常，都执行清理逻辑。 -
不吞掉异常。

## 题目 2：文件资源管理

分析：

``` python
file = open("data.txt")

try:
    data = file.read()
finally:
    file.close()
```

与：

``` python
with open("data.txt") as file:
    data = file.read()
```

的区别。

要求： - 解释上下文管理器的作用。 - 解释文件异常时的资源释放。 -
编写一个安全的文件读取函数。

## 题目 3：contextlib.contextmanager

使用：

``` python
from contextlib import contextmanager
```

实现：

``` python
@contextmanager
def managed_resource():
    ...
```

要求： - yield 前执行初始化。 - yield 后执行清理。 -
异常发生时仍执行清理。 - 理解异常如何在 yield 位置重新抛出。

## 题目 4：异常是否被吞掉

实现一个 Context Manager，支持：

``` python
with IgnoreError(ValueError):
    raise ValueError("Invalid data")
```

要求： - 只忽略指定类型的异常。 - 其他异常正常抛出。 - 理解 `__exit__()`
的返回值。

## 题目 5：多资源管理

实现：

``` python
with open("input.txt") as src, open("output.txt", "w") as dst:
    ...
```

进一步使用 `ExitStack` 管理动态数量的文件资源。

解释为什么多个资源管理时 Context Manager 更安全。

------------------------------------------------------------------------

# Day 10：itertools

**知识点：**
`chain`、`islice`、`product`、`permutations`、`combinations`、`groupby`、`cycle`、`count`、`takewhile`、`dropwhile`、`zip_longest`。

## 题目 1：chain

实现：

``` python
from itertools import chain

def merge_iterables(*iterables):
    ...
```

输入：

``` python
[1, 2], [3, 4], [5, 6]
```

输出：

``` python
[1, 2, 3, 4, 5, 6]
```

要求：惰性合并，不创建额外的大型 list。

## 题目 2：islice

给定一个生成器：

``` python
def generate_logs():
    ...
```

使用 `islice()`： - 获取前 10 条。 - 获取第 100～110 条。 - 每隔 5
条获取一条。

解释为什么 `islice()` 不支持像 list 一样直接倒序访问。

## 题目 3：product / combinations / permutations

给定：

``` python
architectures = ["amd64", "arm64"]
channels = ["stable", "edge"]
```

要求： 1. 生成所有架构和 channel 的组合。 2. 从 4 个 package 中选出 2
个。 3. 生成 3 个元素的所有排列。

解释三者的区别及组合数量。

## 题目 4：groupby 陷阱

给定：

``` python
from itertools import groupby

data = [
    ("amd64", "firefox"),
    ("arm64", "vim"),
    ("amd64", "kernel"),
]
```

使用 `groupby()` 按架构分组。

要求： - 先分析不排序直接 groupby 的结果。 - 再实现正确分组。 - 解释
groupby 为什么只对连续相同的 key 进行分组。 - 解释 groupby
迭代器的生命周期问题。

## 题目 5：zip_longest

实现：

``` python
def merge_package_versions(names, versions):
    ...
```

要求： - 使用 `zip_longest()`。 - 处理两组数据长度不同的情况。 -
不允许静默丢弃多余数据。 - 解释 `zip()` 与 `zip_longest()` 的区别。

------------------------------------------------------------------------

# Day 11：JSON Processing

**知识点：**
`json.loads()`、`json.dumps()`、`json.load()`、`json.dump()`、Serialization/Deserialization、JSON
Validation、Encoding、Nested JSON、JSON Error Handling。

## 题目 1：JSON 转换

实现：

``` python
def parse_json(data):
    ...
```

要求： - 输入 JSON 字符串。 - 返回 Python 对象。 - 处理
JSONDecodeError。 - 不允许使用 `eval()`。

## 题目 2：JSON 序列化

实现：

``` python
def serialize_data(data):
    ...
```

要求： - 使用 `json.dumps()`。 - 支持中文。 - 输出格式化 JSON。 -
处理不能直接 JSON 序列化的对象。

重点理解：

``` python
ensure_ascii=False
indent=4
sort_keys=True
```

## 题目 3：JSON 数据校验

给定：

``` python
package = {
    "name": "firefox",
    "version": "120",
    "architecture": "amd64",
    "dependencies": ["libc", "libssl"]
}
```

实现：

``` python
def validate_package(package):
    ...
```

要求： - name 必须是非空字符串。 - version 必须是字符串。 - architecture
必须是合法值。 - dependencies 必须是 list。 - 不允许存在非法字段类型。

## 题目 4：嵌套 JSON 提取

给定：

``` python
data = {
    "system": {
        "os": {
            "name": "Ubuntu",
            "version": "24.04"
        },
        "hardware": {
            "cpu": {
                "model": "Intel",
                "cores": 16
            }
        }
    }
}
```

实现：

``` python
def get_nested_value(data, path, default=None):
    ...
```

调用：

``` python
get_nested_value(data, "system.os.version")
```

输出：

``` python
"24.04"
```

要求：处理中间字段不存在、类型不正确的情况。

## 题目 5：JSONL 日志处理

实现：

``` python
def iter_jsonl(file_path):
    """
    Read JSON Lines file lazily.
    """
```

要求： - 一行一个 JSON 对象。 - 使用 Generator。 - 空行跳过。 - JSON
格式错误时提供行号。 - 不一次性读取整个文件。

------------------------------------------------------------------------

# Day 12：File Processing

**知识点：** `open()`、File
Modes、Encoding、Buffering、`read()`/`readline()`/`readlines()`、File
Iterator、Large File Processing、CSV/JSONL、Pathlib、Atomic Write。

## 题目 1：文件读取

实现：

``` python
def read_lines(file_path):
    ...
```

要求： - 使用 UTF-8。 - 去掉行尾换行符。 - 保留行内容中的其他空格。 -
文件不存在时合理处理。 - 使用 Generator。

## 题目 2：大文件处理

假设一个日志文件大小为 10GB。

分别使用：

``` python
file.read()
file.readlines()
for line in file:
```

解释三者的内存使用差异。

实现：

``` python
def count_error_logs(file_path):
    ...
```

要求： - 流式处理。 - 不将全部日志加载到内存。 - 统计 ERROR 数量。

## 题目 3：文件编码

处理包含中文的文件。

要求： - 分别使用 UTF-8 和错误编码读取。 - 理解 `UnicodeDecodeError`。 -
解释 `errors="ignore"` 和 `errors="replace"` 的区别。 -
说明为什么不能随意忽略编码错误。

## 题目 4：Pathlib

实现：

``` python
from pathlib import Path

def find_json_files(directory):
    ...
```

要求： - 递归查找所有 JSON 文件。 - 排除隐藏目录。 - 返回 Path 对象。 -
文件不存在或路径不是目录时合理处理。

## 题目 5：Atomic File Write

实现：

``` python
def atomic_write(file_path, content):
    ...
```

要求： - 先写入临时文件。 - 成功后通过 `os.replace()` 替换目标文件。 -
写入失败时不破坏原文件。 - 考虑临时文件清理。 -
理解原子替换和数据持久化并不是同一个概念。

------------------------------------------------------------------------

# Day 13：pytest

**知识点：** Test Function
Naming、Assertions、Fixtures、Parametrize、Exception
Testing、Mock/Patch、Setup/Teardown、Test Isolation、Coverage。

## 题目 1：基础 Unit Test

为 Day 2 的：

``` python
unique_items(items)
```

编写 pytest 测试。

要求： - 正常输入。 - 空 list。 - 全部重复。 - 无重复。 - 单元素。 -
不可 Hash 元素。

## 题目 2：Parametrize

使用：

``` python
@pytest.mark.parametrize(...)
```

为以下函数设计测试：

``` python
def normalize_value(value):
    ...
```

要求： - 至少 8 组输入。 - 同时测试正常情况和异常情况。 -
不允许为了通过测试而修改函数逻辑。

## 题目 3：Fixture

实现 Fixture：

``` python
@pytest.fixture
def sample_packages():
    ...
```

要求： - 多个测试共享测试数据。 - 测试之间不能相互污染。 -
测试后清理临时资源。 - 理解 Fixture
Scope：function、class、module、session。

## 题目 4：异常测试

测试：

``` python
def divide(a, b):
    return a / b
```

要求： - 使用 `pytest.raises()`。 - 验证异常类型。 - 验证异常消息。 -
验证异常发生时的预期行为。

## 题目 5：Mock / Patch

假设：

``` python
def get_system_info():
    import subprocess
    return subprocess.check_output(
        ["uname", "-a"],
        text=True
    )
```

要求： - 使用 Mock，不实际调用系统命令。 - 模拟正常返回。 -
模拟命令执行失败。 - 理解 Mock 与 MagicMock。 - 理解为什么通常应该 patch
被测试模块实际查找依赖的路径。

## 题目 6：测试覆盖率与测试设计

为一个 Package Manager 模块设计测试结构：

``` text
package_manager/
    __init__.py
    manager.py
    validator.py

tests/
    test_manager.py
    test_validator.py
    conftest.py
```

要求： - 至少 15 个测试用例。 - 覆盖正常路径、异常路径、边界情况。 -
使用 pytest-cov 查看覆盖率。 - 解释 Statement Coverage 和 Branch
Coverage 的区别。

------------------------------------------------------------------------

# Day 14：Type Hints + 综合项目

**知识点：** Type
Hints、`Optional`/`Union`、`list[str]`/`dict[str, Any]`、`TypedDict`、`Protocol`、`TypeVar`、Generic、`Iterable`/`Iterator`/`Generator`、`Callable`、综合代码设计。

## 题目 1：Type Hints 基础

为以下函数补充完整 Type Hints：

``` python
def filter_packages(packages, architecture=None):
    ...

def get_package_map(packages):
    ...

def iter_batches(items, batch_size):
    ...

def safe_parse_json(data):
    ...
```

要求： - 使用 Python 3.10+ 类型语法。 - 正确区分
Iterable、Iterator、Generator。 - 使用 Optional 或 `| None`。 - 不要滥用
Any。

## 题目 2：TypedDict

定义：

``` python
class Package(TypedDict):
    ...
```

字段：

``` python
{
    "name": "firefox",
    "version": "120",
    "architecture": "amd64",
    "channel": "stable"
}
```

要求： - 定义完整类型。 - 说明 Required 和 NotRequired 的区别。 - 解释
TypedDict 与普通 dict 的区别。 - 解释 TypedDict
是否会在运行时强制验证类型。

## 题目 3：Generic

实现：

``` python
from typing import TypeVar, Generic

T = TypeVar("T")

class Repository(Generic[T]):
    ...
```

要求： - 支持存储任意类型的数据。 - 支持 add、get、remove。 -
添加类型提示。 - 解释 Generic 的实际价值。

## 题目 4：Protocol

定义：

``` python
class Storage(Protocol):
    ...
```

要求： - 定义 save 和 load 接口。 - 实现 FileStorage。 - 实现
MemoryStorage。 - 让同一个函数可以接受两种 Storage。 - 解释 Protocol 与
ABC 的区别。

## 题目 5：综合项目------Linux Package Processing System

实现一个简单的 Package Processing System。

### 项目处理流程

``` text
JSON / JSONL Input
        |
        v
Validation
字段校验、类型检查、异常处理
        |
        v
Iterator / Generator Pipeline
过滤、惰性计算、批量处理
        |
        v
Collections / Statistics
统计架构、channel、package 数量
        |
        v
JSON Output + pytest
输出处理结果并验证正确性
```

### 项目要求

1.  从 JSON 或 JSONL 文件读取 package 数据。
2.  使用 TypedDict 定义 Package。
3.  校验必需字段及字段类型。
4.  支持 architecture、channel 过滤。
5.  使用 Generator 实现惰性处理。
6.  使用 Iterator 实现可重复遍历的数据集合。
7.  使用 `iter_batches()` 实现批量处理。
8.  使用 Counter 统计不同架构的 package 数量。
9.  使用 defaultdict 按 channel 分组。
10. 使用 Decorator 记录函数执行时间。
11. 使用 Context Manager 管理文件资源。
12. 输出统计结果到 JSON 文件。
13. 使用 pytest 编写完整测试。
14. 所有核心函数都必须有 Type Hints。
15. 不能因为一条无效 package 导致整个数据处理任务意外终止。

### 建议项目目录

``` text
package_processor/
│
├── __init__.py
├── models.py
├── validator.py
├── iterator.py
├── processor.py
├── statistics.py
├── storage.py
├── decorators.py
└── main.py
│
└── tests/
    ├── conftest.py
    ├── test_validator.py
    ├── test_iterator.py
    ├── test_processor.py
    └── test_storage.py
```

------------------------------------------------------------------------

# 三、统一代码提交与评分标准

## 每天代码要求

  项目          要求
  ------------- ----------------------
  Python 版本   Python 3.10+
  Type Hints    核心函数必须添加
  代码风格      PEP 8
  测试框架      pytest
  异常处理      必须考虑
  边界条件      必须测试
  时间复杂度    能分析的题目必须分析
  空间复杂度    能分析的题目必须分析

## 每日 100 分评分体系

  评分项目              分值 评价内容
  ---------------- --------- ----------------------------------
  功能正确性              40 正常输入、边界输入、异常输入
  代码质量                20 可读性、Pythonic、函数设计
  边界与异常处理          15 空值、类型错误、重复数据等
  性能与复杂度            15 时间复杂度、空间复杂度、惰性处理
  测试质量                10 pytest 覆盖率和测试设计
  **总分**           **100** 

## 每日 Code Review 内容

每天提交代码后，按以下结构进行 Review：

1.  **评分**：每题得分及当天总分。
2.  **正确性**：指出 Bug 和遗漏的边界条件。
3.  **代码 Review**：指出不够 Pythonic 的写法。
4.  **性能分析**：时间复杂度和空间复杂度。
5.  **知识点补充**：解释容易被面试官追问的知识点。
6.  **改进版本**：给出推荐的工程级实现。
7.  **pytest**：提供完整测试代码。

如果某个知识点掌握得不够好，安排额外的小题，而不是直接进入下一个知识点。

## 训练规则

-   每天先做当天题目，不提前看答案。
-   可以查 Python 官方文档，但尽量独立完成。
-   不会的题目也先尝试，不要直接跳过。
-   每天完成后，评估是否达到进入下一天的标准。
-   Day 14 完成后，进行一次第一阶段综合能力评估。

