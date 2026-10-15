#1
# print("Welcome to DPLMS Student Registration System")

#2 
courses =["Python with AI/ML","JavaScript","Flutter","MERN Stack"]

#3
# for course in courses:
#   print(course)

#4 
Student_Name = input("Enter Student Name: ")
Email =input("Enter email address:")
Age=input("enter your age")
course=input("enter your course")

#5/#6
new={
    "name":Student_Name,
    "Email" :Email,
    "Age":Age,
    "course":course
    }
#print(new)

if course in courses: 
   status="Registration Successful!" 
else: 
  status ="Course Not Available"

#7
print("Name:",new["name"])
print("Email address:",new["Email"])
print("Age : ",new["Age"])
print("Course : ",new["course"])
print("status" ,status)

