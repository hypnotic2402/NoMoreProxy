from database import *
import csv

newclg = College("trial2")

#list of courses
rows = []
with open("./Data/courses.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

for i in rows:
    c = Course(i[0],i[1])
    newclg.add_course(c)

#list of courses
rows_students = []
with open("./Data/courses.csv", 'r') as file:
    csvreader = csv.reader(file)
    header_st = next(csvreader)
    for row in csvreader:
        rows_students.append(row)

x = header_st.size()
newclg.create_student(x - 3)

for i in rows_students:
    s = Student(i[0],i[1],i[2])

    for j in range(3,x-2):
        c = newclg.getcourse(i[j])
        s.add_course(c)
    
    newclg.add_students(s)

for i in rows:
    c = newclg.getcourse(i[0])
    c.addstudents(x-3)

