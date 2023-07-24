import random

print("\nSchool admission Form\n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
dob = input("Please enter your date of birth: ")
email = input("Please enter your email address: ")
contact = int(input("Please enter your contact number: "))

print("\nPlease Enter Your High School grades Out Of 100\n")
science = int(input("Enter your Science grades: "))
maths = int(input("Enter your Maths grades: "))
socialScience = int(input("Enter your Social Science grades: "))
english = int(input("Enter your English grades: "))

percentage = (science + maths + socialScience + english)/400*100
print("\nYour percentage is", percentage)


def course():
    stream1 = ["Arts"]
    stream2 = ["Arts", "Commerce"]
    stream3 = ["Arts", "Commerce", "Science"]

    if percentage < 50:
        print("You need atleast 50 percent for your admission")
    elif percentage >= 50 and percentage <= 65:
        print("\n", stream1,"\nPlease select a stream.\nSelect number as per the order: ")
        sub = stream1[int(input("Select your stream:"))-1]
        print("\nYou've selected", sub, "as your stream.")
    elif percentage >= 66 and percentage <= 80:
        print("\n", stream2,"\nPlease select a stream.\nSelect number as per the order: ")
        sub = stream2[int(input("Select your stream:"))-1]
        print("\nYou've selected", sub, "as your stream.")
    elif percentage >= 81 and percentage <= 100:
        print("\n", stream3,"\nPlease select a stream.\nSelect number as per the order: ")
        sub = stream3[int(input("Select your stream:"))-1]
        print("\nYou've selected", sub, "as your stream.")

max_length = 6

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

combinedList = numbers

randomNumbers = random.choice(numbers)

password = randomNumbers

for i in range(max_length-1):
    password = password + random.choice(combinedList)


def streamChecking(percentage):

    if percentage > 100:
        print("Error!")
        return 0, False

    else:
        sub = course()
        return sub, True


sub, check = streamChecking(percentage)

if check == True:
    print("\nName:", name,
          "\nAge:", age,
          "\nDate of Birth:", dob,
          "\nEmail:", email,
          "\nContact:", contact,
          "\nPercentage:", percentage,
          "\nYour Roll Number is: ", password)
