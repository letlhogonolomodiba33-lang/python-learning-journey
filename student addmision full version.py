
name=input("Enter your name")
age=int(input("Enter your age"))
mark=int(input("Enter your marks"))

def grade(mark):
    if mark >= 80:
        return "A"
    elif 70<= mark <=79:
        return "B"
    elif 60<= mark <= 69:
        return "C"
    elif 50<= mark <= 59:
        return "D"
    else:
        return("you have failed")


results=grade(mark)
print(results)


student={
   "Name" : name,
   "Age" : age,
   "Marks":mark,
   "Grade" : results,
}

for key, value in student.items():
    print(f"{key}: {value}")

