iDay 5 — Resilient Package API Client
60–90 分钟

今天开始实现一个可靠的 HTTP API Client，支持分页、异常处理、自动重试和依赖注入。

这次不使用 Django、FastAPI、Requests 或其他第三方 HTTP 库，只使用 Python 标准库和 pytest。
1. 场景说明
假设 App Store 提供一个 Package Metadata REST API：
GET /api/v1/packages?page=1&page_size=100


返回 JSON：
{
    "results": [
        {
            "name": "firefox",
            "version": "120.0",
            "architecture": "amd64",
            "channel": "stable"
        },
        {
            "name": "chromium",
            "version": "119.0",
            "architecture": "amd64",
            "channel": "beta"
        }
    ],
    "next_page": 2
}


最后一页：
{
    "results": [
        {
            "name": "vlc",
            "version": "3.0.20",
            "architecture": "arm64",
            "channel": "stable"
        }
    ],
    "next_page": null
}


但实际网络环境可能出现：
- 网络连接超时。
- 连接中断。
- HTTP 500、502、503 等服务器错误。
- HTTP 400、401、404 等客户端错误。
- API 返回的数据格式错误。
- 某一页请求失败，需要重试。
- 分页数据量很大，不能一次性加载。
你需要实现一个具备基本容错能力的 API Client。
2. 定义 Transport 接口
首先定义一个 Transport 类型：
from collections.abc import CallableTransport = Callable[    [str, str, dict[str, int]],    tuple[int, dict[str, object]],]



它表示一个可调用对象，参数依次是：
method: HTTP 方法，例如 GET
url: 请求地址
params: 查询参数


返回：
(status_code, response_data)


例如：
def mock_transport(method, url, params):    return (        200,        {            "results": [],            "next_page": None,        },    )



这里不要求你真正发送 HTTP 请求。Transport 负责模拟或封装底层 HTTP 通信。

这样设计的目的是练习 Dependency Injection（依赖注入）。
3. 定义异常类
实现以下异常：
class APIError(Exception):    passclass APIConnectionError(APIError):    passclass APIResponseError(APIError):    pass



异常用途：
异常	用途
APIError	API Client 基础异常
APIConnectionError	网络连接失败、超时、重试耗尽
APIResponseError	HTTP 状态码错误、响应格式错误

你可以根据实际设计增加其他异常，但需要说明原因。
4. 实现 PackageAPIClient
实现以下类：
class PackageAPIClient:    def __init__(        self,        base_url: str,        transport: Transport,        max_retries: int = 2,        retry_delay: float = 0.1,    ):        ...    def iter_packages(        self,        page_size: int = 100,    ) -> Iterator[dict[str, object]]:        ...



Task 1：初始化和参数验证
要求：
- base_url 必须是非空字符串。
- transport 必须是可调用对象。
- max_retries 必须是非负整数，拒绝 bool。
- retry_delay 必须是非负数，拒绝 bool。
- page_size 必须是正整数，拒绝 bool。
非法参数应该抛出合适的异常。
Task 2：实现分页请求
API 地址：
{base_url}/api/v1/packages


请求参数：
{    "page": 1,    "page_size": 100,}



要求：
1. 从 page=1 开始。
2. 使用 Transport 发送 GET 请求。
3. 解析返回的 HTTP 状态码和 JSON 数据。
4. 提取 results。
5. 逐条 yield package。
6. 根据 next_page 判断是否继续请求。
7. next_page=None 表示最后一页。
重要：必须使用 Generator 实现分页，不能一次性把所有页的数据保存到 List 中。
Task 3：实现重试机制
当请求失败时，支持自动重试。

以下情况可以重试：
错误	是否重试
TimeoutError	是
ConnectionError	是
HTTP 500	是
HTTP 502	是
HTTP 503	是
HTTP 400	否
HTTP 401	否
HTTP 404	否

要求：
- max_retries=2 表示首次请求失败后最多再尝试两次。
- 超过重试次数后，抛出异常。
- 不可重试的 HTTP 4xx 错误直接抛出异常。
- 使用 Exponential Backoff。
重试延迟计算方式：
\[
delay = retry\_delay \times 2^{retry\_count}
\]

例如 retry_delay=0.1：
请求次数	等待时间
第一次重试前	0.1 秒
第二次重试前	0.2 秒
第三次重试前	0.4 秒

提示：这里的 retry_count 从 0 开始。
Task 4：响应数据验证
HTTP 请求成功不代表 API 数据一定合法。

例如下面这些响应都应该被认为是无效响应：
{}



{    "results": "not a list",    "next_page": None,}



{    "results": [],}



要求：
- Response 必须是 Dictionary。
- 必须包含 results。
- results 必须是 List。
- next_page 必须存在。
- next_page 必须是正整数或 None。
- 拒绝 bool 作为 page number。
- next_page 不允许小于或等于当前 page，避免无限分页循环。
对于不合法的响应，抛出 APIResponseError。
5. 额外设计要求
为了让测试更容易编写，你需要考虑以下设计：

A. 不要直接调用 requests.get()

Transport 应该由外部传入。

B. 不要在测试中真正等待

建议考虑把 time.sleep() 也设计成可注入依赖，或者通过 unittest.mock.patch 替换。

例如：
from unittest.mock import patchwith patch("package_client.time.sleep") as mock_sleep:    ...



C. 尽量拆分私有方法

建议考虑：
def _request_page(self, page: int, page_size: int):    ...def _validate_response(self, response, page: int):    ...



但具体如何拆分，由你自己决定。
6. pytest 测试要求
文件结构：
day5/
├── package_client.py
└── test_package_client.py


至少覆盖以下测试：
测试场景	预期结果
单页请求	正确返回 package
多页请求	正确获取所有页面
最后一页 next_page=None	正常结束
TimeoutError	自动重试
ConnectionError	自动重试
HTTP 500	自动重试
HTTP 503	自动重试
HTTP 400	不重试
超过 max_retries	抛出异常
results 不存在	抛出 APIResponseError
results 不是 List	抛出 APIResponseError
next_page 不存在	抛出 APIResponseError
next_page 为 bool	抛出 APIResponseError
next_page 小于当前页	抛出 APIResponseError
Generator 惰性行为	不提前请求所有页面
sleep 调用	延迟符合 Exponential Backoff

建议使用 unittest.mock.Mock、call 和 patch。
7. 实现提示
不要把所有逻辑写进 iter_packages()。

建议采用这样的职责划分：
PackageAPIClient
iter_packages()

负责分页控制、逐条 yield package


_request_page()

负责请求、重试和异常处理


Transport

负责底层 HTTP 通信，由外部注入


_validate_response()

独立验证 API 返回的数据结构

8. 技术知识点
知识点	重点
Callable / Type Alias	定义函数接口
Dependency Injection	依赖注入
Generator	分页惰性读取
Exception Chaining	异常链
Retry Mechanism	自动重试
Exponential Backoff	指数退避
Mock / patch	模拟外部依赖
API Validation	响应数据验证
Separation of Concerns	职责分离

9. 完成检查清单
Day 5 Progress
0%



0 / 10 completed
[ ] 定义 Transport 类型和异常类
[ ] 实现 PackageAPIClient 初始化及参数验证
[ ] 实现单页请求
[ ] 实现多页 Generator
[ ] 实现 TimeoutError / ConnectionError 重试
[ ] 实现 HTTP 5xx 重试和 4xx 快速失败
[ ] 实现 Exponential Backoff
[ ] 实现 API Response Validation
[ ] 使用 Mock / patch 编写 pytest
[ ] 验证分页惰性行为


今天的练习建议：

先独立完成 PackageAPIClient，不要急着写全部测试。先用一个简单的 mock_transport() 验证单页和多页逻辑，再实现重试，最后补齐 pytest。

这道题比 Day 4 难度明显高一些，尤其是重试和 Generator 分页。遇到问题可以分阶段提交代码，我会逐段进行 Code Review，不会一开始就直接给你完整答案。

