class StudentProfile:
    def __init__(self, name, id, cgpa):
        self.name = name
        self._id = id
        self.__cgpa = cgpa 

    def show_cgpa(self):
        return self.__cgpa

student_profile = StudentProfile('Tamim', '101', '-67')

print(f'Student Name : {student_profile.name}')
print(f'Student ID : {student_profile._id}')
print(f'CGPA : {student_profile.show_cgpa()}')