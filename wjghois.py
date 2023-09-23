def face_control(name):
    if name == 'Vasya' or name == 'Vasiliy':
        raise TypeError (f"no {name}. We dont need {name}")
    else:
        return name

ch = int (input("how many people"))
for i in range(ch):
    name = input("What is you name")
    face_control(name)
    print(f"Welcome {name}")
    