student = dict()

student['name'] = input("What's the name of the student? ")
student['media'] = float(input("What's the media of the student? "))

if (student['media'] >= 7): print(f"{student['name']} is approved!")
else: print(f"{student['name']} is reproved!")