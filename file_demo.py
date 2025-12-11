# course_file = open("course.txt")


# for line in course_file:
#    print(line)

# with "open" function the program is open 
# and can be  closed traditionally using:
# "courses_file.close()"


# But there is a better way to do this in python using the "With" Key word

with open('course.txt') as course_file:
    for line in course_file:
        print(line)