from hope import *
from database import *

newclg = College("trial1")

# While running the code, for testing purposes, uncomment below line, run  the code, then comment the line and run again

# newclg.delete()



newclg.create_student(1)
c1 = Course("CS101","c1")
c2 = Course("CS102","c2")
c3 = Course("CS103","c3")
newclg.add_course(c1)
newclg.add_course(c2)
newclg.add_course(c3)


#get course by course id
s1 = Student("I1","mudizi","./sample_img/NarenderaModi.jpg")
c1p = newclg.getcourse("CS101")
s1.add_course(c1p)
newclg.add_students(s1)
#s1.add_course(c2)

s2 = Student("I2","pappu","./sample_img/Pappu.jpeg")
c2p = newclg.getcourse("CS102")
s2.add_course(c2p)
newclg.add_students(s2)

s3 = Student("I3","kejri","./sample_img/kejri.jpg")
c1p = newclg.getcourse("CS101")
s3.add_course(c1p)
newclg.add_students(s3)

c1.addstudents(1)
c2.addstudents(1)
c3.addstudents(1)
c1.add_class("class21112020")
a,b = newclg.getlist("c1")
# print(b)

# c1.markattendence(1,"class21112020","c1")

#attendance for c1

refList = []
for i in a:
    refList.append(i[0])

nameList = []
for i in b:
    nameList.append(i[0])

r = check_present(refList , "./test_images/k2.jpg" , nameList , "")

f = 0
if r != "-1":
    f = 1

c1.markattendence(f , "class21112020" , r)
print(r)






