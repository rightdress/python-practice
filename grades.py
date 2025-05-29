# Store a list of student grades
grades = [88, 92, 76, 81, 95, 67, 73, 89, 100, 84]

# Calculate the average
average = sum(grades) / len(grades)

# Find the highest and lowest grades
highest = max(grades)
lowest = min(grades)

# Count how many students passed
passed = 0

for grade in grades:
  if grade >= 70:
    passed += 1

# Output
print("Student grades:" , grades)
print("Average grade:" , average)
print("Highest grade:" , highest)
print("Lowest grade:" , lowest)
print("Number of students who passed:", passed)
