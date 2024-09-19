import json

DAY_LIST = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
WEEK_DAY = {"sunday": 1, "monday": 2, "tuesday": 3, "wednesday": 4, "thursday": 5, "friday": 6}

HOURS = int(input("how many hours are in the schedule?"))
DAYS = int(input("how many days are in the schedule?"))
CLASSES_NUM = int(input("please enter the amount of classes"))

TOTAL_SCH_HOUR = HOURS * DAYS

for c in range(CLASSES_NUM):
    S = [["free" for x in range(HOURS)] for i in range(DAYS)]
    file = open("class" + str(c) + ".txt", 'w')
    json.dump(S, file)




SUBJECT_NAME_DICT = {}
SUBJECT_NAME = input("please enter subject name")
NUM_OF_LESSON_HOURS = int(input("please enter how many hours for the subject "))
SUM_OF_LESSON_HOURS = 0

while SUBJECT_NAME != "done":
    SUM_OF_LESSON_HOURS += NUM_OF_LESSON_HOURS
    if SUM_OF_LESSON_HOURS > TOTAL_SCH_HOUR:
        SUM_OF_LESSON_HOURS -= NUM_OF_LESSON_HOURS
        print("please enter a lower amount of hours for the"
              " lesson this is how many left:", TOTAL_SCH_HOUR - SUM_OF_LESSON_HOURS)
        NUM_OF_LESSON_HOURS = int(input("please enter how many hours for the subject "))
    elif SUM_OF_LESSON_HOURS == TOTAL_SCH_HOUR:
        print("the schedule is full")
        SUBJECT_NAME = "done"
    else:
        SUBJECT_NAME_DICT[SUBJECT_NAME] = NUM_OF_LESSON_HOURS
        SUBJECT_NAME = input("please enter subject name")
        NUM_OF_LESSON_HOURS = int(input("please enter how many hours for the subject "))
print(SUBJECT_NAME_DICT)



TEACHER_DICT ={}
for i in





