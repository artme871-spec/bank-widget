# Финансовый виджет (bank-widget)

Учебный проект: набор функций для обработки, фильтрации и отображения данных о банковских операциях клиента (карты, счета, список транзакций).

## Возможности и структура проекта

* **Маскировка карт и счетов (`src/masks.py`)** — маскирование номеров карт и банковских счетов для безопасного отображения.
* **Расширенная маскировка и обработка дат (`src/widget.py`)** — формирование строки с типом карты/счёта и её замаскированным номером, а также конвертация даты из ISO-формата.
* **Фильтрация и сортировка (`src/processing.py`)** — сортировка транзакций по дате и фильтрация по статусу выполнения.
* **Генераторы данных (`src/generators.py`)** — функции-генераторы для эффективной и ленивой обработки больших объемов данных (фильтрация по валюте, поочередное извлечение описаний, генерация номеров карт в диапазоне).
* **Декораторы логирования (`src/decorators.py`)** — декоратор `log` для автоматической регистрации деталей выполнения функций, их результатов и перехвата ошибок.

---

## Установка

Проект использует Poetry для управления зависимостями.
```bash
git clone <ссылка-на-репозиторий>
cd <название-проекта>
poetry install
```

Либо через `pip` и `requirements.txt`:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Использование и примеры

### 1. Маскировка карт и счетов
```python
from src.widget import mask_account_card, get_date

print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
print(mask_account_card("Счет 73654108430135874305"))      # Счет **4305
print(get_date("2024-03-11T02:26:18.671407"))               # 11.03.2024
```

### 2. Фильтрация и сортировка операций
```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

filtered = filter_by_state(operations, "EXECUTED")
sorted_ops = sort_by_date(operations, reverse=True)
```

### 3. Работа с генераторами большого объема данных
```python
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Фильтрация транзакций по валюте (возвращает итератор)
usd_transactions = filter_by_currency(operations, "USD")

# Извлечение описаний операций по очереди
descriptions = transaction_descriptions(operations)

# Генерация номеров банковских карт в заданном диапазоне
for card_number in card_number_generator(1, 5):
    print(card_number)  # 0000 0000 0000 0001 ...
```

### 4. Логирование функций с помощью декоратора `log`
Декоратор автоматически фиксирует успешное выполнение функции или возникшую ошибку (включая её тип и входные параметры).
```python
from src.decorators import log

# Логирование вывода в консоль
@log()
def my_func(x, y):
    return x + y

# Логирование в локальный файл
@log(filename="function_logs.txt")
def my_error_func(x, y):
    return x / y  # При y=0 запишет ошибку ZeroDivisionError и входные данные
```

---

## Линтеры и форматирование кода

В проекте настроены утилиты `flake8`, `mypy`, `black` и `isort` для проверки соответствия стандартам PEP 8:
```bash
poetry run flake8 src
poetry run mypy src
poetry run isort src
poetry run black src
```

---

## Тестирование и покрытие (Code Coverage)

Проект полностью покрыт модульными тестами с использованием `pytest`. Тесты лежат в директории `tests/` и изолированы по модулям (`test_masks.py`, `test_widget.py`, `test_processing.py`, `test_generators.py`, `test_decorators.py`). Общие фикстуры вынесены в `tests/conftest.py`.

Для перехвата и тестирования вывода в консоль в декораторах применяется встроенная фикстура `capsys`.

**Запуск тестов:**
```bash
poetry install --with dev
poetry run pytest
```

По умолчанию `pytest` запускается с автоматическим измерением покрытия кода модуля `src` и формирует:
1. Отчет о покрытии прямо в терминале (`--cov-report=term-missing`).
2. HTML-отчет о покрытии в папке `htmlcov/` (`--cov-report=html`). Открыть его можно через браузер: `htmlcov/index.html`.

Порог покрытия жестко зафиксирован на уровне **80%** (`fail_under = 80` в конфигурации `pyproject.toml`). Если покрытие опустится ниже этой планки, тесты завершатся с ошибкой.
