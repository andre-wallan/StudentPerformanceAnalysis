
"""
Student Performance Analysis Module

Performs exploratory data analysis on student mathematics records.
"""

from data_loader import load_student_data


def analyze_student_performance(data):
    """Analyze student grades, study time, and attendance."""

    print("\n" + "=" * 55)
    print("          STUDENT PERFORMANCE ANALYSIS")
    print("=" * 55)

    # 1. General performance statistics
    print("\n1. GENERAL PERFORMANCE")
    print("-" * 55)

    print(f"Total students: {len(data)}")
    print(f"Average final grade: {data['G3'].mean():.2f}/20")
    print(f"Highest final grade: {data['G3'].max()}/20")
    print(f"Lowest final grade: {data['G3'].min()}/20")

    # 2. Pass and fail analysis
    pass_mark = 10

    passed = (data["G3"] >= pass_mark).sum()
    failed = (data["G3"] < pass_mark).sum()

    print("\n2. PASS AND FAIL ANALYSIS")
    print("-" * 55)

    print(f"Students passed: {passed}")
    print(f"Students failed: {failed}")
    print(f"Pass rate: {(passed / len(data)) * 100:.2f}%")
    print(f"Fail rate: {(failed / len(data)) * 100:.2f}%")

    # 3. Study time analysis
    print("\n3. STUDY TIME ANALYSIS")
    print("-" * 55)

    study_analysis = data.groupby("studytime")["G3"].mean()

    for study_time, average_grade in study_analysis.items():
        print(
            f"Study time category {study_time}: "
            f"{average_grade:.2f}/20 average grade"
        )

    # 4. Attendance analysis
    print("\n4. ABSENCE ANALYSIS")
    print("-" * 55)

    correlation = data["absences"].corr(data["G3"])

    print(f"Absence-grade correlation: {correlation:.3f}")

    # 5. Grade progression
    print("\n5. GRADE PROGRESSION")
    print("-" * 55)

    for grade in ["G1", "G2", "G3"]:
        print(f"{grade} average: {data[grade].mean():.2f}/20")

    print("\n" + "=" * 55)
    print("          ANALYSIS COMPLETED")
    print("=" * 55)


def main():
    """Load student records and print the performance analysis."""
    students = load_student_data()
    analyze_student_performance(students)


if __name__ == "__main__":
    main()
