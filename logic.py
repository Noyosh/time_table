import json

BUSY = "busy"
FREE = "free"

DAY_LIST = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
WEEK_DAY = {"sunday": 0, "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5}

CLASSES_NUM = input("please enter the num of classes")
while not CLASSES_NUM.isnumeric():
    print("please enter a number")
    CLASSES_NUM = input("please enter the num of classespip")
CLASSES_NUM = int(CLASSES_NUM)

HOURS = input("Please enter the number of study hours per day between 1-8")
while not HOURS.isnumeric or int(HOURS) > 8 or int(HOURS) < 0:

    HOURS = input("Please enter the number of study hours per day between 1-8")
HOURS = int(HOURS)

DAYS = (input("Please enter the number of school days per week between 1-8"))
while not DAYS.isnumeric or int(DAYS) > 6 or int(DAYS) < 0:

    DAYS = (input("Please enter the number of school days per week between 1-8"))
DAYS = int(DAYS)

TOTAL_SCH_HOUR = HOURS * DAYS

SUBJECT_NAME_DICT = {}
SUBJECT_NAME = input("Enter the name of the lesson here, enter done to stop")

NUM_OF_LESSON_HOURS = input("please enter how many hours for the subject ")

SUM_OF_LESSON_HOURS = 0

while SUBJECT_NAME != "done":
    while not NUM_OF_LESSON_HOURS.isnumeric():
        print("please enter a number")
        NUM_OF_LESSON_HOURS = input("Enter the number of study hours for the lesson here")

    NUM_OF_LESSON_HOURS = int(NUM_OF_LESSON_HOURS)

    SUM_OF_LESSON_HOURS += NUM_OF_LESSON_HOURS
    if SUM_OF_LESSON_HOURS > TOTAL_SCH_HOUR:
        SUM_OF_LESSON_HOURS -= NUM_OF_LESSON_HOURS
        print("please enter a lower amount of hours for the"
              " lesson this is how many left:", TOTAL_SCH_HOUR - SUM_OF_LESSON_HOURS)
        NUM_OF_LESSON_HOURS = input("Enter the number of study hours for the lesson here")

    elif SUM_OF_LESSON_HOURS == TOTAL_SCH_HOUR:
        SUBJECT_NAME_DICT[SUBJECT_NAME] = NUM_OF_LESSON_HOURS
        print("the schedule is full")
        SUBJECT_NAME = "done"

    else:
        SUBJECT_NAME_DICT[SUBJECT_NAME] = NUM_OF_LESSON_HOURS
        SUBJECT_NAME = input("Enter the name of the lesson here, enter done to stop")
        if not SUBJECT_NAME == "done":
            NUM_OF_LESSON_HOURS = input("Enter the number of study hours for the lesson here")

print(SUBJECT_NAME_DICT)

SUBJECT_NAME_LIST = list(SUBJECT_NAME_DICT.keys())
TEACHER_LIST = []

TEACHER_BUSY_DAYS = {}

for name in SUBJECT_NAME_LIST:
    print(name)
    TEACHER_NUM = input("Enter here how many teachers teach this lesson")
    while not TEACHER_NUM.isnumeric():
        TEACHER_NUM = input("Enter here how many teachers teach this lesson")
    TEACHER_NUM = int(TEACHER_NUM)

    for num in range(TEACHER_NUM):
        BUSY_DAYS_LIST = []
        NUM_OF_DAYS = 0

        print("teacher num", num + 1)
        BUSY_DAYS = input("please enter which days you cannot work or done")

        while BUSY_DAYS != "done":
            if BUSY_DAYS.isnumeric or (not (BUSY_DAYS in DAY_LIST)):
                print("please enter a currect name")
            else:
                BUSY_DAYS_LIST.append(WEEK_DAY[BUSY_DAYS])
                BUSY_DAYS = input("please enter which days you cannot work or enter done to stop")
                NUM_OF_DAYS += 1

                for i in list(TEACHER_BUSY_DAYS.values()):
                    if NUM_OF_DAYS > i:
                        TEACHER_BUSY_DAYS_NEW = {"teacher" + name + str(num) + ".txt": NUM_OF_DAYS}
                        TEACHER_BUSY_DAYS_NEW.update(TEACHER_BUSY_DAYS)
                        TEACHER_BUSY_DAYS = TEACHER_BUSY_DAYS_NEW
                    else:
                        TEACHER_BUSY_DAYS["teacher" + name + str(num) + ".txt"] = NUM_OF_DAYS

                S = [[FREE for x in range(HOURS)] for i in range(DAYS)]
                for i in range(len(S)):
                    if i in BUSY_DAYS_LIST:
                        for j in range(len(S[i])):
                            S[i][j] = BUSY
                file = open("teacher_" + name + "_" + str(num) + ".txt", 'w')
                TEACHER_LIST.append("teacher_" + name + "_" + str(num) + ".txt")
                json.dump(S, file)
            BUSY_DAYS = input("please enter which days you cannot work or enter done to stop")

CLASS_NAME_LIST = []

for c in range(CLASSES_NUM):
    S = [[FREE for x in range(HOURS)] for i in range(DAYS)]

    for name in SUBJECT_NAME_LIST:
        subject_full = 0
        for teacher in TEACHER_LIST:
            subject_name = teacher.split("_")
            if subject_full < SUBJECT_NAME_DICT[name] and (name in subject_name):
                file = open(teacher, 'r')
                sch_teacher = json.load(file)
                for day in range(len(S)):
                    for hour in range(len(S[day])):
                        if (S[day][hour] == FREE and sch_teacher[day][hour] == FREE
                                and subject_full < SUBJECT_NAME_DICT[name]):
                            sch_teacher[day][hour] = BUSY
                            file = open(teacher, 'w')
                            json.dump(sch_teacher, file)
                            S[day][hour] = teacher
                            subject_full += 1
    file = open("class" + str(c) + ".txt", 'w')
    CLASS_NAME_LIST.append("class" + str(c) + ".txt")
    json.dump(S, file)
