from my2darray import Array2D

gradeFile = open("gradefile.txt", "r")

#extract first two lines
numStudents = int(gradeFile.readline())
numExams = int(gradeFile.readline())
print numExams, numStudents
#create 2D array
examGrades = Array2D(numStudents, numExams)
i = 0
for student in gradeFile:
    grades = student.split()
    for j in range(numExams):
        examGrades[i,j] = int(grades[j])
    i += 1
gradeFile.close()

for i in range(numStudents):
    total = 0
    for j in range(numExams):
        total += examGrades[i,j]
    examAvg = total / numExams
    print("%2d: %6.2f" %(i+1, examAvg))
