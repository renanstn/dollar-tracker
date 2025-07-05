create_table_query = """
    CREATE TABLE IF NOT EXISTS dollar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datehour TEXT NOT NULL,
        value INTEGER NOT NULL
    )
"""

insert_values_query = """
    INSERT INTO dollar (datehour, value)
    VALUES (?, ?)
"""
