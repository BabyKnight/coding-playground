# Python  - coding playground

> problems for 10 days

## Week 1

### Day 1：数据结构与 Python 基础

- list、dict、set、tuple
- list/dict comprehension
- sorted、lambda、key function
- `collections.Counter`、`collections.defaultdict`
- 字符串和 JSON 处理

✅ 练习：解析一批 Snap 软件包信息，按名称、版本、架构分组和排序。

### Day 2：函数、类和代码组织

- 函数参数、`*args`、`**kwargs`
- 类、继承、组合
- `dataclasses`
- Type Hints
- 模块与包的组织

✅ 练习：实现一个简单的 Package、Channel、Revision 数据模型。

### Day 3：文件、异常与日志

- `pathlib`、`json`、`csv`
- 自定义 Exception
- `try/except/finally`
- `logging`
- 上下文管理器

✅ 练习：读取软件包元数据文件，校验格式并生成错误日志。

### Day 4：迭代器、生成器和装饰器

- iterable / iterator
- `yield`、generator expression
- decorator
- context manager

✅ 练习：实现一个可以逐批读取大量软件包记录的生成器。

### Day 5：测试与代码质量

- pytest fixture、parametrize
- Mock
- 单元测试与边界条件
- PEP 8、类型检查

✅ 练习：为前四天的代码编写测试，覆盖异常和无效输入。

## Week 2

### Day 6：REST API

- FastAPI、HTTP 方法、状态码、请求验证、异常处理

✅ 练习：开发 Package 查询 API。

### Day 7：数据库

- SQLite / PostgreSQL、SQL、索引、事务、ORM

✅ 练习：设计 Package、Revision、Channel 三张表。

### Day 8：并发与异步

- threading、multiprocessing、asyncio、`async/await`

✅ 练习：并发获取多个软件包的元数据，并处理超时和失败。

### Day 9：性能与可靠性

- 缓存、分页、批量查询、重试、超时、幂等性

✅ 练习：优化一个存在重复数据库查询的 API。

### Day 10：综合项目

✅ 练习：把前面的练习整合成一个小型 Package Store Backend，包含 API、数据库、测试和日志。
