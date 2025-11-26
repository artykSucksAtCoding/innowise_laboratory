"""The Student Grade Analyzer"""

def display_interface() -> None:
    """Display the interface.

    Args:
        None.
    """

    print('---Student Grade Analyzer---')
    print('1. Add a new student')
    print('2. Add grades for a student')
    print('3. Generate a full report')
    print('4. Find the top student')
    print('5. Exit program')
    print('Enter your choice: ')


def add_student(students: list) -> None:
    """Add students to the list.

    Args:
        students (list): List of students.
    """

    while True:
        name:str = input("1. Enter student name: ")
        if is_number1(name):
            print("Invalid student name.")

        elif any(s['name'] == name for s in students):
            print('Student already exists.')

        else:
            student_dict: dict[str, list[int]] = {
                "name": name,
                "grades": []
            }
            students.append(student_dict)
            break


def add_grade(students: list) -> None:
    """Add grades to the list.
    Args:
        students (list): List of students.
    """

    s:str = input('Enter student name: ')

    if not students:
        print('No students entered.')
        return
    for student in students:
        if student['name'] == s:
            while True:
                grade = input("Enter a grade(or 'done' to finish): ")
                if grade == 'done':
                    break
                if not is_number(grade) :
                    print("Invalid grade. Please enter a whole number between 0 and 100.")
                elif is_number_in_range(grade):
                    student['grades'].append(int(grade))
                else:
                    print("Invalid grade. Please enter a whole number between 0 and 100.")

            return
    print('There is no such student.')


def make_report(students: list) -> None:
    """Makes a report of students' GPA.

    Args:
        students (list): List of students.
    """

    max_grade: float  = -1
    min_grade: float = 101
    total_grade: float = 0
    count: int = 0

    if not is_filled(students):
        return

    print("--Student Report --")

    for student in students:
        try:
            s: float = sum(student['grades'])
            gpa: float = s / len(student['grades'])
            max_grade = max(gpa, max_grade)
            min_grade = min(gpa, min_grade)
            total_grade += gpa
            count += 1

            print(f"{student['name']}'s average grade is {gpa}.")
        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A.")

    print('-'* 26)

    print(f"Max Average: {max_grade}")

    print(f"Min Average: {min_grade}")
    print(f"Overall Average: {total_grade / count}")

def find_top(students: list) -> None:
    """Find the top students.

    Args:
        students (list): List of students.
    """

    if not is_filled(students):
        print('There is no top performer')
        return
    greatest = max(students, key = lambda s: sum(s['grades'])/len(s['grades']) if s['grades'] else -1 )

    print(f"The student with the highest average is {greatest['name']} with a grade of {sum(greatest['grades'])/len(greatest['grades'])}.")


def is_number(s: str) -> bool:
    """Check if a string is an int number.
    Args:
        s (str): String.
    """

    try:
        int(s)
        return True
    except ValueError:
        return False


def is_number_in_range(s: str, low: int = 0, high: int = 100) -> bool:
    """
    Check if a string is an integer number and belongs to [low, high].

    Args:
        s (str): String to check.
        low (int): Lower bound.
        high (int): Upper bound.
    """

    if is_number(s):
        value = int(s)
        return low <= value <= high
    return False


def is_filled(students: list) -> bool:
    """Check if there are grades.
    Args:
        students (list): List of students.

    Returns:
        bool: True if there are grades.
    """

    if not students:
        print('No students entered.')
        return False

    for student in students:
        if student['grades']:
            return True

    print('No grades entered.')
    return False

def is_number1(s: str) -> bool:
    """Check if a string is a number.

    Args:
        s (str): String.

    Returns:
        bool: True if string is a number.
    """

    try:
        float(s)
        return True
    except ValueError:
        return False



def main():
    students: list[dict[str, list[int]]] = []

    while True:
        display_interface()

        try:
            choice = int(input())
            if choice == 1:
                add_student(students)
            elif choice == 2:
                add_grade(students)
            elif choice == 3:
                make_report(students)
            elif choice == 4:
                find_top(students)
            elif choice == 5:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5")

        except ValueError:
            print('Invalid input. Please enter a number.')

if __name__ == '__main__':
    main()