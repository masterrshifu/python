### Task: School admission system ###
## START ##
# Taking details #
Name = input('Tell your name: ')
Age = int(input('Tell your age: '))
DOB = input('Please enter your DOB in this format DD/MM/YYYY: ')
EA = input('Tell your email address: ')
Contact = int(input('Tell your contact no: '))

# Taking Grades #
import random
percentage = 0
List = ['Arts', 'Commerce', 'Science']
print('Type your scores(out of 100): ')
print('(If score is in decimal round it up and send it here)')
Maths = int(input('Maths: '))
Chemistry = int(input('Chemistry: '))
Biology = int(input('Biology: '))
Physics = int(input('Physics: '))
History = int(input('History: '))
Geography = int(input('Geography: '))
Civics = int(input('Civics: '))
L2 = int(input('L2: '))
L3 = int(input('L3: '))
ELan = int(input('ELan: '))
Elit = int(input('ELit: '))
Computer = int(input('Computer: ')) 

# Finding Percentage  #
def percentager(Maths, Chemistry ,Biology , Physics , Geography , History , Civics , L2 , L3 , Elit , ELan , Computer):
  total = Maths + Chemistry + Biology + Physics + Geography + History + Civics + L2 + L3 + Elit + ELan + Computer
  if total <= 1200:
    percent =  total/1200 * 100
    return percent
  else:
    print('Invalid Inputs')
    return 0
percentage = percentager(Maths, Chemistry ,Biology , Physics , Geography , History , Civics , L2 , L3 , Elit , ELan , Computer)
print(percentage,'%')

# Showing Streams #
if percentage >= 80:
  print('You can go to:')
  print(List)
  chosen = int(input('Choose one as per the order(Press any key greater than 3 if you want to exit):'))-1
elif percentage < 80.0 and percentage >= 40.0:
  List.remove('Science')
  print('You can go to:')
  print(List)
  chosen = int(input('Choose one as per the order:(Press any key greater than 2 if you want to exit ): '))-1
elif percentage > 10.0 and percentage < 40.0:
  print('You can go to only Art')
  chosen = int(input('Do you accept:(Press any key greater than 3 if you want to exit): '))-1
else:
  print('Sorry but looks like there is no space for you!')
  chosen = 0

# Choosing Roll No #
rollno = ''
def rollno():
  r1 = random['1','2','3','4','5','6','7','8','9']
  r2 = random['1','2','3','4','5','6','7','8','9']
  r3 = random['1','2','3','4','5','6','7','8','9']
  r4 = random['1','2','3','4','5','6','7','8','9']
  r5 = random['1','2','3','4','5','6','7','8','9']
  r6 = random['1','2','3','4','5','6','7','8','9']
  r7 = random['1','2','3','4','5','6','7','8','9']
  roll = r1 + r2 + r3 + r4 + r5 + r6 + r7
  return roll
if chosen >= 4 or chosen < 1:
  print('Quitting...')
else: 
  rollno = rollno()
  print('Name: ',Name,
  '\nAge:',Age,
  '\nRoll No: ',rollno,
  '\nDOB: ',DOB,
  'Email',EA,
  'Contact No: ',Contact)
## END ##