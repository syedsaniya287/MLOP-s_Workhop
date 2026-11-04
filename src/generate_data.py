
import os
import numpy as np
import pandas as pd

def generate_student_data(records=1000):
    np.random.seed(42)

    study_hours = np.random.uniform(1, 10, records)
    attendance = np.random.uniform(50, 100, records)
    previous_marks = np.random.uniform(30, 100, records)
    assignment_score = np.random.uniform(30, 100, records)

    noise = np.random.normal(0, 5, records)

    final_score = (
        study_hours * 2.5
        + attendance * 0.20
        + previous_marks * 0.30
        + assignment_score * 0.15
        + noise
    )

    final_score = np.clip(final_score, 0, 100)

    df = pd.DataFrame({
        "study_hours": study_hours.round(2),
        "attendance": attendance.round(2),
        "previous_marks": previous_marks.round(2),
        "assignment_score": assignment_score.round(2),
        "final_score": final_score.round(2)
    })

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/students.csv", index=False)

    print("Student dataset generated successfully!")
    print("Total records:", len(df))
    print(df.head())

if __name__ == "__main__":
    generate_student_data()
