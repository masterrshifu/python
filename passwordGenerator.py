import random

max_length = 8


numbers = ['0','1','2','3','4','5','6','7','8','9']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
specialCharacters = ['!','#', '$', '%', '&', '~']

combinedList = numbers + lowerCase + upperCase + specialCharacters


randomNumber = random.choice(numbers)
randomLower = random.choice(lowerCase)
randomUpper = random.choice(upperCase)
randomSpecial = random.choice(specialCharacters)

password = randomLower + randomNumber + randomUpper + randomSpecial


for i in range(max_length-4):
    password = password + random.choice(combinedList)

print(password)
