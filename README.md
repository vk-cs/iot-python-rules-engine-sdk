CoIIoT SDK
==========

This package includes classes and functions for writing business rules in `Python 3` for `VK IoT Platform`.
Using coiiot_sdk in the development environment improves the convenience of writing rules through autocompletion and type hints.

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
