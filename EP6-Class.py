class School:
    schoolName = 'Python101'
class Student:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.scores = {}

    def add_score(self, course, score):
        self.scores[course] = score

    def get_average_score(self):
        total = sum(self.scores.values())
        return total / len(self.scores)

sn = School
s = Student("ลุงวิศวะ", 101)
s.add_score("Math", 85)
s.add_score("Science", 92)
s.add_score("Thai", 92)
print(f'ชื่อโรงเรียน {sn.schoolName}')
print(f'ชื่อ {s.name}')
print(f'คะแนนเฉลี่ย {s.get_average_score()}')