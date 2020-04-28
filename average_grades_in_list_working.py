
   #  Enter grades to calculate mean/average grades. tyep e to exit\n",

   print(\"Enter grades to calculate mean/average grades. tyep e to exit\")\n",
   
   # create an empty list
   grades = []
    
   while( True ) :
      grade = input(" enter grades ")
      if grade == e :
         break
      else :
         grade = float(grade)
         grades.append(grade)
   print(grades)
   
   for grade in grades :
      sum = sum + grade
      average = sum / len(grades)