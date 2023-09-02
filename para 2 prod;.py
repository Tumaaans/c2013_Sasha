import random


class Student:
    def __init__(self, name):
        self.name = name
        self.glandess = 50
        self.progress = 0
        self.alive = True


    def to_study(self):
        print("ля учиться пора.....")
        self.progress += 0.12
        self.glandess -= 3


    def to_sleep(self):
        print("ухххх спать наконец")
        self.glandess += 3


    def to_chill(self):
        print("Rest time")
        self.glandess += 5
        self.progress -= 0.1

    def is_alive(self):
        if  self.progress < -0.5:
            print("иди какай")
            self.alive = False


        elif self.glandess <= 0:
            print("суецыд")
            self.alive = False


        elif self.progress > 5:
            print("Володька наглаженый")
            self.alive = False


    def end_of_day(self):
        print(f"Gladness = {self.glandess}")
        print(f"Progress = {self.progress}")

    def live(self, day):
        day = f"Day {day} of {self.name} life"
        print(f"{day:=^30}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
            self.to_study()


        elif live_cube == 2:
            self.to_chill()


        elif live_cube == 3:
            self.to_sleep()


        self.end_of_day()
        self.is_alive()

vasya = Student(name="Vasyliy")

for day in range(365):
    if vasya.alive == False:
        break
    vasya.live(day)
