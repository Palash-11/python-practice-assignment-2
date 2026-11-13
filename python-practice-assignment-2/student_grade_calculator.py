name = input("student name: ")

subject1 = float(input("subject 1: "))
subject2 = float(input("subject 2: "))
subject3 = float(input("subject 3: "))

total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3

if 80 <= average_marks <= 100:
    grade = "A+"
elif 70 <= average_marks <= 79:
    grade = "A"
elif 60 <= average_marks <= 69:
    grade = "B"
elif 50 <= average_marks <= 59:
    grade = "C"
else:
    grade = "F"

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")