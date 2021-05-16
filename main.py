from helper import validate_and_execute

cal_to_units = 24
type_of_unit = "hours"


def days_to_units(count_of_days):
    return f"{count_of_days} days have {count_of_days * cal_to_units} {type_of_unit}"

 
user_input = " "
while user_input != "exit":
    user_input = input("hey user enter no of days as a comma separated list & I will convert it to hours\n")
    list_of_days = user_input.split(", ")
    print(type(list_of_days))
    print(list_of_days)
    set_of_days = set(user_input.split(", "))
    print(type(set_of_days))
    print(set_of_days)

    for number_of_days_element in set(user_input.split(", ")):
        validate_and_execute()


