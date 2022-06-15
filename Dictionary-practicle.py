# book practicle

# 19 traverse dicionary and display its elements on different lines
print("Q 19 : ")
Days={
    'Monday':1,
    'Tuesday':2,
    'Wednesday':3,
    'Thursday':4,
    'Friday':5,
    'Saturday':6,
    'Sunday':7
}

for i in Days:
    print(f"{i} ----> {Days[i]}")

print()

# 20 Traverse a dictionary and display its elements on same line
print("Q 20 : ")
Days = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}

for i in Days:
    print(f"{i} ----> {Days[i]}",end=' ')

print()
print()

# 21 Create dictionary and display its information on screen
print("Q 21 : ")
computerscience=dict()
i=0
n=int(input("Number of students = "))

while i<n:
    name=str(input("Name : "))
    grade=str(input("Grade : "))
    computerscience[name]=grade
    i+=1

print("{:^10} {:^10} {:^10}".format("Computer Science","Name of student","Grade"))
for i in computerscience:
    print("\t {:^9}  {:^14}  {:^14}".format("Python",i,computerscience[i]))

print()

# 22 display information in acsending order of names
print("Q 22 : ")
computerscience = dict()
i = 0
n = int(input("Number of students = "))

while i < n:
    name = str(input("Name : "))
    grade = str(input("Grade : "))
    computerscience[name] = grade
    i += 1

print("{:^10} {:^10} {:^10}".format("Computer Science", "Name of student", "Grade"))
for i in sorted(computerscience):
    print("\t {:^9}  {:^16}  {:^10}".format("Python", i, computerscience[i]))

print()
