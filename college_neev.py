def main():
  choice = str(input("Would you like to apply for this college? (YES OR NO):"))
  
  if choice == "YES":
      print("Great! We will require the basic information first!")
      name = input("Input your name:")
      age = int(input("Input your age:"))
      gmail = input("Input your email id:")
      if age <= 17:
        print("Sorry you are too young to apply for college")
      if age >= 17:
        print("Great! We currently have three streams available\nMaths\nScience\nArts")
        print("Please enter the marks you earned, and we will show the streams available to you (OUT OF 100).")
        maths = int(input("Maths:"))
        sci = int(input("Science:"))
        arts = int(input("Arts:"))
        if sci >= 90 and maths >= 90 and arts >=90:
          ch = input("Great! Arts and Maths and Science are available to you. Please choose:")
        if sci >= 90 and maths <= 90 and arts <= 90:
          ch = input("Great! Science is available to you. Please choose:")
        if sci >= 90 and maths >= 90 and arts <= 90:
          ch = input("Great! Science and Maths are available to you. Please choose:")
        if sci <= 90 and maths <= 90 and arts >= 90:
          ch = input("Great! Arts is available to you. Please choose:")
        if sci <= 90 and maths >= 90 and arts >= 90:
         ch = input("Great! Maths and Arts are available to you. Please choose:")
        if sci >= 90 and maths <= 90 and arts >= 90:
          ch = input("Great! Science and Arts are available to you. Please choose:")
        if sci <= 90 and maths <= 90 and arts <= 90:
          print("Sorry no stream is availble to you.")
          print("Please try next year.")
            
  
      print("Great lets have a online interview two weeks later")
      print("Name:",name,
        "Age:", age,
        "Gmail(to which to meeting link will be sent):",gmail,
        "Stream:",ch)
  elif choice == "NO":
    print("Ok then")


main()
