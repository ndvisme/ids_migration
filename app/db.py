import psycopg2
from typing import List
from app.file_handler import OldToNewId


def update_app_instances(old_to_new_ids: List['OldToNewId']):
    import os
    conn_params = {
        "dbname": os.getenv("DB_NAME", "sightd"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "password"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", 5432))
    }

    try:
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cursor:
                for mapping in old_to_new_ids:
                    cursor.execute(
                        """
                        UPDATE your_table_name
                        SET id = %s
                        WHERE id = %s
                        """,
                        (mapping.new, mapping.old)
                    )
                conn.commit()
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
