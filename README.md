Виджет банковских операций клиента

Учебный проект: набор функций для обработки и отображения данных о банковских
операциях клиента (карты, счета, список транзакций).

Возможности

- Маскировка номеров карт и счетов (`src/masks.py`).
- Формирование строки с типом карты/счёта и её замаскированным номером,
  а также конвертация даты из ISO-формата (`src/widget.py`).
- Фильтрация и сортировка списка операций (`src/processing.py`).

Установка

Проект использует [Poetry](https://python-poetry.org/) для управления
зависимостями.

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

Использование

Маскировка карт и счетов

```python
from src.widget import mask_account_card, get_date

mask_account_card("Visa Platinum 7000792289606361")
mask_account_card("Счет 73654108430135874305")
get_date("2024-03-11T02:26:18.671407")
```

Фильтрация операций по статусу

```python
from src.processing import filter_by_state

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

filter_by_state(operations)
filter_by_state(operations, "CANCELED")
```

Сортировка операций по дате

```python
from src.processing import sort_by_date

sort_by_date(operations)
sort_by_date(operations, reverse=False)
```

Линтеры

В проекте настроены `flake8`, `mypy`, `black` и `isort`:

```bash
poetry run flake8 src
poetry run mypy src
poetry run isort src
poetry run black src
```
