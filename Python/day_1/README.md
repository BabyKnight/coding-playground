# Problem 1

## 原始数据
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

## 任务 1：实现一个软件包查询函数

函数签名：

```python
def find_packages(packages, name=None, architecture=None, channel=None):
    pass


要求：

- 可以根据 name 筛选软件包
- 可以根据 architecture 筛选
- 可以根据 channel 筛选
- 所有筛选条件可以组合使用
- 如果所有条件都是 `None`，返回全部软件包
- 不要修改原始 packages 数据

## 任务 2：统计软件包数量

函数签名：
```python
def count_packages_by_architecture(packages):
    pass

期望输出：
```python
{
    "amd64": 4,
    "arm64": 1
}


## 任务 3：找出每个软件包的最新版本

函数签名：

```python
def get_latest_packages(packages):
    pass


要求：

- 按软件包名称分组，每个软件包只保留最新版本
- 版本为点分数字格式（如 `3.0.20`、`120.0`）
- 可选方案：使用 `packaging.version`，或者手写简易版本比较逻辑

## 任务 4：边界情况思考

- 输入空列表怎么办？
- 某个软件包没有 `architecture` 字段怎么办？
- 查询不存在的软件包怎么办？
- 版本号格式不正确怎么办？

