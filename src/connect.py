#
#   Import LIBRARIES
import sqlite3
from sqlite3 import Cursor

#   Import FILES
#  ______________________
#

database: str = "src/data/my.db"
first_table: str = "first_table"

sql_statements: list[str] = [
    """CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY, 
            name text NOT NULL, 
            begin_date DATE, 
            end_date DATE
        );""",
    """CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            priority INT, 
            project_id INT NOT NULL, 
            status_id INT NOT NULL, 
            begin_date DATE NOT NULL, 
            end_date DATE NOT NULL, 
            FOREIGN KEY (project_id) REFERENCES projects (id)
        );""",
]


# create a database connection
try:
    with sqlite3.connect(database=database) as conn:
        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
        # interact with database
        cursor: Cursor = conn.cursor()

        # execute all statements to create tables (projects & tasks)
        for statement in sql_statements:
            cursor.execute(statement)  # cursor.execute(first_table)
        print("Tables created successfully.")

        # commit the changes
        conn.commit()
        # pass

except sqlite3.OperationalError as e:
    print(f"Database error: {e}", e)
    # print("Failed to open database:", e)


# if __name__ == "__main__":
