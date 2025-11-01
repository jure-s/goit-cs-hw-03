# goit-cs-hw-03  

## 📘 Завдання

Домашня робота складається з двох частин:

1. **PostgreSQL**
   - Створити базу даних `tasks_db` з таблицями:
     - `users` (id, fullname, email)
     - `status` (id, name)
     - `tasks` (id, title, description, status_id, user_id)
   - Використати зв’язки з `ON DELETE CASCADE`.
   - Наповнити базу тестовими даними за допомогою Faker (`seed.py`).
   - Реалізувати SQL-запити у `queries.sql`.

2. **MongoDB**
   - Створити базу `cat_db` з колекцією `cats`.
   - Реалізувати CRUD-операції у `mongo/main.py`:
     - додавання, перегляд, оновлення та видалення документів.

---

## Структура проєкту

```
goit-cs-hw-03/
├── postgres/
│   ├── schema.sql        # SQL-схема
│   ├── queries.sql       # Запити SELECT, JOIN, GROUP BY
│   ├── seed.py           # Faker-генератор даних
│   ├── .env.example
│   └── .env
│
├── mongo/
│   ├── main.py           # CRUD з PyMongo
│   ├── .env.example
│   └── .env
│
├── docker-compose.yml    # Контейнери PostgreSQL і MongoDB
├── requirements.txt
└── README.md
```

---

## Запуск проєкту локально

### 1️⃣ Запустити бази даних через Docker
```bash
docker compose up -d
```

### 2️⃣ Ініціалізувати схему PostgreSQL
```bash
docker cp .\postgres\schema.sql cs03-postgres:/tmp/schema.sql
docker exec -it cs03-postgres psql -U postgres -d tasks_db -f /tmp/schema.sql
```

### 3️⃣ Наповнити PostgreSQL даними
```bash
python postgres/seed.py
```

### 4️⃣ Виконати SQL-запити
Відкрити `postgres/queries.sql` і виконати запити по черзі в `psql` або будь-якому клієнті.

---

## MongoDB CRUD

```bash
python mongo/main.py
```

Очікуваний результат:
```
🧹 All cats deleted
✅ Cat added with id: ...
🔄 Cat 'Barsik' age updated to 4
🗑️ Cat 'Murka' deleted
```

---

## Залежності
```
faker
psycopg2-binary
pymongo
python-dotenv
```

Інсталяція:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Перевірено
- [x] PostgreSQL контейнер працює  
- [x] Схема створюється без помилок  
- [x] Faker заповнює дані  
- [x] SQL-запити виконуються  
- [x] MongoDB CRUD працює коректно  

---
