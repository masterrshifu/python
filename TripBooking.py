print("Hello! Welcome to Hansuja Travel Booking Serrvice!")

place = ["Mumbai", "New Delhi", "Kolkata", "Jaipur", "Agra", "Udaipur"]

price = 0     #what is this x?

print("The choices for the areas of departure and arival are", place)
departure = int(input("Which of the folowing places will you be departing from? ( state the place acording to it's number on the list): "))
arival = int(input("Which of the folowing places will you be travelling to? ( state the place acording to it's number on the list): "))

if departure-1 > len(place) or arival-1 > len(place):
    print("Sorry! There seems to have been a error with your arivial and departure areas! Please redo this action!")

else:
    transport = ["Bus", "Train", "Airplane"]
    
    print(transport)
    
    transportation = int(input("Which of the following ways would you like to travel ? ( state the way acording to it's number on the list): "))
    
    if transport[transportation-1] == transport[0]:
        if place[departure-1] == place[0]:
            if place[arival-1] == place[0]:
                price = 0
            
            elif place[arival-1] == place[1]:
                 price = 112
            
            elif place[arival-1] == place[2]:
                price = 100
            
            elif place[arival-1] == place[3]:
                price = 105
        
            elif place[arival-1] == place[4]:
                price = 110
        
            else:
                price = 140
        
        elif place[departure-1] == place[1]:
            
            if place[arival-1] == place[0]:
                price = 112
            
            elif place[arival-1] == place[1]:
                price = 0
        
            elif place[arival-1] == place[2]:
                price = 105
        
            elif place[arival-1] == place[3]:
                price = 125
        
            elif place[arival-1] == place[4]:
                price = 112
        
            else:
                price = 142
    
        elif place[departure-1] == place[2]:
            
            if place[arival-1] == place[0]:
                price = 110
            
            elif place[arival-1] == place[1]:
                price = 112
        
            elif place[arival-1] == place[2]:
                price = 0
        
            elif place[arival-1] == place[3]:
                price = 135
        
            elif place[arival-1] == place[4]:
                price = 112
        
            else:
                price = 102
        
        elif place[departure-1] == place[3]:
        
            if place[arival-1] == place[0]:
                price = 113
        
            elif place[arival-1] == place[1]:
                price = 110
        
            elif place[arival-1] == place[2]:
                price = 105
        
            elif place[arival-1] == place[3]:
                price = 0
        
            elif place[arival-1] == place[4]:
                price = 102
        
            else:
                price = 112
                
        elif place[departure-1] == place[4]:
            
            if place[arival-1] == place[0]:
                price = 110
        
            elif place[arival-1] == place[1]:
                price = 112
        
            elif place[arival-1] == place[2]:
                price = 105
        
            elif place[arival-1] == place[3]:
                price = 135
        
            elif place[arival-1] == place[4]:
                price = 0
        
            else:
                price = 102
        
        else:
            if place[arival-1] == place[0]:
                price = 120
        
            elif place[arival-1] == place[1]:
                price = 115
        
            elif place[arival-1] == place[2]:
                price = 105
        
            elif place[arival-1] == place[3]:
                price = 135
        
            elif place[arival-1] == place[4]:
                price = 110
        
            else:
                price = 0

    elif transport[transportation-1] == transport[1]:
        if place[departure-1] == place[0]:
            if place[arival-1] == place[0]:
                price = 0
            
            elif place[arival-1] == place[1]:
                 price = 112
            
            elif place[arival-1] == place[2]:
                price = 100
            
            elif place[arival-1] == place[3]:
                price = 105
        
            elif place[arival-1] == place[4]:
                price = 110
        
            else:
                price = 140
        
        elif place[departure-1] == place[1]:
            
            if place[arival-1] == place[0]:
                price = 112
            
            elif place[arival-1] == place[1]:
                price = 0
        
            elif place[arival-1] == place[2]:
                price = 105
        
            elif place[arival-1] == place[3]:
                price = 125
        
            elif place[arival-1] == place[4]:
                price = 112
        
            else:
                price = 142
    
        elif place[departure-1] == place[2]:
            
            if place[arival-1] == place[0]:
                price = 110
            
            elif place[arival-1] == place[1]:
                price = 112
        
            elif place[arival-1] == place[2]:
                price = 0
        
            elif place[arival-1] == place[3]:
                price = 135
        
            elif place[arival-1] == place[4]:
                price = 112
        
            else:
                price = 102
        
        elif place[departure-1] == place[3]:
        
            if place[arival-1] == place[0]:
                price = 113
        
            elif place[arival-1] == place[1]:
                price = 110
        
            elif place[arival-1] == place[2]:
                price = 105
        
            elif place[arival-1] == place[3]:
                price = 0
        
            elif place[arival-1] == place[4]:
                price = 102
        
            else:
                price = 112
                
        elif place[departure-1] == place[4]:
            
            if place[arival-1] == place[0]:
                price = 110
        
            elif place[arival-1] == place[1]:
                price = 112
        
            elif place[arival-1] == place[2]:
                price = 105
        
            elif place[arival-1] == place[3]:
                price = 135
        
            elif place[arival-1] == place[4]:
                price = 0
        
            else:
                price = 102
    
    elif transport[transportation-1] == transport[2]:
        
        if place[departure-1] == place[0]:
            
            if place[arival-1] == place[0]:
                price = 0
            
            elif place[arival-1] == place[1]:
                 price = 112
            
            elif place[arival-1] == place[2]:
                price = 100
            
            elif place[arival-1] == place[3]:
                price = 105
        
            elif place[arival-1] == place[4]:
                price = 110
        
            else:
                price = 140
        
        elif place[departure-1] == place[1]:
            
            if place[arival-1] == place[0]:
                price = 112
            
            elif place[arival-1] == place[1]:
                price = 0
        
            elif place[arival-1] == place[2]:
                price = 105
        
            elif place[arival-1] == place[3]:
                price = 125
        
            elif place[arival-1] == place[4]:
                price = 112
        
            else:
                price = 142
    
        elif place[departure-1] == place[2]:
            
            if place[arival-1] == place[0]:
                price = 110
            
            elif place[arival-1] == place[1]:
                price = 112
        
            elif place[arival-1] == place[2]:
                price = 0
        
            elif place[arival-1] == place[3]:
                price = 135
        
            elif place[arival-1] == place[4]:
                price = 112
        
            else:
                price = 102
        
        elif place[departure-1] == place[3]:
        
            if place[arival-1] == place[0]:
                price = 113
        
            elif place[arival-1] == place[1]:
                price = 110
        
            elif place[arival-1] == place[2]:
                price = 105
        
            elif place[arival-1] == place[3]:
                price = 0
        
            elif place[arival-1] == place[4]:
                price = 102
        
            else:
                price = 112
                
        elif place[departure-1] == place[4]:
            
            if place[arival-1] == place[0]:
                price = 110
        
            elif place[arival-1] == place[1]:
                price = 112
        
            elif place[arival-1] == place[2]:
                price = 105
        
            elif place[arival-1] == place[3]:
                price = 135
        
            elif place[arival-1] == place[4]:
                price = 0
        
            else:
                price = 102
        
    else:
        print("It seems that your mode of transport is out of the range")
        price = -1

    if price>-1:
        num = int(input("How many passengers will their be? "))

        price = num*price

        name = input("What is your full name?: ")
        num = input("What is your phone number?: ")
        email = input("What is your email?: ")

        print("------------------------------------")
        print("-Ticket Information-")
        print("Name: ", name)
        print("Phone Number: ", num)
        print("Email: ", email)
        print("Price: ", price)

        print("An email confirmation will be sent to", email)
        
