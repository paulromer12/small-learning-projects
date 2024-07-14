# Paul Romer, CSD205, July 9 2024, Module 9.2 assignment

# Create a student class that will calculate and display student cumulative GPA. Your program will then use the methods of the student class to accomplish the following::
# 		Prompt the user for the first and last name of the student.
# 		Create a student object by passing the first and last name to the __init__ method.
# 		Create a loop that prompts the user for the following: The credits and grade for each course the student has taken.
# 		Once the user ends the loop, display the student’s cumulative GPA.
# If you are unfamiliar with how to calculate a cumulative GPA here is a site that will provide you with the formula and walk through several examples: How to Calculate Your Cumulative GPA | Rutgers MyRun (Rutgers University-Newark, 2023).


class Student:
    def __init__(self, first_name,  last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
    
    def add_course(self, credits, grade):
        self.courses.append({"credits": credits, "grade": grade})
        print(f"Added: credits={credits}, grade={grade}")
        print("Current list of courses:")
        for course in self.courses:
            print(course)
        print()

    def calculate_gpa(self):
        total_credits = 0
        total_grade_points = 0
        for course in self.courses:
            total_credits += course["credits"]
            total_grade_points += course["credits"] * course["grade"]
        if total_credits == 0:
            return "No Credits, Can't divide by zero"
        else:
            gpa = total_grade_points / total_credits
            return gpa

    def display_gpa(self):
        gpa = self.calculate_gpa()
        if isinstance(gpa, str):
            print(gpa)
        else:
            print(f"The cumulative GPA for {self.first_name} {self.last_name} is {gpa:.2f}")


def main():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    print()
    student = Student(first_name, last_name)

    while True:
        try:
            credits = int(input("Enter the number of credits for the course (0 to quit and print GPA): "))
            if credits == 0:
                break
            grade = float(input("Enter the grade for the course (0.0 - 4.0): "))
            student.add_course(credits, grade)
        except ValueError:
            print("Invalid input. Please enter valid numbers for credits and grade.")

    student.display_gpa()


if __name__ == "__main__":
    main()