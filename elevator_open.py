floors = 10
current_floor = 7  # this is just a starting point
user_floor = 3  # another starting point
emergency = False

user_floor = 2
current_floor = 7

difference = user_floor - current_floor

if difference < 0 :
   if emergency == False :
       current_floor = user_floor
       print( "Move down" )

elif difference > 0 :
   if emergency == False :
       current_floor = user_floor
       print(" Move Up " )
    
else :
   (" Open door ")