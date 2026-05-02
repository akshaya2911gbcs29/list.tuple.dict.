students={}
n=int(input("Enter no of students:"))
for i in range(n):
    name=input("Enter student name:")
    mark=int(input("Enter marks:"))
    students[name]=mark
search=input("Enter student name to find marks:")
print("Marks:",students.get(search,"Student not found"))
