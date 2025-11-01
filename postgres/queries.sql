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

-- Q4: Порахувати кількість завдань у кожного користувача
SELECT
    u.fullname AS user_name,
    COUNT(t.id) AS total_tasks
FROM users u
LEFT JOIN tasks t ON t.user_id = u.id
GROUP BY u.fullname
ORDER BY total_tasks DESC;

-- Q5: Користувачі, які не мають завдань
SELECT
    u.id,
    u.fullname,
    u.email
FROM users u
LEFT JOIN tasks t ON t.user_id = u.id
WHERE t.id IS NULL;

-- Q6: Завдання з певним статусом (приклад: 'completed')
SELECT
    t.id,
    t.title,
    s.name AS status,
    u.fullname AS owner
FROM tasks t
JOIN status s ON s.id = t.status_id
JOIN users  u ON u.id = t.user_id
WHERE s.name = 'completed'
ORDER BY t.id;

-- Q7: Завдання певного користувача (приклад: email)
SELECT
    t.id,
    t.title,
    s.name AS status
FROM tasks t
JOIN users  u ON u.id = t.user_id
JOIN status s ON s.id = t.status_id
WHERE u.email = 'example@example.com';
