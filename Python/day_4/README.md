Day 4 — Robust JSONL Package Feed Parser


你需要开发一个 Package Feed Parser，负责从 JSONL（JSON Lines）数据流中读取软件包信息、验证数据、处理异常，并支持跳过无效记录。
1. 场景说明
假设 Snap Store 有一个软件包元数据导入服务，需要从外部数据源接收软件包信息。

数据源使用 JSONL 格式，每一行代表一个软件包：
{"name": "firefox", "version": "120.0", "architecture": "amd64", "channel": "stable"}
{"name": "chromium", "version": "119.0", "architecture": "amd64", "channel": "beta"}
{"name": "vlc", "version": "3.0.20", "architecture": "arm64", "channel": "stable"}


但实际数据可能存在问题：
- JSON 格式错误。
- 缺少必要字段。
- 字段类型错误，例如 version 是数字而不是字符串。
- 字段内容为空字符串。
- 某一行完全为空。
你的任务是实现一个可靠的 Parser。
2. 数据模型
使用 dataclass 定义软件包记录：
from dataclasses import dataclass@dataclass(frozen=True)class PackageRecord:    name: str    version: str    architecture: str    channel: str



要求：
1. 使用 frozen=True，对象创建后不能修改。
2. 所有字段必须是非空字符串。
3. 不允许缺少任何必要字段。
3. 需要实现的函数
Task 1：定义自定义异常
class PackageRecordError(ValueError):    pass



所有软件包记录的数据验证错误，都应该抛出 PackageRecordError。

Task 2：解析单条 JSON 记录
def parse_package_record(    raw: str,    line_number: int,) -> PackageRecord:    ...



要求：
1. 使用 json.loads() 解析 JSON。
2. 验证 JSON 格式是否合法。
3. 验证解析结果必须是 Dictionary。
4. 验证四个必要字段是否存在。
5. 验证所有字段都是字符串。
6. 验证所有字段不是空字符串。
7. 成功时返回 PackageRecord。
8. 失败时抛出 PackageRecordError，错误信息中必须包含 line_number。
例如：
raw = '{"name": "firefox", "version": "120.0", "architecture": "amd64", "channel": "stable"}'record = parse_package_record(raw, line_number=1)print(record)



预期结果：
PackageRecord(
    name='firefox',
    version='120.0',
    architecture='amd64',
    channel='stable'
)


Task 3：实现 JSONL 流式解析
from collections.abc import Iterable, Iteratordef iter_package_feed(    lines: Iterable[str],    *,    skip_invalid: bool = False,) -> Iterator[PackageRecord]:    ...



要求：
- 输入可以是 List、Tuple 或 Generator。
- 逐行解析，不允许一次性读取全部数据。
- 空行直接跳过。
- 使用 parse_package_record() 解析每一条记录。
- skip_invalid=False：遇到错误立即抛出异常。
- skip_invalid=True：遇到错误时记录 warning 日志，然后跳过该行，继续处理后面的记录。
- 保持原始数据顺序。
- 返回 Generator，不允许返回 List。
4. Logging 要求
使用 Python 标准库 logging。

当 skip_invalid=True 时，遇到无效数据需要输出 warning。

例如：
WARNING: Invalid package record at line 3: Missing required field 'version'


提示：
import logginglogger = logging.getLogger(__name__)logger.warning("Invalid package record at line %s: %s", line_number, error)



不要使用 print() 代替 logging。
5. 测试要求（pytest）
至少覆盖以下测试场景：
测试场景	预期结果
合法 JSON 记录	返回 PackageRecord
JSON 格式错误	抛出 PackageRecordError
JSON 解析结果不是 dict	抛出 PackageRecordError
缺少 name 字段	抛出 PackageRecordError
缺少 version 字段	抛出 PackageRecordError
字段类型为 int	抛出 PackageRecordError
字段为空字符串	抛出 PackageRecordError
空行	跳过
多条合法记录	全部正确返回
skip_invalid=False	第一条错误记录触发异常
skip_invalid=True	跳过错误记录，继续解析
输入为 Generator	正常处理
日志输出	能捕获 warning

特别注意：使用 pytest 的 caplog fixture 测试日志，不要通过检查终端输出判断日志是否正确。
6. 建议的项目结构
day4/
├── package_parser.py
└── test_package_parser.py


package_parser.py 放实现代码，test_package_parser.py 放测试代码。
7. 技术知识点
本次练习重点掌握：
知识点	需要掌握的内容
dataclass	数据模型、frozen
json.loads()	JSON 解析和异常处理
isinstance()	类型验证
Custom Exception	自定义异常和异常继承
Generator	yield 和惰性处理
logging	日志级别、logger
pytest	参数化测试、异常测试
caplog	测试日志输出

8. 额外挑战（选做）
如果你完成了基础要求，可以进一步考虑：
1. 是否应该拒绝 JSON 中的额外字段？
2. line_number 如果是负数或 bool，是否应该拒绝？
3. 如果 lines 中某个元素不是字符串，应该如何处理？
4. 如何让错误信息更容易用于线上问题排查？
5. 如果数据源有 100 万条记录，你的实现是否仍然能够保持较低的内存占用？

完成标准
Day 4 Checklist
0/8 completed

0%



[ ] PackageRecord dataclass 实现完成
[ ] PackageRecordError 自定义异常实现完成
[ ] parse_package_record() 实现完成
[ ] iter_package_feed() 实现完成
[ ] 支持 skip_invalid 两种模式
[ ] 使用 logging 输出 warning
[ ] pytest 覆盖主要正常和异常场景
[ ] 使用 Generator 验证惰性处理

本次先不要使用 Django、FastAPI、Pydantic 或数据库。 只使用 Python 标准库和 pytest。
