student = []
n=int(input("enter the number:"))
for i in range(n):
    print("Student",i+1)
    id=int(input("enter the student id:"))
    name=input("enter the student name:")
    marks=float(input("enter the student marks:"))
    student.append((id,name,marks))
student=tuple(student)
print("Student details:")
for j in range(0,len(student)):
    print(student[j][0],'\t',student[j][1],'\t',student[j][2])
search_id=int(input("enter the student id:"))
for s in student:
    if s[0]==search_id:
        print("record found:\nID:",s[0],"\nName:",s[1],"\nMarks:",s[2],"\n")
        break
    else:
         print("Record not found")
print("Less than 40")
max=0
t=0
for s in student:
    if s[2]<40:
        print(s[0],'\t',s[1],'\t',s[2])
    if s[2]>max:
        max=s[2]
        tup=(s[0],s[1],s[2])
    t+=s[2]
avg=t/n
print("Student with highest mark:",tup)
print("Average:",avg)
