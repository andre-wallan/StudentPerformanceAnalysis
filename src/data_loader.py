
"""
Data Loader Module
Loads student mathematics records into Pandas.
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "student-mat.csv"


def load_student_data():
    """Load student records from the CSV dataset."""

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}\n"
            "Place student-mat.csv inside the data folder."
        )

    data = pd.read_csv(DATA_FILE, sep=";")

    required_columns = [
        "studytime", "absences", "G1", "G2", "G3"
    ]

    missing = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    print("Student dataset loaded successfully!")
    print(f"Total student records: {len(data)}")

    return data


if __name__ == "__main__":
    students = load_student_data()
    print(students.head())
