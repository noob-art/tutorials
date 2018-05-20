#Name: Unufe Eloho, Phone_Number: 09092448203 Email_add: elohounufe@gmail.com

#Inputed data collected from the Teacher/ User
student_name1 = input("Enter Student Name: ")


# More than one test score is inputted
student_test_grade1 = int(input("Kindly Enter  First Test Score: "))
student_test_grade2= int(input("Kindly Enter Second Test Score: "))
student_test_grade3= int(input("Kindly Enter Third Test Score: "))
student_test_grade4= int(input("Kindly Enter Fourth Test Score: "))
student_test_grade5= int(input("Kindly Enter Fifth Test Score: "))

#More than one Homework recorded
student_homework1 = int(input("Kindly Enter First Homework Score: "))
student_homework2 = int(input("Kindly Enter Second Homework Score: "))
student_homework3 = int(input("Kindly Enter Third Homework Score: "))
student_homework4 = int(input("Kindly Enter Fourth Homework Score: "))
student_homework5 = int(input("Kindly Enter Fifth Homework Score: "))

#Exam score
student_Exam_grade = int(input("Kindly Enter Exam Score: "))

#Create a dictionary to put our Data
student = student_name1
student = {}
student["name"] = student_name1
student["test"] = [student_test_grade1, student_test_grade2, student_test_grade3]
student["homework"] = [student_homework1, student_homework2, student_homework3]
student["Exam"] = student_Exam_grade


# create an average function
def average(numbers):
	total = sum(numbers)
	total = float(total)
	return total / len(numbers)

# This function calculates the total score of the student
def get_total():
	homework = average(student["homework"])
	tests = average(student["test"])
	exam = student["Exam"]
	total = homework  + tests + exam
	return total

#This Function grades the total score
def letter_grade():
	get_total()
	if get_total() >= 90:
		return ("A")
	elif 90 > get_total() >=80:
		return("B")
	elif 80 > get_total() >= 70:
		return("C")
	elif 70 > get_total() >= 60:
		return("D")
	else:
		return ("F")

#Output showing students overall score and grade
print("{0}, scored {1}, his grade is {2}".format(student_name1, get_total(), letter_grade()))