"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""

passing_grade = 50

def input_students(num_students):
    students = [
        {
            'name': 'Pornpipat',
            'scores': [35, 54, 60]
        },
        {
            'name': 'Soda',
            'scores': [87, 75, 93]
        }
    ]
    return students


def calculate_averages(students):
    for student in students:
        sum_score = 0
        for score in student['scores']:
            sum_score += score
        student['average'] = sum_score / len(student['scores'])  
    return students


def display_results(students):
    print("\n=== Student Details ===")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Average Score: {student['average']:.1f}")  
        if student['average'] >= passing_grade:  
            print("Status: PASS\n")
        else:
            print("Status: FAIL\n")


num = int(input("Enter number of students: "))
students = input_students(num)
calculate_averages(students)
display_results(students)
