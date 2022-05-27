class Student:
    student = "Lencier"

    def __init__(self,name,Lname,birth_year,):
        self.name = name
        self.Lname = Lname
        self.birth_year = birth_year

    def full_name(self):
        return "f hello {name}, your last name is{Lname} "

    def birth_year(self):
         return "f hello {name},{Lname} you were born in {birth_year}"

    def initials(self):
        return "f Hi your initials are {name[0]} and {Lname[0]}"
        












