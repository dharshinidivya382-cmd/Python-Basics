import pandas as pd
data = {
    "Name": ["Arun", "Divya", "Kavi", "Rahul", "Priya"],
    "Python": [85, 92, 78, 88, 95],
    "Java": [80, 90, 75, 82, 91],
    "Maths": [88, 95, 80, 85, 93]
}

df = pd.DataFrame(data)

df["Total"] = df["Python"] + df["Java"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("Student Data")
print(df)

print("\nClass Average:")
print(df["Average"].mean())

print("\nTop Student:")
top_student = df.loc[df["Average"].idxmax()]
print(top_student["Name"])
