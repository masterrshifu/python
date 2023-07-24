sourceLocations = ["Toronto","Edmonton","Montreal","Victoria"]

destinationLocations = ["Toronto","Edmonton","Montreal","Victoria"]

modes = ["Bus","Rail","Air"]


print("\n",sourceLocations,"\nWhat is your current location?\nSelect number as per the order: ")
departureLocation = sourceLocations[int(input("Select location: "))-1]
print(departureLocation)

for i in destinationLocations:
    if i == sourceLocations:
        destinationLocations.remove(i)


print("\n",destinationLocations,"\nWhat is your destination?\nSelect number according to the order: ")
destination = destinationLocations[int(input("Select destination: "))-1]
print(destination)

print("\n",modes,"\nSelect your mode of transport: ")
modeTransport = modes[int(input("Select mode of transport: "))-1]
print("\nYou've selected ",modeTransport," as your means of travel!")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
phoneNumber = input("Enter your mobile number: ")
dateOfJourney = input("Enter your date of journey in DD/MM/YYYY format: ")
numberOfTickets = int(input("Enter number of tickets: "))
email = input("Enter your email address for us to share the tickets: ")

def fairing (mode,price):
    classes = ["Standard","Economy","Middle","First"]
    ticektPrice = 0

    if mode == "Bus":
        fair_class = classes[1]
    elif mode == "Air":
        print("\n",classes,"\nPlease select a class.\nSelect number as per the order: ")
        fair_class = classes[int(input("Select class: "))-1]
        print(fair_class)
    elif mode == "Rail":
        print("\n", classes, "\nPlease select a class.\nSelect number as per the order: ")
        fair_class = classes[int(input("Select class: ")) - 1]
        print(fair_class)

    if fair_class == "Standard":
        ticketPrice = price
    elif fair_class == "Economy":
        ticketPrice = price*1.5
    elif fair_class == "Middle":
        ticketPrice = price*2;
    elif fair_class == "First":
        ticketPrice = price*3;
    else:
        print("Invalid Selection")
    return fair_class,ticketPrice



def ticketCreation (destination,numberOfTickets,source,mode):

    total = 0
    ticketFair = 0

    if source == "Toronto" and destination == "Victoria":
        ticketFair = 1500
    elif source == "Toronto" and destination == "Montreal":
        ticketFair = 1800
    elif source == "Toronto" and destination == "Edmonton":
        ticketFair = 1900

    if source == "Edmonton" and destination == "Victoria":
        ticketFair = 900
    elif source == "Edmonton" and destination == "Montreal":
        ticketFair = 2100
    elif source == "Edmonton" and destination == "Toronto":
        ticketFair = 1750

    if source == "Victoria" and destination == "Edmonton":
        ticketFair = 2400
    elif source == "Victoria" and destination == "Montreal":
        ticketFair = 850
    elif source == "Victoria" and destination == "Toronto":
        ticketFair = 1150

    if source == "Montreal" and destination == "Edmonton":
        ticketFair = 3100
    elif source == "Montreal" and destination == "Victoria":
        ticketFair = 450
    elif source == "Montreal" and destination == "Toronto":
        ticketFair = 900


    fairClass, ticketPrice = fairing(mode,ticketFair)

    if numberOfTickets > 1:
        for i in range(numberOfTickets-1):
            additionalTicket = int(input("Enter age of other passenger: "))
            if additionalTicket < 10:
                total = total + ticketPrice/1.5
            else:
                total += ticketPrice

    total += ticketPrice
    return total





def ticketChecking(name,destination,source,numberOfTickets,mode):

    if destination == source:
        print("Error! Source location cannot be same as current location..")
        return 0, False
    else:
        total = ticketCreation(destination,numberOfTickets,source,mode)
        return total, True


total,check = ticketChecking(name,destination,departureLocation, numberOfTickets, modeTransport)

if check == True:
    print("\nName: ",name,
          "\nNumber of Tickets: ",numberOfTickets,
          "\nDate of Journey: ",dateOfJourney,
          "\nAge: ",age,
          "\nYour ticket total: ",total,
          "\nThank you for booking your ticket. You will get a confirmation over the email shortly!")













