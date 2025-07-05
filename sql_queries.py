create_table_query_sqlite = """
    CREATE TABLE IF NOT EXISTS dollar (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        datehour    TEXT NOT NULL,
        value       INTEGER NOT NULL
    )
"""

create_table_query_postgres = """
    CREATE TABLE IF NOT EXISTS dollar (
        id          SERIAL PRIMARY KEY,
        datehour    TIMESTAMP NOT NULL,
        value       INTEGER NOT NULL
    )
"""

insert_values_query_sqlite = """
    INSERT INTO dollar (datehour, value)
    VALUES (?, ?)
"""

insert_values_query_postgres = """
    INSERT INTO dollar (datehour, value)
    VALUES (%s, %s)
"""
