while True:
    print("welcome to my program \n")
    choice = input("""press (a) to claculate your age or press (b) to know your birth year \n)

    if choice == "a":
      year_born = input("enter in which year you were born : ")
      year_born = int(year_born)
      print(2022 - year_born, "\n")


    elif choice == "b":
      age = input("enter your current age : ")
      age = int(age)
      print(2022 - age, "\n")
