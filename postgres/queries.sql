-- Q1: Усі користувачі
SELECT id, fullname, email
FROM users
ORDER BY id;

-- Q2: Усі завдання з іменем користувача та назвою статусу
SELECT
    t.id,
    t.title,
    t.description,
    s.name    AS status,
    u.fullname AS owner
FROM tasks t
LEFT JOIN status s ON s.id = t.status_id
LEFT JOIN users  u ON u.id = t.user_id
ORDER BY t.id;

-- Q3: Завдання зі статусом 'new'
SELECT
    t.id,
    t.title,
    u.fullname AS owner
FROM tasks t
JOIN status s ON s.id = t.status_id
JOIN users  u ON u.id = t.user_id
WHERE s.name = 'new'
ORDER BY t.id;
