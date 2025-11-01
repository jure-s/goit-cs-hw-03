# goit-cs-hw-03

Домашнє завдання: PostgreSQL (DDL, DML, Faker) + MongoDB (PyMongo CRUD).

## Структура
- `postgres/` — SQL-схема, запити, seed.
- `mongo/` — PyMongo CRUD.
- `docker-compose.yml` — локальні Postgres і MongoDB (опційно).
- `requirements.txt` — залежності.

## Швидкий старт
```bash
# створити та активувати venv (приклад для Windows PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# (опціонально) підняти БД локально:
docker compose up -d
