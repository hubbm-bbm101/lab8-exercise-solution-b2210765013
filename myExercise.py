import sys
d= {}

with open(sys.argv[1],"r+") as file:
#content = file.read().split("\n")
    for line in file:
        person, school = line.split(":")
        d[person] = school

    for student in sys.argv[2].split(","):
        try:
            print("Name: {}, University: {}".format(student, d[student]))
        except:
            print("No record of {} was found".format(student))