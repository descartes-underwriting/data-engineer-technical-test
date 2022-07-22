from pathlib import Path

from variables import OUTPUT_PATH, INPUT_PATH


def compute_payouts(
    path: str,
) -> None:
    # Fill me ===>
    pass
    # <=== Stop


def export_payouts(
    path: Path,
) -> None:
    # Fill me ===>
    pass
    # <=== Stop


def export_payout_per_event(
    path: Path,
) -> None:
    # Fill me ===>
    pass
    # <=== Stop


def export_payout_per_year(
    path: Path,
) -> None:
    # Fill me ===>
    pass
    # <=== Stop


# Do not edit

if __name__ == "__main__":
    compute_payouts(INPUT_PATH / "payout_structure.csv")

    export_payouts(OUTPUT_PATH / "payouts.csv")
    export_payout_per_event(OUTPUT_PATH / "payout_per_event.csv")
    export_payout_per_year(OUTPUT_PATH / "payout_per_year.csv")

    assert (OUTPUT_PATH / "payouts.csv").is_file()
    assert (OUTPUT_PATH / "payout_per_event.csv").is_file()
    assert (OUTPUT_PATH / "payout_per_year.csv").is_file()
