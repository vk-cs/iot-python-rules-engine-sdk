CoIIoT SDK
==========

Данный пакет включает в себя тайпинги для написания бизнес правил на `Python 3` для `VK IoT Platform`.
Использование coiiot_sdk в среде разработки повышает удобство написания правил за счет автодополнения и анализа типов.

## Installation

```bash
    pip install coiiot_sdk-0.0.1.tar.gz
```

## Example

```python
from coiiot_sdk import user_logs, cron_context

logger = user_logs.get_logger()
ctx = cron_context.current()

logger.info(f'rule_name={ ctx.rule.name }')
logger.info(f'schedule_name={ ctx.schedule.name }')
```
