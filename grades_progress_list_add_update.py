grades = []
sum = 0.0

while True :
    print( "Enter your choices - " )
    print( "Enter grades -> 1" )
    print( "List grades -> 2" )
    print( "Delete a grade -> 3" )
    print( "Update a grade -> 4" )
    print( "Clear grades -> 5" )
    print( "Calculate grades -> 6" )
    
    print( "Exit program -> 7" )
    
    choice = int(input( "->" ))
    
 
    if not (choice) <= 7 and choice.isnumeric() :
        print( "Enter a valid choice number 1 - 7" )
        continue
    
    if int(choice) == 7 :
        break
    
    if int(choice) == 1 :
        print( "enter a grades. 'e' to exit." )
        
        while ( True ) :
            grade = input( "->" )
            if grade == "e" :
                break
            else :
                grade = float(grade)
                grades.append(grade)

            continue
        
    if int(choice) == 2 :
        for grade in grades :
            print( grade )
            
    if int(choice) == 3 :
        for grade in grades :
            print(grades)
        index = int(input( "Enter the index to delete" ))
        if index < len(grades) - 1 and index >= 0 :
            grades.pop(index)
        else :
            print( "Invalid index. Try again." )
            
    if int(choice) == 4 :
        for grade in grades :
            print(grades)
        index = int(input( "enter grade to update" ))
        if index < len(grades) - 1 and index >= 0 :
            new_grade = float(input( "->" ))
            grades[index] = new_grade
        else :
            print( "Invalid index. Try again" )
            
    if int(choice) == 5 :
        grades.clear()
        
    if int(choice) == 6 :
        for grade in grades :
            sum = sum + grade
            average = sum /len(grades)
        print("Average class grade is: ", average)
            

