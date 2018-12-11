from W10_Overerving.Models.Persoon import Persoon
from W10_Overerving.Models.Student import Student

# class ouder

class Ouder(Persoon):

    def __init__(self, parnaam, parvoornaam, pargeboortejaar):
        super().__init__(parnaam, parvoornaam, pargeboortejaar)
        self.__lijststudenten = []

    def voeg_student_toe(self,student):
        if not isinstance(student, Student):
            raise ValueError("Ongeldige student.")
        #geen dubbles
        if not student in self.__lijststudenten:
            self.__lijststudenten.append(student)
        return student

    def geef_info_student(self):
        info_student = ""
        for student in self.__lijststudenten:
            info_student +=(str(student))
        return info_student

    def geef_opleidingen_studenten(self):
        lijstopleidingen = []
        for student in self.__lijststudenten:
            lijstopleidingen.append(str(student) + "heeft richting " + student.opleiding)
        return lijstopleidingen

    def __str__(self):
        return ("Ouder {0}".format(super().__str__()))
