# Student Performance Analysis

A Python command-line project for exploring student mathematics grades,
study time, and absences. It reads the included CSV dataset, prints summary
statistics, and generates charts for grade distribution, study-time
performance, absences, and grade progression.

## Requirements

- Python 3
- Packages listed in `requirements.txt`

## Setup

From the project root in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

Run the analysis and charts separately:

```powershell
python .\src\analysis.py
python .\src\visualization.py
```

The dataset is expected at `data\student-mat.csv`. The loader checks for this
file and for the columns needed by the analysis.

The analysis reports the number of students, average/highest/lowest final
grades, pass and fail counts (using 10/20 as the pass mark), mean final grades
by study-time category, the absences/grade correlation, and averages for
grades G1, G2, and G3.

The visualization script saves four PNG files in `charts\`:

- `grade_distribution.png` — distribution of final grades (G3)
- `study_time_performance.png` — average G3 by study-time category
- `absences_performance.png` — absences compared with G3
- `grade_progression.png` — average grades across G1, G2, and G3

The charts are also displayed while the visualization script is running.

## Project layout

```text
data/       Student mathematics records
src/        Data loading, analysis, and visualization scripts
charts/     Generated chart images
```

## Assignment submission reminders

This README documents the software but does not replace any institution-
provided README template. If the assignment requires a specific template,
transfer this project information into that template. Video recording and
posting, public GitHub publication, the time log, the learning-strategies
discussion, and the Microsoft Teams video link must be completed and
submitted separately.
