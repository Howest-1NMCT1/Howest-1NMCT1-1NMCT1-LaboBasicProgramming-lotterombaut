#test ouder
from W10_Overerving.Models.Ouder import Ouder
from W10_Overerving.Models.Student import Student

# student aanmaken
student1 = Student("Lotte", "Rombaut", 671, "MCT", 1999)
student2 = Student("Koek", "Doos", 952 , "LOL", 1932)


#ouder aanmaken
ouder1 = Ouder("Ou", "Der", 1967)
ouder2 = Ouder("Mama", "Moeke", 1976)

#studenten lijst tievoegen aan ouder
ouder1.voeg_student_toe(student1)
ouder2.voeg_student_toe(student2)

print(ouder1.geef_info_student())
print(ouder2.geef_info_student())

print(ouder1.__str__())
print(ouder2.__str__())