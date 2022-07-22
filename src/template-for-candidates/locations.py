from variables import INPUT_PATH
import tests


def read_locations(path: str) -> None:
    # Fill me ===>
    pass
    # <=== Stop


# Do not edit

if __name__ == "__main__":

    read_locations(INPUT_PATH / "locations.csv")

    tests.check_locations()
