class student:
    student_count=0
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
        student.student_count+=1
    def display_count(self):
        print('total students',student.student_count)
    def display_student(self):
        print("rollno",self.rollno)
        print("name",self.name)
        print("course",self.course)
stud1=student(10,"jack","mca")
stud1.display_student()
