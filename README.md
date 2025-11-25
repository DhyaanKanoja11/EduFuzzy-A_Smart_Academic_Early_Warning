## Overview
**EduFuzzy** is an AI-powered academic analytics tool designed to evaluate student performance holistically. Unlike traditional grading systems that use rigid thresholds (e.g., "Below 75% attendance = Detained"), EduFuzzy uses **Fuzzy Logic** to handle uncertainty and edge cases. It also integrates **Linear Regression** for grade prediction and **K-Means Clustering** for unsupervised student grouping, providing a complete picture of academic risk.

## Features
*   **Fuzzy Risk Assessment:** Calculates a nuanced "Risk Score" (0-100%) based on Attendance and Internal Marks using a Fuzzy Inference System.
*   **Predictive Analytics:** Uses Linear Regression to forecast a student's "Final Exam Score" based on their current performance.
*   **Intelligent Grouping:** Automatically segments students into clusters (e.g., "High Achievers", "At-Risk") using K-Means Clustering.
*   **Automated Reporting:** Generates a detailed CSV report with risk status (Safe, Monitor, Critical).
*   **Visual Analytics:** Produces a bar chart visualizing the risk distribution across the class.
*   **Logic-Based Reasoning:** Includes a Prolog module (`edufuzzy.pl`) to demonstrate symbolic AI and rule-based inference for risk classification.


## Technologies & Tools Used
*   **Programming Language:** Python 3.13
*   **Logic Programming:** SWI-Prolog (for symbolic reasoning)
*   **Fuzzy Logic:** `scikit-fuzzy` (for defining membership functions and rules)
*   **Machine Learning:** `scikit-learn` (for Linear Regression and K-Means Clustering)
*   **Data Processing:** `pandas`, `numpy`
*   **Visualization:** `matplotlib`
*   **IDE:** VS Code

## Steps to Install & Run

### 1. Prerequisites
Ensure you have Python installed. You can check by running:
`python --version`

### 2. Clone/Download the Repository
Download the project folder to your local machine.

### 3. Install Dependencies
Navigate to the project directory in your terminal and run:
`pip install numpy pandas scikit-fuzzy matplotlib networkx scipy packaging scikit-learn`

### 4. Setup Data
Ensure a file named `students.csv` exists in the `data/` folder with the following structure:
| StudentID | Name | Attendance | InternalMarks |
| :---: | :---: | :---: | :---: |
| 101 | Alice | 85 | 42 |
| 102 | Bob | 60 | 25 |
| 103 | Charlie | 95 | 48 |
| 104 | David | 40 | 15 |
| 105 | Eve | 75 | 35 |

### 5. Run the Project
Execute the main script:
`python main.py`

### 6. Running the Prolog Module 
To test the logic-based version of the engine:
1.  Install [SWI-Prolog](https://www.swi-prolog.org/).
2.  Open the `prolog/edufuzzy.pl` file in SWI-Prolog.
3.  Run the query `report_all.` to see the classification of all students.

## Instructions for Testing
To verify the system works as expected, you can try these test cases by modifying the `data/students.csv` file:

*   **Test Case 1 (Safe Student):** Add a student with **95% Attendance** and **48 Marks**.
    *   *Expected Output:* Fuzzy Risk Score < 30, Status: "Safe".
*   **Test Case 2 (Critical Student):** Add a student with **40% Attendance** and **15 Marks**.
    *   *Expected Output:* Fuzzy Risk Score > 60, Status: "Critical".
*   **Test Case 3 (Borderline):** Add a student with **75% Attendance** and **35 Marks**.
    *   *Expected Output:* Fuzzy Risk Score approx 40-50, Status: "Monitor".

## Screenshots / Results
*(Note: These appear when you run the project)*

### 1. Console Output
The system prints a comprehensive table showing Fuzzy Risk, Predicted Scores, and Clusters:
Final Analysis (Fuzzy + Regression + Clustering):
<img width="809" height="159" alt="image" src="https://github.com/user-attachments/assets/596755d0-dc23-45dd-bc72-fdd41b7a47cb" />

### 2. Visualization Chart
A chart named `risk_analysis_chart.png` (or pop-up window) displays the risk score for each student against the critical threshold.
<img width="1000" height="703" alt="image" src="https://github.com/user-attachments/assets/15575245-06d9-40b4-8a3d-f1cfcd09a502" />

## "Comprehensive Git History is Mentioned in the Project Report"

## References

1. Zadeh, L. A. (1965). *Fuzzy Sets*. Information and Control, 8(3), 338-353.

2. Scikit-Fuzzy Documentation. Retrieved from https://pythonhosted.org/scikit-fuzzy/

3. Scikit-Learn: Machine Learning in Python. Retrieved from https://scikit-learn.org/stable/

4. MacQueen, J. (1967). *Some Methods for Classification and Analysis of Multivariate Observations*. Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics.

5. Pandas Documentation. Retrieved from https://pandas.pydata.org/docs/

6. Matplotlib: Visualization with Python. Retrieved from https://matplotlib.org/

7. NumPy Documentation. Retrieved from https://numpy.org/doc/

8. NetworkX Documentation. Retrieved from https://networkx.org/
