# complete example of dictionary
def all_student_info(dictionary):
    print("\n\tStudent Info")
    for n, g in dictionary.items():
        print("\nStudent Name: ", n)
        print("Student Gpa: ", g)


student_info = {}

while True:
    student_name = input("Enter your Name: ")
    student_gpa = float(input("Enter your Gpa: "))

    student_info[student_name] = student_gpa

    check_flag = input("Do You want to add more student info y/n: ")

    if check_flag == 'y':
        continue
    else:
        break

# calling function to print all values of dictionary
all_student_info(student_info)
