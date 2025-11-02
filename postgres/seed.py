import psycopg2
from faker import Faker
import random
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path=".env")

# Connection params
db_params = {
    "host": os.getenv("PGHOST", "localhost"),
    "port": os.getenv("PGPORT", "5432"),
    "user": os.getenv("PGUSER", "postgres"),
    "password": os.getenv("PGPASSWORD", "postgres"),
    "dbname": os.getenv("PGDATABASE", "tasks_db"),
}

fake = Faker()

def seed_data():
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # Clear old data
        cur.execute("DELETE FROM tasks;")
        cur.execute("DELETE FROM users;")

        # Fetch statuses
        cur.execute("SELECT id, name FROM status;")
        statuses = [row for row in cur.fetchall()]

        # Create users
        for _ in range(10):
            fullname = fake.name()
            email = fake.unique.email()
            cur.execute(
                "INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id;",
                (fullname, email),
            )
            user_id = cur.fetchone()[0]

            # Create random tasks for each user
            for _ in range(random.randint(1, 5)):
                title = fake.sentence(nb_words=4)
                description = fake.text(max_nb_chars=100)
                status_id = random.choice(statuses)[0]

                cur.execute(
                    """
                    INSERT INTO tasks (title, description, status_id, user_id)
                    VALUES (%s, %s, %s, %s);
                    """,
                    (title, description, status_id, user_id),
                )

        conn.commit()
        print("✅ Database successfully seeded with fake data.")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        if conn:
            cur.close()
            conn.close()


if __name__ == "__main__":
    seed_data()
