# Write a program that asks the user to enter five test scores. The program should display a
# letter grade



# o te the ele i union she placept ve test scores as arguments and return the.
# average of the scores (10 Marks)
# determine to te Thor unain should otein eatinese as an argument and returna
# Score
# 90-100
# 80-89
# 70-79
# 60-69
# Below 60
# Letter Grade
# LL


def calculateAverageGrade(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5
    average = total / 5

    # determine the letter grade bag
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade


# calculate the average grade for Sandra
sandra = calculateAverageGrade(85, 90, 78, 92, 88)
print(sandra)


