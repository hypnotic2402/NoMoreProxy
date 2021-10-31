from database import *
import csv

from hope import *

newclg = College("trial2")
# newclg.delete()
#list of courses
rows = []
with open("./Data/courses.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

# print(rows)


for i in rows:
    c = Course(i[0],i[1])
    newclg.add_course(c)

#list of courses
rows_students = []
with open("./Data/student.csv", 'r') as file:
    csvreader = csv.reader(file)
    header_st = next(csvreader)
    for row in csvreader:
        rows_students.append(row)

# print(rows_students)

x = len(header_st)
newclg.create_student(x - 3)

for i in rows_students:
    s = Student(i[0],i[1],i[2])

    for j in range(3,x):
        c = newclg.getcourse(i[j])
        s.add_course(c)

    
    newclg.add_students(s)

for i in rows:
    c = newclg.getcourse(i[0])
    # print(c.getcoursename())
    c.addstudents(x-3)


a,b = newclg.getlist("Python_Programming")
# print(a)
c = newclg.getcourse("ESS112")
c.add_class("class11102020")
#print(c.output())
refList = []
for i in a:
    refList.append(i[0])

nameList = []
for i in b:
    nameList.append(i[0])

r = check_present(refList , "./test_images/t1.jpg" , nameList , "")

f = 0
if r != "-1":
    f = 1

c.markattendence(f , "class11102020" , r)
print(r)