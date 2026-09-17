# Lab 3

import pandas as pd
import json

df = pd.read_csv("employees.csv")

result = {"departments": {}}

for department, group in df.groupby("Department"):
    employees = []

    for _, row in group.iterrows():
        employees.append({
            "id": int(row["EmpID"]),
            "name": row["Name"],
            "salary": int(row["Salary"])
        })

    result["departments"][department] = {
        "total_spend": int(group["Salary"].sum()),
        "employees": employees
    }

with open("departments.json", "w") as f:
    json.dump(result, f, indent=4)

print("Done")
