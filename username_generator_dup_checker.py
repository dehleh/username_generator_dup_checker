import datetime
import getpass


#Flower box section

###############################################
#    Name:
#    Date:
#    Program Description:



##############################################

# Lists and dictionary to store employee data
employee_data_list = []
username_list = []
employee_data_dict = {}

# Function to validate input length
def validate_length(input_str, min_length):
    return len(input_str) >= min_length

# Function to create a username
def create_username(first_name, last_name, birth_year):
    first_initial = first_name[0].lower()
    username = first_initial + last_name.lower() + birth_year[-2:]
    return username

# Input loop for 5 employees
for _ in range(5):
    while True:
        # Gather user input
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        birth_year = input("What year were you born? ")

        # Validate input length
        if validate_length(first_name, 2) and validate_length(last_name, 2) and validate_length(birth_year, 4):
            break
        else:
            print("Please make sure your first and last name are at least 2 characters long, and the birth year is 4 characters long.")

    # Display and confirm employee information
    print("Employee Information:")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Year of Birth: {birth_year}")
    confirm = input("Is this information correct? (Yes/No): ")

    if confirm.lower() == "yes":
        # Create username
        username = create_username(first_name, last_name, birth_year)

        # Check for duplicates in the username list
        if username in username_list:
            new_username = first_name.lower() + first_name[0].lower() + birth_year[-2:]
            username_list.append(new_username)
            username = new_username

        # Append to lists and dictionary
        employee_data_list.append((first_name, last_name, birth_year))
        username_list.append(username)
        employee_data_dict[username] = (first_name, last_name, birth_year)
    else:
        # Clear input variables and ask the questions again
        first_name = ""
        last_name = ""
        birth_year = ""

# Get today's date
today_date = datetime.date.today().strftime("%Y-%m-%d")

# Output the requested information
print("Usernames:", username_list)
print("Today's Date:", today_date)
print("Employee Data list:", employee_data_list)
print("Employee Data Dictionary:", employee_data_dict)
