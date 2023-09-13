# Function to generate a username based on user input
def generate_username(existing_usernames):
    while True:
        # Prompt the user for input
        user_input = input("Enter your desired username: ")

        # Check if the username is already taken
        if user_input in existing_usernames:
            print("Username is already taken. Please choose another.")
        else:
            # Username is unique, return it
            return user_input

if _name_ == "_main_":
    print("Welcome to the Username Generator!")

    # List to store existing usernames
    existing_usernames = []

    # Number of usernames to generate (you can change this as needed)
    num_usernames = 5

    for i in range(num_usernames):
        print(f"\nGenerating Username {i + 1}/{num_usernames}")
        username = generate_username(existing_usernames)
        existing_usernames.append(username)
        print(f"Your unique username is: {username}")