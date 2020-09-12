# Author: Shakeb Siddiqui sms8508@psu.edu

def getGradePoint(grade):
 if grade == ("A"):
  course1gp=float(4.0)
 elif grade == ("A-"):
  course1gp=float(3.67)
 elif grade == ("B+"):
  course1gp=float(3.33)
 elif grade == ("B"):
  course1gp=float(3.0)
 elif grade == ("B-"):
  course1gp=float(2.67)
 elif grade == ("C+"):
  course1gp=float(2.330)
 elif grade == ("C"):
  course1gp=float(2.0)
 elif grade == ("D"):
  course1gp=float(1.0)
 elif grade == ("F"):
  course1gp=float(0.0)
 else:
  course1gp=float(0.0)
 return course1gp



def run():
  grade1 = input("Enter your course 1 letter grade: ")
  Gp1 = getGradePoint(grade1)
  credit1 = input("Enter your course 1 credit: ")
  print (f"Grade point for course 1 is: {Gp1}")

  grade2 = input("Enter your course 2 letter grade: ")
  Gp2 = getGradePoint(grade2)
  credit2 = input("Enter your course 2 credit: ")
  print (f"Grade point for course 2 is: {Gp2}")

  grade3 = input("Enter your course 3 letter grade: ")
  Gp3 = getGradePoint(grade3)
  credit3 = input("Enter your course 3 credit: ")
  print (f"Grade point for course 3 is: {Gp3}")

  credit1=float(credit1)
  credit2=float(credit2)
  credit3=float(credit3)

  GPA = ((Gp1 * credit1) + (Gp2 * credit2) + (Gp3 * credit3)) / (credit1 + credit2 + credit3)
  return GPA
  

print(f"Your GPA is: {run()}")