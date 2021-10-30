import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="OverWatch",
  password="Error@404"
)

# if(mydb):
    # print("Hello")

if not (mydb): print("Error connecting")

mycur = mydb.cursor()

class Student:
    def __init__(self,roll_no,name,photograph):
        self.roll_no = roll_no
        self.name = name
        self.listofcourses = []
        self.photograph = photograph



    def add_course(self,course):
        self.listofcourses.append(course)

    def getroll(self):
        return self.roll_no

    def getname(self):
        return self.name

    def getlistofcourses(self):
        return self.listofcourses   

    def getphotograph(self):
        return self.photograph 

class Course:
    def __init__(self,course_id,course_name):
        self.course_id = course_id
        self.course_name = course_name
        mycur.execute("create table if not exists "+self.course_name +" (student_rno varchar(255),name varchar(255));")
        self.students = []

    def add_class(self,date):
        mycur.execute("Alter table "+ self.course_name+" add " + date + " varchar(255) default '0';")


    def getcourseid(self):
        return self.course_id

    def getcoursename(self):
        return self.course_name

    def addstudents(self,noofcourses):
        s = ""
        for i in range(1,noofcourses+1):
            if(i == noofcourses):
                s = s+"course"+str(i)+" = '" + self.course_name + "'"
            else:
                s = s+"course"+str(i)+" = '" + self.course_name + "' OR"

        mycur.execute("Select roll_no from Students where ("+s+")")
        
        self.students = mycur.fetchall()

        for i in self.students:
            mycur.execute("Insert into "+ self.course_name+" values ('"+i+"');")
            mycur.commit()


    # get roll no from name of the student
    # add attendence functionality
    # add students
    # def markattendence(self):
    def markattendence(self,face,date,name):
        if(face):
            mycur.execute("update "+self.course_name+" set "+date+" = '1' where name = '"+name+"';")

            # mycur.commit()


class College:
    def __init__(self,college_name):
        mycur.execute("Create database if not exists "+college_name+";")
        mycur.execute("use "+college_name+";")
        self.courselist = []
        self.college_name = college_name

    def add_course(self,course):
        self.courselist.append(course);

    def getcourse(self,id): 
        for i in self.courselist:
            if(i.getcourseid() == id):
                return i

    def create_student(self,noofcourses):
        self.noofcourses = noofcourses
        s = "";
        for i in range(1,noofcourses+1):
            s = s+"course"+str(i)+" varchar(255),"

        mycur.execute("create table if not exists Students ( roll_no varchar(255),name varchar(255), "+s + "addressphoto varchar(255));")
        # print("create table if not exists Students ( roll_no varchar(255),name varchar(255), "+s + "addressphoto varchar(255));")    
    
    def add_students(self,s):
        c = ""
        for i in s.getlistofcourses():
            c = c + "'"+i.getcourseid() + "',"

        # print(s.getname())
        mycur.execute("insert into Students values ('"+s.getroll() + "','"+s.getname()+"',"+c+"'"+s.getphotograph()+"');")
        # mycur.commit()

    def getlist(self,course_name):
        for i in self.courselist:
            if(i.getcoursename() == course_name):
                c = i

        s = ""
        for i in range(1,self.noofcourses+1):
            if(i == self.noofcourses):
                s = s+"course"+str(i)+" = '" + c.getcourseid() + "'"
            else:
                s = s+"course"+str(i)+" = '" + c.getcourseid() + "' OR"

        mycur.execute("Select addressphoto from Students where ("+s+");")
        
        # print("Select addressphoto from Students where ("+s+");")
        
        addressphoto = mycur.fetchall()
        
        # print(addressphoto)
        mycur.execute("Select name from Students where ("+s+")")
    
        name = mycur.fetchall()
        return addressphoto,name

    
    def delete(self):
        mycur.execute("Drop database "+self.college_name)
        #mycur.commit()




# newclg = College("trial1")
# #newclg.delete()
# newclg.create_student(1)
# c1 = Course("CS101","c1")
# c2 = Course("CS102","c2")
# c3 = Course("CS103","c3")
# newclg.add_course(c1)
# newclg.add_course(c2)
# newclg.add_course(c3)


# #get course by course id
# s1 = Student("I1","mudizi","./modiji.jpg")
# c1p = newclg.getcourse("CS101")
# s1.add_course(c1p)
# newclg.add_students(s1)
# #s1.add_course(c2)
 
# s2 = Student("I2","pappu","./modiji.jpg")
# c2p = newclg.getcourse("CS102")
# s2.add_course(c2p)
# newclg.add_students(s2)

# s3 = Student("I3","kejri","./modiji.jpg")
# c1p = newclg.getcourse("CS101")
# s3.add_course(c1p)
# newclg.add_students(s3)

# c1.addstudents(1)
# c2.addstudents(1)
# c3.addstudents(1)
# c1.add_class("class21112020")
# a,b = newclg.getlist("c1")
# print(b)

# c1.markattendence(1,"class21112020","c1")