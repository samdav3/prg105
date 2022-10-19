

def main():
    file = open('grades.txt', 'a')
    num = int(input("How many students do you need ot enter grades for? "))
    class_values = []
    for num in range(num):
        names = input(f'Enter the name of the student: ')
        grades = input("Enter the student's final grade: ")
        class_values.append([names, grades])
    file.write(str(class_values))
    print(class_values)
    file.close()


main()
