
# 
#   Import LIBRARIES
import sqlite3
#   Import FILES
#  ______________________
# 



try:
    with sqlite3.connect(database= "data/my.db") as conn:
        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
        # interact with database
        pass
except sqlite3.OperationalError as e:
    print("Failed to open database:", e)



# if __name__ == "__main__":

