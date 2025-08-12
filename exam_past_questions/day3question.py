# Write a program that asks the user to enter five test scores. The program should display a
# letter grade 


def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# getting input and displaying the grades
for count in range(5): # loop [1, 2, 3, 4, 5]
    score = float(input("Enter score for test {}: ".format(count + 1)))
    grade = determine_grade(score)
    print("Grade for test {}: {}".format(count + 1, grade))