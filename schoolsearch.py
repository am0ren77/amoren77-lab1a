# Ashley Moreno
# Lab 1 Part a
# schoolsearch.py

students = list()

# Function to read students.txt file and store student data
def read_students(filename):
    global students
    with open(filename, 'r') as file:
        for line in file:
	    data = line.strip().split(',')

	    student_info = [
		data[0],		# StLastName
		data[1],		# StFirstName
		int(data[2]),		# Grade
		int(data[3]),		# Classroom
		int(data[4]),		# Bus
		float(data[5]),		# GPA
		data[6],		# TLastName
		data[7]			# TFirstName
	    ]
	    students.append(student_info)

# R4. S[tudent]: <lastname>
def find_by_last_name(last_name):
    results = [student for student in students if student[0] == last_name]
    if results:
        for student in results:
	    print({
                    'last_name': student[0],
                    'first_name': student[1],
                    'grade': student[2],
                    'class_room': student[3],
                    'teacher': student[7] + " " + student[6]
                })
    else:
        print("No students found with last name: " + last_name)

# R5. S[tudent]: <lastname> B[us]
def find_by_last_name_bus(last_name):
    results = [student for student in students if student[0] == last_name]
    if results:
	for student in results:
	    print(student[0] + " " + student[1] + " - BUS ROUTE " + str(student[4]))
    else:
	print("No students found with last name: " + last_name)


# R6. T[eacher]: <lastname>
def find_by_tlast_name(tlast_name):
    results = [student for student in students if student[6] == tlast_name]
    if results:
	for student in results:
	    print(student[0] + " " + student[1])
    else:
	print("No students found for teacher with last name: " + tlast_name)

# R7. G[rade]: <Number>
def find_by_grade(grade):
    results = [student for student in students if student[2] == grade]
    if results:
        for student in results:
            print(student[0] + " " + student[1])   
    else:
        print("No students found in grade.")

# R8. B[us]: <Number>
def find_by_bus(bus_route):
    results = [student for student in students if student[4] == bus_route]
    if results:
        for student in results:
            print(student[0] + " " + student[1] + " " + str(student[2]) + " " + str(student[3]))
    else:
        print("No students found for bus route.")

# R9. G[rade]: <Number> H[igh] or G[rade]: <Number> L[ow]


# R10. A[verage]: <Number>


# R11. I[nfo]


def main():
    filename = "students.txt"
    read_students(filename)

    while True:
	command = input("Enter command: ").strip()
	
	if command.startswith('Q'):
            print("Quitting program.")
            break

	parts = command.split()
	main_command = parts[0]

	if command.startswith('S'):
	  if len(parts) > 1:
              last_name = parts[1]
	      if len(parts) > 2 and parts[2].startswith('B'):
                  find_by_last_name_bus(last_name) 
	      else:
		  find_by_last_name(last_name) 

	elif command.startswith('T'):
	  if len(parts) > 1:
                tlast_name = parts[1]
                find_by_tlast_name(tlast_name)	

	elif command.startswith('G'):
	  if len(parts) > 1:
		grade = int(parts[1])
		find_by_grade(grade)

	elif command.startswith('B'):
	  if len(parts) > 1:
		bus_route = int(parts[1])
		find_by_bus(bus_route)


if __name__ == "__main__":
    main()

