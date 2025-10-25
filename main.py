#Write a program to show students' grades by entering five subject marks and calculating average marks and grades.
#  For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?
grade1=int(input("Enter your first grade: "))
grade2=int(input("Enter your second grade: "))
grade3=int(input("Enter your third grade: "))
grade4=int(input("Enter your fourth grade: "))
grade5=int(input("Enter your fifth grade: "))
average=(grade1+grade2+grade3+grade4+grade5)/5
if average>=91 and average<=100:
    print("A1")
elif average>=81 and average<=90:
    print("A2")
elif average>=71 and average<=80:
    print("B1")
elif average>=61 and average<=70:
    print("B2")
elif average>=51 and average<=60:
    print("C1")
elif average>=41 and average<=50:
    print("C2")
elif average>=31 and average<=40:
    print("D1")
elif average>=21 and average<=30:
    print("D2")
elif average>=11 and average<=20:
    print("E1")
else:
    print("E2")