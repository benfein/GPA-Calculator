numberOfCourses = 0
a = 4.0
aMinus = 3.7
bPlus = 3.3
b = 3.0
bMinus = 2.7
cPlus = 2.3
c = 2.0
cMinus = 1.7
dPlus = 1.3
d = 1.0
f = 0.0
grades = []
currentGPA = 0.00
tempNumber = input("How many courses are you taking?")
if (tempNumber.isnumeric()):
	numberOfCourses = tempNumber
else:
	print("Invalid Entry")
	quit()
for i in range(int(numberOfCourses)):
	currentGrade = input("Enter your grade for course " + str(i + 1))
	grades.append(currentGrade)
for i in grades:
		if(i == "A"):
			currentGPA = currentGPA + a
		elif(i == "A-"):
			currentGPA = currentGPA + aMinus
		elif(i == "B+"):
			currentGPA = currentGPA + bPlus
		elif(i == "B"):
			currentGPA = currentGPA + b
		elif(i == "B-"):
			currentGPA = currentGPA + bMinus
		elif(i == "C+"):
			currentGPA = currentGPA + cPlus
		elif(i == "C"):
			currentGPA = currentGPA + c
		elif(i == "C-"):
			currentGPA = currentGPA + cMinus
		elif(i == "D+"):
			currentGPA = currentGPA + dPlus
		elif(i == "D"):
			currentGPA = currentGPA + d
		elif(i == "F"):
			currentGPA = currentGPA + f
		else: 
			print("The grade entered is invalid")
			quit()
currentGPA = currentGPA / int(numberOfCourses)
print("Your GPA will be " + str(currentGPA))




