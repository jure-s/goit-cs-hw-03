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

-- Q8: Усі завдання конкретного користувача за user_id
SELECT id, title, description
FROM tasks
WHERE user_id =  :user_id;

-- Q9: Завдання з певним статусом через ПІДЗАПИТ (напр. 'new')
SELECT id, title, description
FROM tasks
WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- Q10: Оновити статус конкретного завдання на 'in progress'
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = :task_id;

-- Q11: Користувачі без жодного завдання (NOT IN + підзапит)
SELECT id, fullname, email
FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- Q12: Додати нове завдання користувачу (INSERT)
INSERT INTO tasks (title, description, status_id, user_id)
VALUES (:title, :description, (SELECT id FROM status WHERE name = 'new'), :user_id);

-- Q13: Усі НЕ завершені завдання (статус ≠ 'completed')
SELECT t.id, t.title
FROM tasks t
WHERE t.status_id <> (SELECT id FROM status WHERE name = 'completed');

-- Q14: Видалити конкретне завдання за id
DELETE FROM tasks
WHERE id = :task_id;

-- Q15: Знайти користувачів за шаблоном email (LIKE)
SELECT id, fullname, email
FROM users
WHERE email LIKE '%@example.com';

-- Q16: Оновити ім’я користувача
UPDATE users
SET fullname = :new_fullname
WHERE id = :user_id;

-- Q17: Кількість завдань для КОЖНОГО статусу (GROUP BY)
SELECT s.name AS status, COUNT(t.id) AS total
FROM status s
LEFT JOIN tasks t ON t.status_id = s.id
GROUP BY s.name
ORDER BY s.name;

-- Q18: Завдання користувачів з певним доменом email (JOIN + LIKE)
SELECT t.id, t.title, u.email
FROM tasks t
JOIN users u ON u.id = t.user_id
WHERE u.email LIKE '%@example.com';

-- Q19: Список завдань без опису
SELECT id, title
FROM tasks
WHERE description IS NULL OR description = '';

-- Q20: Користувачі та їхні завдання у статусі 'in progress' (INNER JOIN)
SELECT u.fullname, t.id AS task_id, t.title
FROM users u
JOIN tasks t   ON t.user_id = u.id
JOIN status s  ON s.id = t.status_id
WHERE s.name = 'in progress';
