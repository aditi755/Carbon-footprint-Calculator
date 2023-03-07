# Carbon Footprint Tracker Program

# Set up the dictionary to store user data
user_data = {
    "Name": "",
    "Electricity": 0,
    "Gas": 0,
    "Transportation": 0,
    "Waste": 0
}

# Define the function to get user input and update the dictionary
def get_user_input():
    user_data["Name"] = input("Enter your name: ")
    user_data["Electricity"] = float(input("Enter your electricity usage (in kWh): "))
    user_data["Gas"] = float(input("Enter your gas usage (in therms): "))
    user_data["Transportation"] = float(input("Enter your transportation emissions (in metric tons of CO2 equivalent): "))
    user_data["Waste"] = float(input("Enter your waste emissions (in metric tons of CO2 equivalent): "))

# Define the function to calculate the total carbon footprint
def calculate_carbon_footprint():
    total_footprint = user_data["Electricity"] * 0.0006 + user_data["Gas"] * 5.53 + user_data["Transportation"] * 19.6 + user_data["Waste"] * 1.06
    return total_footprint

# Define the main function to call other functions
def main():
    get_user_input()
    total_footprint = calculate_carbon_footprint()
    print(f"\n{user_data['Name']}, your total carbon footprint is {total_footprint:.2f} metric tons of CO2 equivalent.")

# Call the main function to run the program
if _name_ == "_main_":
    main()
