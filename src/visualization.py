
"""
Student Performance Visualization Module

Creates and saves charts from student mathematics records.
"""

from pathlib import Path
import matplotlib.pyplot as plt

from data_loader import load_student_data


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHARTS_DIR = PROJECT_ROOT / "charts"

# Create charts directory if it does not exist
CHARTS_DIR.mkdir(exist_ok=True)


def plot_grade_distribution(data):
    """Display the distribution of final student grades."""

    plt.figure(figsize=(10, 6))

    plt.hist(
        data["G3"],
        bins=range(0, 22),
        edgecolor="black",
        alpha=0.8
    )

    plt.title("Distribution of Student Final Grades")
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Number of Students")
    plt.xticks(range(0, 21))
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "grade_distribution.png", dpi=300)
    plt.show()
    plt.close()


def plot_study_time_performance(data):
    """Compare average grades across study-time categories."""

    study_averages = data.groupby("studytime")["G3"].mean()

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        study_averages.index.astype(str),
        study_averages.values,
        edgecolor="black",
        alpha=0.8
    )

    plt.title("Average Final Grade by Study Time")
    plt.xlabel("Study Time Category")
    plt.ylabel("Average Final Grade (G3)")
    plt.ylim(0, 20)
    plt.grid(axis="y", alpha=0.3)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.2,
            f"{height:.2f}",
            ha="center"
        )

    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "study_time_performance.png", dpi=300)
    plt.show()
    plt.close()


def plot_absences_performance(data):
    """Explore the relationship between absences and final grades."""

    plt.figure(figsize=(10, 6))

    plt.scatter(
        data["absences"],
        data["G3"],
        alpha=0.6,
        edgecolors="black"
    )

    correlation = data["absences"].corr(data["G3"])

    plt.title(
        f"Student Absences vs Final Grades "
        f"(Correlation: {correlation:.2f})"
    )
    plt.xlabel("Number of Absences")
    plt.ylabel("Final Grade (G3)")
    plt.ylim(-1, 21)
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "absences_performance.png", dpi=300)
    plt.show()
    plt.close()


def plot_grade_progression(data):
    """Compare average grades across three grading periods."""

    grades = ["G1", "G2", "G3"]
    averages = [data[grade].mean() for grade in grades]

    plt.figure(figsize=(10, 6))

    plt.plot(
        grades,
        averages,
        marker="o",
        linewidth=2,
        markersize=8
    )

    for grade, average in zip(grades, averages):
        plt.annotate(
            f"{average:.2f}",
            (grade, average),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center"
        )

    plt.title("Student Grade Progression")
    plt.xlabel("Grading Period")
    plt.ylabel("Average Grade")
    plt.ylim(0, 20)
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "grade_progression.png", dpi=300)
    plt.show()
    plt.close()


def main():
    """Load data and generate all visualizations."""

    print("Loading student data...")
    students = load_student_data()

    print("\nGenerating visualizations...")

    plot_grade_distribution(students)
    plot_study_time_performance(students)
    plot_absences_performance(students)
    plot_grade_progression(students)

    print("\nAll visualizations generated successfully!")
    print(f"Charts saved in: {CHARTS_DIR}")


if __name__ == "__main__":
    main()
