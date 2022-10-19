

def main():
    grades = open('grades.txt', 'w')
    num = int(input("How many students do you need ot enter grades for? "))
    class_grades = []
    rows = num
    cols = 2
    for num in range(num):
        name = input(f'Enter the name of the student: ')
        grade = input("Enter the student's final grade: ")
        class_grades.append([name, grade])
        for name in range(rows):
            for grade in range(cols):
                values = ([name, grade])
        grades.write(values)
    grades.close()
    print(grades)


main()
