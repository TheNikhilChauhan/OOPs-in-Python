# online course management system

class OnlineCourse:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []

    def enroll_students(self, student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in the {self.course} course.")

    def course_details(self):
        print(f"Courses: {self.course}")
        print(f"Instructor Name: {self.instructor}")
        print(f"Enrolled Students: ")
        for student in self.students:
            print(student.name)

    def completed_course(self, name):
        for student in self.students:
            if student.name in name:
                self.students.remove(student)
            print(f"{name} has completed the course!")
        else:
            print(f"{name} is not enrolled in this course")
    
    def avg_grade(self, grades):
        total = sum(student.grades)
        average = total / len(student.grades)
        print(f"The average grade is: {round(average, 1)}")



class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

# 
course_input = input("Enter a course: ").lower()
name = input("Enter the Instructor: ").lower()
# student = input("Enter a name: ").lower()

course = OnlineCourse(course_input, name )
grades = [90, 94, 86, 45, 70]

# 
# course.avg_grade(grades)
# course.enroll_students(student)
# course.course_details()
# course.completed_course(student)

num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    student_name = input("Enter a student name: ").lower()
    grades = []
    for _ in range(3):
        grade = int(input("Enter a grade: "))
        grades.append(grade)
    student = Student(student_name, grades)
    course.enroll_students(student)
    course.avg_grade(student)
course.course_details()