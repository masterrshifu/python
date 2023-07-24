### Task: School admission system ###
## START ##
# Taking details #
print('http//www.OxfordAcademy/Admission/College.com')
print('Welcome! This is the Oxford College admission system:')
Name = input('Name: ')
Age = int(input('Age: '))
while(Age < 17):
  print('You are not eligible for going to a college!')
  Age = int(input('Age: '))
DOB = input('Please enter your DOB in this format DD/MM/YYYY: ')
EA = input('Email address: ')
Contact = int(input('Contact No: '))

# Showing Streams #
List = ['Arts', 'Commerce', 'Science']
print('You can go to:')
print(List)
chosen = int(input('Choose one as per the order:'))

# Taking Grades #
import random
sub = []
numberOfSub = 0
print('Type your scores(out of 100): ')
print('(If score is in decimal round it up and send it here)')
if chosen == 1:
  Arts = int(input('Arts and Crafts: '))
  sub = [Arts]
  numberOfSub = 1
elif chosen == 2:
  English = int(input('English: '))
  Maths = int(input('Maths: '))
  BusinessStudies = int(input('Business Studies: '))
  sub = [English,Maths,BusinessStudies]
  numberOfSub = 3
elif chosen == 3:
  Biology = int(input('Biology: '))
  Chemistry = int(input('Chemistry: '))
  Physics = int(input('Physics: '))
  sub = [Biology,Chemistry,Physics]
  numberOfSub = 3
# Finding Percentage  #
total = 0
for i in range(len(sub)):
  total += sub[i] 
def percentager(numberOfSub,sub,total):
  if total <= numberOfSub * 100:
    percent =  total/numberOfSub
    return percent
  else:
    print('Invalid Inputs')
    return 0
percentage = percentager(numberOfSub,sub,total)
print(percentage,'%')

# Choosing Roll No #
list = ['1','2','3','4','5','6','7','8','9']
rollno = ''
def rollno():
  r1 = random.choice(list)
  r2 = random.choice(list)
  r3 = random.choice(list)
  r4 = random.choice(list)
  r5 = random.choice(list)
  r6 = random.choice(list)
  r7 = random.choice(list)
  roll = r1 + r2 + r3 + r4 + r5 + r6 + r7
  return roll

# Your College choosing #
Colleges = ['Delhi','Bangalore','Kolkata']
if percentage >= 90:
  print('You can go to:')
  print(Colleges)
  College = int(input('Choose the desired place of College(according to no): '))-1
elif percentage > 90 and percentage <= 80:
  Colleges.remove('Delhi')
  print('You can go to:')
  print(Colleges)
  College = int(input('Choose the desired place of College(according to no): '))-1
elif percentage >= 50 and percentage < 80:
  print('You can go to Bangalore only:')
  College = int(input('Do you accept:(Type 1 if you accept and 0 if you dont):  '))
  if College != 1:
    chosen = 0
else:
  College = 'None' 
if chosen >= 4 or total > numberOfSub*100 or percentage < 50:
  print('Quitting...')
else: 
  stream = List[chosen-1]
  rollno = rollno()
  print('Name:',Name,
  '\nAge:',Age,
  '\nRoll No:',rollno,
  '\nDOB:',DOB,
  '\nEmail:',EA,
  '\nContact No:',Contact,
  '\nStream:',stream,
  '\nCollege:',Colleges[College])
## END ##