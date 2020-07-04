#  print("Enter grades to calculate mean/average grades. tyep e to exit")

# create an empty list
grades = []
sum = 0

while( True ) :
   grade = input(" enter grades ")
   if grade == "e" :
      break
   else :
      grade = float(grade)
      grades.append(grade)
print("grades: ", grades)


for grade in grades :
   sum = sum + grade
average = sum /len(grades)
print("Average class grade is: ", average)