""" 
Michael Barnes 
GPATEST.py
What my app will do is you will enter a studnent LN,FN and then their GPA, once you are done you will be ecsorted back to LN,when  
you arrive back at LN you will be able to  enter another student requirments.Also be causios becuase if accdiently push ZZZ in 
all cap you will be able to exit the program,which will print all done and how many students you have entered . 
"""
while True:
  Count=1
  LastName = input("Enter your last name or enter ZZZ to quit : ")
  Count=Count+1
  if LastName == "ZZZ":
    print("All Done !You have entered",Count,"students")
    break
  FirstName = input("Enter your first name: ")
  GPA = float(input("Enter your GPA: "))

  if GPA >= 3.5:
      print("You are on the Dean's list")
  elif GPA >= 3.25:
      print("You are on the Honor roll")
  else:
      print(FirstName, LastName, "You are not on the Dean's list or the Honor roll")