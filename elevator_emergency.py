floors = 10
current_floor = 7  # this is just a starting point
user_floor = 3  # another starting point
emergency = False

user_floor = 2
current_floor = 7

difference = user_floor - current_floor

if difference < 0:
    if emergency == False:
        print( "Move down" )

if difference > 0:
    if emergency == False:
        print(" Move Up " )