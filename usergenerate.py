import datetime

# Function to validate the year of birth
def validate_year(year_str):
    try:
        year = int(year_str)
        if 1900 <= year <= datetime.datetime.now().year:
            return year
    except ValueError:
        pass
    return None

# Initialize lists and dictionary
usernames = []
employee_data = {}

# Get user input
for _ in range(3):
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    year_of_birth = None

    while year_of_birth is None:
        year_of_birth = validate_year(input("Enter your year of birth (between 1900 and current year): "))

    # Create the username
    username = first_name[0].lower() + last_name.lower() + str(year_of_birth)[-2:]

    # Check for duplicates
    while username in usernames:
        username = first_name.lower() + last_name[0].lower() + str(year_of_birth)[-2:]

    # Append to the lists and dictionary
    usernames.append(username)
    employee_data[username] = (first_name, last_name, year_of_birth)

# Get today's date
current_date = datetime.date.today()

# Output the information
print("\nUsername:", usernames)
print("Today's Date:", current_date)
print("Employee Data list that you used to gather user input:")
for username, data in employee_data.items():
    print(f"Username: {username}, First Name: {data[0]}, Last Name: {data[1]}, Year of Birth: {data[2]}")
print("Username list with all usernames:", usernames)
print("Employee data dictionary:", employee_data)
