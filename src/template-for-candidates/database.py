from utils import database_operation, load_statements
import sqlite3
import tests


@database_operation
@load_statements("database/your_script.sql")
def create_tables(
    your_script: str,
    cursor: sqlite3.Cursor,
) -> None:
    # Fill me, e.g. cursor.execute(your_script) ===>
    pass
    # <=== Stop


# Do not edit

if __name__ == "__main__":
    create_tables()

    tests.check_tables()
