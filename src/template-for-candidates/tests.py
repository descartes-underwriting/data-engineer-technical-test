from utils import database_operation, load_statements
import sqlite3

# Do not edit


@database_operation
@load_statements("tests/check_tables.sql")
def check_tables(
    check_tables: str,
    cursor: sqlite3.Cursor,
) -> None:
    try:
        cursor.executescript(check_tables)
    except:
        print(
            "\nFAIL: At least one of the following table is missing: `earthquakes`, `locations`, `losses`\n"
        )
        raise
    else:
        print("PASS: Found the expected tables")


@database_operation
@load_statements("tests/check_locations.sql")
def check_locations(check_locations: str, cursor: sqlite3.Cursor) -> None:
    try:
        cursor.execute(check_locations)
        locations = sorted([location for location in cursor])
        expected_locations = [
            ("California Dreamin'",),
            ("Californification",),
            ("Hotel California",),
        ]
        assert locations == expected_locations
    except:
        print(
            "\nFAIL: Failed to read the expected locations from the `locations` table"
        )
        if locations is not None:
            print(f"Expected: {expected_locations}")
            print(f"Found: {locations}")
        print("\n")
        raise
    else:
        print("PASS: Found all expected locations")


@database_operation
@load_statements("tests/check_earthquakes.sql")
def check_earthquakes(check_earthquakes: str, cursor: sqlite3.Cursor) -> None:
    # NOTE: We test for a subset of "interesting" earthquakes.
    # Given the area of interest and the time range, the API
    # will return are a lot more than 10 earthquakes, but these
    # 10 should be in the list
    try:
        cursor.execute(check_earthquakes)
        earthquakes_found = len([v for v in cursor])
        assert earthquakes_found == 10
    except:
        if earthquakes_found is not None:
            print(
                "\nFAIL: Found {earthquakes_found} out of 10. Some of the following earthquakes are missing:"
            )
            print(
                "('ci1053635', 'ci2021449', 'ci3141273', 'ci3144585', 'ci3149646', 'ci3347678', 'ci3359741', 'ci3360245', 'ci3360255', 'ci731691')"
            )
            print("\n")
        raise
    else:
        print("PASS: Found the expected earthquakes")
