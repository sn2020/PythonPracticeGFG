def validate_and_execute():
    try:
        user_input_int = int(number_of_days_element)
        if user_input_int > 0:
            hours = days_to_units(user_input_int)
            print(hours)
        elif user_input_int == 0:
            print("you entered 0, please enter a positive number\n")
        else:
            print("You have entered a negative number please enter only integer\n")
    except:
        print("your input is not valid\n")