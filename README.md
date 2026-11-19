# Student Performance Analysis

## Overview

This project was created to explore and learn **Python** by building a practical data analysis application. The software is a **Student Performance Analysis** tool that allows users to:

- Load and explore student mathematics records from a CSV dataset
- Calculate the average, highest, and lowest final grades
- Identify the number of students who passed or failed
- Compare students' study time with their academic performance
- Examine the relationship between student absences and final grades
- Generate charts to display student performance and grade progression

The purpose of this project was to practice **Python programming, data handling, data analysis, and data visualization** while working with a real-world educational dataset.

The project helped me understand how to use Python libraries to load, organize, analyze, and present data. I also learned how to create visual charts that make it easier to understand student performance and identify patterns in the data.

## Software Demo Video

[Software Demo Video](INSERT_YOUR_YOUTUBE_LINK_HERE)



## Development Environment

- **Visual Studio Code** – code editor used for development
- **Python 3** – programming language used to build the project
- **Pandas** – used for loading and analyzing the student dataset
- **NumPy** – used for numerical operations
- **Matplotlib** – used for creating data visualizations
- **CSV Dataset** – contains student mathematics records

The project uses Python libraries to perform data analysis and generate charts.

---

## Features

- **Data Loading** – Reads student mathematics records from the CSV dataset.
- **Summary Statistics** – Calculates the number of students and their average, highest, and lowest final grades.
- **Pass and Fail Analysis** – Counts students who passed or failed using 10/20 as the pass mark.
- **Study Time Analysis** – Compares average final grades across different study-time categories.
- **Absence Analysis** – Examines the relationship between student absences and final grades.
- **Grade Progression** – Compares average grades across G1, G2, and G3.
- **Data Visualization** – Generates four charts to make the results easier to understand.

---

## Useful Websites

- [Python Official Documentation](https://docs.python.org/3/) – Reference for Python programming.
- [Pandas Documentation](https://pandas.pydata.org/docs/) – Learning how to load and analyze datasets.
- [NumPy Documentation](https://numpy.org/doc/) – Reference for numerical operations.
- [Matplotlib Documentation](https://matplotlib.org/stable/) – Learning how to create charts and graphs.
- [Stack Overflow](https://stackoverflow.com/) – Finding solutions to programming problems and errors.

---

## Future Work

Future improvements for the Student Performance Analysis project include:

- Add more student performance indicators for deeper analysis.
- Allow users to load different student datasets.
- Include more charts to explore other factors affecting academic performance.
- Add filters to analyze students based on different categories.
- Develop a simple web interface to make the application easier to use.
- Improve the analysis by adding more statistical methods.

---

## How to Run

1. Clone the GitHub repository.
2. Open the project folder in Visual Studio Code or PowerShell.
3. Create a Python virtual environment:

   `py -m venv .venv`

4. Activate the virtual environment:

   `.\.venv\Scripts\Activate.ps1`

5. Install the required packages:

   `python -m pip install -r requirements.txt`

6. Make sure the dataset is available in the `data` folder as `student-mat.csv`.

7. Run the data analysis:

   `python .\src\analysis.py`

8. Generate and display the charts:

   `python .\src\visualization.py`

The charts will be saved in the `charts` folder.

---