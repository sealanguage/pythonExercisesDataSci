grades = []    #initialize an empty list

while True :    #this program runs in an infinite loop
   print(" Enter your choice ")
   print(" Enter grades -> 1 ")
   print(" Delete grades -> 2 ")
   print(" ")
   print(" ")
   print(" Exit program -> 6 ")

   choice = input(" -> ")

   if len(choice == 1) :
      print("enter a valid choice number 1 - 6")
      continue

   if int(choice) == 6 :
      break
