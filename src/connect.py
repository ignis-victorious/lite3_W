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


def add_project(conn, project) -> int | None:
    # insert table statement
    sql: str = """ INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) """

    # Create  a cursor
    cur: Cursor = conn.cursor()

    # execute the INSERT statement
    cur.execute(sql, project)

    # commit the changes
    conn.commit()

    # get the id of the last inserted row
    return cur.lastrowid


def add_task(conn, task) -> int | None:
    # insert table statement
    sql: str = """INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
             VALUES(?,?,?,?,?,?) """

    # create a cursor
    cur: Cursor = conn.cursor()

    # execute the INSERT statement
    cur.execute(sql, task)

    # commit the changes
    conn.commit()

    # get the id of the last inserted row
    return cur.lastrowid


def main():

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

            # add  a project
            project_one: tuple[str, str, str] = ("Cool App with SQLite & Python", "2015-01-01", "2015-01-30")
            project_id: int | None = add_project(conn=conn, project=project_one)
            print(f"Created a project with the id {project_id}")

            # add tasks to the project
            tasks: list[tuple[str, int, int, int | None, str, str]] = [
                ("Analyze the requirements of the app", 1, 1, project_id, "2015-01-01", "2015-01-02"),
                ("Confirm with user about the top requirements", 1, 1, project_id, "2015-01-03", "2015-01-05"),
            ]

            for task in tasks:
                task_id: int | None = add_task(conn=conn, task=task)
                print(f"Created task with the id {task_id}")

    except sqlite3.OperationalError as e:
        print(f"Database error: {e}", e)
        # print("Failed to open database:", e)


if __name__ == "__main__":
    main()
