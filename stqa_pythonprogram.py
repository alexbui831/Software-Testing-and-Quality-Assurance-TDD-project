import sys


def main():

  print("\nWhich function would you like me to perform?")
  print("1. Body Mass Index Calculation.")
  print("2. Retirement Calculation.")
  print("3. Exit Program.")
  answer = input()

  if answer == "1": 
    bmi_inputs()
  if answer == "2":
    retirement_inputs()
  if answer == "3":
    endprogram()
  if answer != ["1", "2", "3"]:
    main()


def bmi_inputs():

  print("This function will calculate BMI for the user.")
  print("Input Height in feet and inches.")
  hFt = float(input("Feet:"))
  hInch = float(input("Inches:"))
  weight = float(input("Input weight in pounds:"))

  bmi_analysis(bmi_calc(hFt, hInch, weight))
            
  
def bmi_calc(hFt, hInch, weight):

  # Calculates body mass index
  BMI = ((weight * .45) / (((hFt * 12) + hInch)* .025) **2)

  return BMI

def bmi_analysis(BMI):

  print("BMI:", round(BMI, 2))

  if BMI < 18.5:
    print("User is underweight.")
    analysis = "underweight"
  if BMI >= 18.5 and BMI <= 24.9:
    print("User is normal weight.")
    analysis = "normal weight"
  if BMI >= 25 and BMI <= 29.9:
    print("User is overweight.")
    analysis = "overweight"
  if BMI >= 30:
    print("User is obese.")
    analysis = "obese"

  return analysis


def retirement_inputs():

  print("This function will calculate how long it wll take for the user to reach retirement.")

  age = int(input("Input age:"))
  yearSalary = float(input("Input annual salary:"))
  percentSaved = float(input("Input percentaged of salary saved:"))
  desiredSalary = float(input("Input retirement saving goal:"))

  # Calls retirement_calc
  retirement_analysis(retirement_calc(age, yearSalary, percentSaved, desiredSalary))


def retirement_calc(age, yearSalary, percentSaved, desiredSalary):

  # Calculates what age user will be when saving goal is met
  savingPerYear = (yearSalary * percentSaved) * 1.35
  yearsUntilAchievement = (desiredSalary / savingPerYear)
  futureAge = age + yearsUntilAchievement

  return futureAge


def retirement_analysis(futureAge):

  if futureAge > 100:
    print("Age when goal will be met:", round(futureAge, 0), "\nUnfortunately, you will probably be dead before you meet that goal.")
    success = "fail to save"
  if futureAge <= 100:
    print("Age when goal will be met: ", round(futureAge,0))
    success = "saving was a success"
    
  return success

def endprogram():

  sys.exit(0)


main()