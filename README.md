CoIIoT SDK
==========

Данный пакет включает в себя тайпинги для написания бизнес правил на `Python 3.7` для `Mailru CoIIoT Platfrom`, а 
также утилиту командой строки для работы с HTTP API платформы.

## Installation

```bash
    pip install coiiot_sdk-0.0.1.tar.gz
```

## Usage

### Инициализируем проект
```bash
    coiiot-cli init --key "my-api-key" --addr "http://platform-addr"
```

### Создаём новое правило

Для создания нового правила необходимо выполнить команду

```bash
    coiiot-cli rules new test_rule
```

Команда создаст новое правило с именем `test_rule` из шаблона по умолчанию на файловой системе в папке `./rules` и
опубликует это правило в платформе (HTTP POST request).

### Сохраняем изменения

Для сохранения изменений в правиле необходимо выполнить команду
```bash
    coiiot-cli rules commit test_rule
```

Команда сохранит правило с именем `test_rule` из папки `./rules` в платформе (HTTP PATCH request).

### Получаем из платформы существующее правило

Для получения из платформы существующего правила необходимо выполнить команду
```bash
    coiiot-cli rules fetch test_rule
```

Команда вытянет из платформы правило с именем `test_rule` и поместит его в папку `./rules` (HTTP GET request)
