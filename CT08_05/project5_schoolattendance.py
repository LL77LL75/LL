def percent(attended, total):
    if total == 0:
        return 0
    return (attended / total) * 100
attendence_dict = {
    "john": (True, True, False, True, True),
    "jane": (True, False, False, True, False),
    "doe": (False, False, False, False, False),
    "smith": (True, True, True, True, True),
    "sara": (True, False, True, True, False)
}

attendance_dictionary = {
    "Matthew" : [],
    "Jayden" : [],
    "Isaac" : [],
    "Ayden" : [],
    "Noah" : [],
    "Sam" : [],
    "Ryan" : [],
    "Elim" : [],
    "Angeline" : [],
    "Youmi" : [],
    "Artemis" : [],
    "Edgar" : [],
    "Josh" : [],
    "Isabelle" : []
}
def take_attendance(attendance_dictionary):
    ans = False
    while not ans:
        for name,attendance_list in attendance_dictionary.items():
            attendence = (input(f"Enter if the person is here: {name}")).strip()
            if attendence.lower() == "y":
                attendance_list.append(True)
            elif attendence.lower() == "n":
                attendance_list.append(False)
            else:
            print("Invalid input, please enter 'y' or 'n'.")
