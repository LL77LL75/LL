from unicodedata import name
def percent(attended, total):
    if total == 0:
        return 0
    return (attended / total) * 100
def take_attendance(attendance_dictionary):
    ans = False
    for i in attendance_dictionary.items():
        day = 1
        ans = " "
        gyatt = True
        name = i[0]
        attendence = []
        while gyatt == True:
            ans = input(f"Is {name} present on day {day}? (y/n): ")
            if ans == "y":
                day+=1
                attendence.append(True)
                gyatt = True
            elif ans == "n":
                day+=1
                attendence.append(False)
                gyatt = True
            elif ans == "":
                print("Attendance taking ended.")
                day = 1
                gyatt = False
            else:
                print("Invalid input, please enter 'y' or 'n'.")
                gyatt = True
def calculate_attendance_percentage(attendance_dictionary):
    percentages = {}
    for name, attendance in attendance_dictionary.items():
        total_days = len(attendance)
        days_present = sum(attendance)
        percentages[name] = days_present/total_days * 100
    return percentages
attendence_dictionary = {
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
take_attendance(attendence_dictionary)
print(f"Attendance percentages: {calculate_attendance_percentage(attendence_dictionary)}")
