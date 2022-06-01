class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: list, score: float):
        self.name, self.age, self.tracks, self.score = name, age, tracks, score

    def change_name(self, new_name):
        self.name = new_name
        return self.name

    def change_age(self, new_age):
        self.age = new_age
        return self.age

    def add_track(self, new_track):
        self.tracks.append(new_track)
        return self.tracks[-1]

    def get_score(self, new_score):
        self.score = new_score
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
print(Bob)
# Expected methods
a = Bob.change_name("Peter")
b = Bob.change_age(34)
c = Bob.add_track("UI/UX")
d = Bob.get_score(34)
print(a, b, c, d)
