import math #imported to use floor(()


# Function to calucate age to savings goal
def calucate_years_to_goal (age, annual_sal, percentage, goal):
    x = False

    try:
        age = int(age)
        annual_sal = int(annual_sal)
        percentage = int(percentage)
        goal = int(goal)

    except ValueError:
        print("")
        print ("YOUR INPUT IS INVALID!")
        age_to_goal = "Invalid"
        x = True

    else:
        if (x == True):
            return age_to_goal

        putback = (percentage/100) * annual_sal* 2
        years = goal/putback
        age_to_goal = years + age
        age_to_goal = math.floor(age_to_goal)

        #IF age is equal or over 100

        if age_to_goal >= 100:
        
            print("\nGOAL WILL NOT BE REACHED IN A LIFETIME")
            print("Your age when goal is reached:")
            return age_to_goal
        else:
            print("\nYour age when goal is reached:")
            return age_to_goal

