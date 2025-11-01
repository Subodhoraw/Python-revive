class Student:
    """A class to manage student information and grades"""
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, subject, score):
        """Add a grade for a subject"""
        self.grades.append({"subject": subject, "score": score})
        return f"Added {score}% in {subject} for {self.name}"
    
    def get_average(self):
        """Calculate average grade"""
        if not self.grades:
            return 0
        total = sum(grade["score"] for grade in self.grades)
        return round(total / len(self.grades), 2)
    
    def get_letter_grade(self):
        """Convert average to letter grade"""
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    def display_report(self):
        """Display complete grade report"""
        print(f"\n{'='*50}")
        print(f"GRADE REPORT")
        print(f"{'='*50}")
        print(f"Student: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"\n{'Subject':<20} {'Score':>10}")
        print(f"{'-'*50}")
        
        for grade in self.grades:
            print(f"{grade['subject']:<20} {grade['score']:>9}%")
        
        print(f"{'-'*50}")
        print(f"{'Average:':<20} {self.get_average():>9}%")
        print(f"{'Letter Grade:':<20} {self.get_letter_grade():>10}")
        print(f"{'='*50}")


# === USING THE STUDENT CLASS ===

# Create students
student1 = Student("Alice Johnson", "S12345")
student2 = Student("Bob Smith", "S12346")

# Add grades for student 1
print(student1.add_grade("Math", 95))
print(student1.add_grade("English", 88))
print(student1.add_grade("Science", 92))
print(student1.add_grade("History", 85))

# Add grades for student 2
print(student2.add_grade("Math", 78))
print(student2.add_grade("English", 82))
print(student2.add_grade("Science", 75))

# Display reports
student1.display_report()
student2.display_report()

# Access individual data
print(f"\n{student1.name}'s average: {student1.get_average()}%")
print(f"{student2.name}'s letter grade: {student2.get_letter_grade()}")