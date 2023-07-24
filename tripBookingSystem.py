# Build a Bus/Air/Rail Booking System 
# where the user can choose a source and 
# destination from the list given and 
# enter the information passenger-wise, 
# depending on the distance cost shall 
# be computed. Rail and Air systems will 
# have different fares for different classes. 
# The student should be able to think of 
# the system as to how he/she uses it as a user.


# Selecting the departure location

sourceLocations = ["Delhi","Mumbai","Kolkata","Dehradun"]
destinationLocations = ["Delhi","Mumbai","Kolkata","Dehradun"]

modes = ["Bus","Rail","Air"]

print("\n",sourceLocations,"\nWhat is your current location?\nSelect number as per the order: ")
departureLocation = sourceLocations[int(input("Select location: "))-1]    # following 0-based indexing in lists, so need to subtract 1
print(departureLocation)

#removing the source location from the list of destination locations
for i in destinationLocations:
    if i == departureLocation:
        destinationLocations.remove(i)

#selecting the destination location
print("\n",destinationLocations,"\nWhat is your destination location?\nSelect number as per the order: ")
destination = destinationLocations[int(input("Select destination: "))-1]
print(destination)


#selecting the mode of transport
print("\n",modes,"\nSelect your mode of transport: ")
modeTransport = modes[int(input("Select mode of transport: "))-1]
print("\nYou've selected ",modeTransport," as your means of travel!")


#taking the basic information from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
phoneNumber = input("Enter your mobile number: ")
dateOfJourney = input("Enter your date of journey in DD/MM/YYYY format: ")
numberOfTickets = int(input("Enter number of tickets: "))
email = input("Enter your email address for us to share the tickets: ")


#defining a ticket creation method that will basically set the fair for distinct routes.

def ticketCreation(destination, numberOfTickets, source, mode):

    total = 0
    ticketFair = 0

    #["Delhi","Mumbai","Kolkata","Dehradun"]

    if source == "Delhi" and destination == "Mumbai":
        ticketFair = 1000
    elif source == "Delhi" and destination == "Kolkata":
        ticketFair = 1200
    elif source == "Delhi" and destination == "Dehradun":
        ticketFair = 800

    if source == "Mumbai" and destination == "Delhi":
        ticketFair = 1250
    elif source == "Mumbai" and destination == "Kolkata":
        ticketFair = 1100
    elif source == "Mumbai" and destination == "Dehradun":
        ticketFair = 1800

    if source == "Kolkata" and destination == "Mumbai":
        ticketFair = 1300
    elif source == "Kolkata" and destination == "Delhi":
        ticketFair = 1450
    elif source == "Kolkata" and destination == "Dehradun":
        ticketFair = 1850

    if source == "Dehradun" and destination == "Mumbai":
        ticketFair = 1800
    elif source == "Dehradun" and destination == "Delhi":
        ticketFair = 750
    elif source == "Dehradun" and destination == "Kolkata":
        ticketFair = 1700

    
    fairClass, ticketPrice = fairing(mode, ticketFair)

    if numberOfTickets > 1:
        for i in range(numberOfTickets-1):
            additionalTicket = int(input("Enter the age of other passenger: "))
            if additionalTicket < 10:
                total = total + ticketPrice/1.5
            else:
                total += ticketPrice

    total += ticketPrice
    return total




#method for total trip fair calculation
def fairing(mode, price):
    classes = ["Standard","First","Middle","Economy"]

    ticketPrice = 0

    if mode == "Bus":
        fair_class = classes[3]

    elif mode == "Air":
        print("\n",classes,"\nPlease select a class. \nSelect number as per the order: ")
        fair_class = classes[int(input("Select class: "))-1]
        print(fair_class)
    elif mode == "Rail":
        print("\n",classes,"\nPlease select a class. \nSelect number as per the order: ")
        fair_class = classes[int(input("Select class: "))-1]


    if fair_class == "Standard":
        ticketPrice = price
    elif fair_class == "Economy":
        ticketPrice = 1.5*price
    elif fair_class == "Middle":
        ticketPrice = price*2
    elif fair_class == "First":
        ticketPrice = price*3
    else:
        print("Invalid Selection")

    return fair_class, ticketPrice
            

#method where the tickets are generated and checked if everything's intact
def ticketChecking(name, destination, source, numberOfTickets, mode):

    if destination == source:
        print("Error! Source location cannot be same as current location..")
        return 0, False
    else:
        total = ticketCreation(destination, numberOfTickets, source, mode)
        return total, True



total, check = ticketChecking(name, destination, departureLocation, numberOfTickets, modeTransport)

if check ==  True:
    print("\nName: ", name,
    "\nNumber of Tickets: ", numberOfTickets,
    "\nDate of journey: ", dateOfJourney,
    "\nAge: ", age,
    "\nYour ticket total: ", total,
    "\nThank you for booking ticket. You will get a confirmation over the email shortly.")

