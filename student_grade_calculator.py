name = input("Enter student name: ")

marks = []
for i in range(5):
    mark = float(input(f"Enter mark for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
