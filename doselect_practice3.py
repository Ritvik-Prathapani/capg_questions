class StuTable:
    def __init__(self, student_id, name, standard):
        self.id = student_id
        self.name = name
        self.standard = standard

class MarkTable:
    def __init__(self, student_id, mark):
        self.id = student_id
        self.mark = mark

class SqlOperation:
    def __init__(self, students, marks):
        self.students = students
        self.marks = marks

    def joinTable(self):
        """Joins student table with marks table based on student ID."""
        mark_dict = {}  # Dictionary to store marks by student ID
        for mark in self.marks:
            if mark.id not in mark_dict:
                mark_dict[mark.id] = []
            mark_dict[mark.id].append(mark.mark)

        # Filter students who have marks and store their marks
        joined_list = []
        for student in self.students:
            if student.id in mark_dict:
                joined_list.append((student.id, student.name, mark_dict[student.id]))

        return joined_list

    def selectByStandard(self, standard):
        """Selects students by standard."""
        return [student.name for student in self.students if student.standard == standard]

# Creating student records
s1 = StuTable(1, "John", 3)
s2 = StuTable(2, "Jack", 3)
s3 = StuTable(3, "Jerry", 4)
s4 = StuTable(4, "Tim", 5)

# Creating marks records
m1 = MarkTable(1, 99)
m2 = MarkTable(2, 99)
m3 = MarkTable(2, 80)  # Jack has two marks

# Performing SQL-like operations
sql1 = SqlOperation([s1, s2, s3, s4], [m1, m2, m3])

# Running the join operation
result = sql1.joinTable()

# Printing the result
print("Joined Table (Students with Marks):")
for student_id, name, marks in result:
    print(f"ID: {student_id}, Name: {name}, Marks: {marks}")

print(sql1.selectByStandard(3))  # Selecting students by standard
