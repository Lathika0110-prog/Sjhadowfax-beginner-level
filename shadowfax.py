pi=22/7
print(pi)
print(type(pi))


# Assign values to the variables
principal = 1000  # Principal amount (for example, 1000)
rate_of_interest = 5  # Rate of interest (for example, 5%)
time = 3  # Time in years

# Calculate simple interest
simple_interest = (principal * rate_of_interest * time) / 100

# Display the result
print("Simple Interest for 3 years is:", simple_interest)




# Store the principal amount, rate of interest, and time in different variables
P = 1000  # Principal amount (example: $1000)
R = 5     # Rate of interest (example: 5%)
T = 3     # Time in years (example: 3 years)

# Calculate Simple Interest
simple_interest = (P * R * T) / 100

# Print the Simple Interest
print("The Simple Interest is:", simple_interest)



# List of superheroes representing the Justice League
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Print the list of superheroes
print("Justice League Superheroes:")
print(justice_league)

# 2. Access individual superheroes (for example, first and last heroes)
print("\nFirst superhero in the list:", justice_league[0])  # Superman
print("Last superhero in the list:", justice_league[-1])  # Green Lantern

# 3. Add a superhero to the list
justice_league.append("Martian Manhunter")
print("\nUpdated Justice League with Martian Manhunter:")
print(justice_league)

# 4. Remove a superhero (for example, remove Aquaman)
justice_league.remove("Aquaman")
print("\nUpdated Justice League after removing Aquaman:")
print(justice_league)

# 5. Search for a superhero (e.g., check if 'Flash' is in the list)
if "Flash" in justice_league:
    print("\nFlash is part of the Justice League!")
else:
    print("\nFlash is not part of the Justice League!")

# 6. Sort the list alphabetically
justice_league.sort()
print("\nJustice League superheroes sorted alphabetically:")
print(justice_league)

# 7. Reverse the list order (optional)
justice_league.reverse()
print("\nJustice League superheroes in reverse order:")
print(justice_league)



# Function to calculate BMI and determine the category
def calculate_bmi():
    # Ask the user to input height (in meters) and weight (in kilograms)
    height = float(input("Enter your height in meters (e.g., 1.75): "))
    weight = float(input("Enter your weight in kilograms (e.g., 70): "))
    
    # Calculate BMI using the formula: BMI = weight / (height)^2
    bmi = weight / (height ** 2)
    
    # Print the BMI value
    print(f"Your BMI is: {bmi:.2f}")
    
    # Determine the BMI category
    if bmi >= 30:
        print("Category: Obesity")
    elif 25 <= bmi < 30:
        print("Category: Overweight")
    elif 18.5 <= bmi < 25:
        print("Category: Normal")
    else:
        print("Category: Underweight")

# Call the function to execute
calculate_bmi()




# Lists of cities per country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter a city name
city = input("Enter a city name: ").strip()

# Check which country the city belongs to
if city in Australia:
    print(f"{city} is in Australia.")
elif city in UAE:
    print(f"{city} is in the UAE.")
elif city in India:
    print(f"{city} is in India.")
else:
    print(f"Sorry, {city} is not in our database of cities.")




# Lists of cities per country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter two city names
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()

# Check if both cities belong to the same country
if city1 in Australia and city2 in Australia:
    print(f"{city1} and {city2} both belong to Australia.")
elif city1 in UAE and city2 in UAE:
    print(f"{city1} and {city2} both belong to the UAE.")
elif city1 in India and city2 in India:
    print(f"{city1} and {city2} both belong to India.")
else:
    print(f"{city1} and {city2} do not belong to the same country.")



import random

# Variables to track the statistics
count_6 = 0
count_1 = 0
count_two_6s_in_a_row = 0

# Previous roll to check if two 6s were rolled consecutively
previous_roll = None

# Simulate rolling a six-sided die 20 times
for i in range(20):
    roll = random.randint(1, 6)  # Roll the die (random number between 1 and 6)
    
    # Count how many times a 6 is rolled
    if roll == 6:
        count_6 += 1
    
    # Count how many times a 1 is rolled
    if roll == 1:
        count_1 += 1
    
    # Check if two 6s were rolled consecutively
    if roll == 6 and previous_roll == 6:
        count_two_6s_in_a_row += 1
    
    # Update the previous roll for the next iteration
    previous_roll = roll

# Print the statistics
print(f"Number of times 6 was rolled: {count_6}")
print(f"Number of times 1 was rolled: {count_1}")
print(f"Number of times two 6s were rolled in a row: {count_two_6s_in_a_row}")




def workout_routine():
    total_jumping_jacks = 0  # Keep track of the total number of jumping jacks completed
    sets = 10  # Number of jumping jacks per set
    
    # Perform 10 jumping jacks at a time until we reach 100 or the user decides to quit
    for set_number in range(1, 11):  # We need to complete 10 sets of 10 jumping jacks (10 * 10 = 100)
        total_jumping_jacks += sets  # Add the number of jumping jacks in the current set
        
        # Ask the user if they are tired after each set
        tired = input(f"Set {set_number}: You have completed {total_jumping_jacks} jumping jacks. Are you tired? (yes/y to stop): ").strip().lower()
        
        if tired == "yes" or tired == "y":
            skip = input("Do you want to skip the remaining sets? (yes/y to skip): ").strip().lower()
            
            if skip == "yes" or skip == "y":
                print(f"You completed a total of {total_jumping_jacks} jumping jacks.")
                break
    else:
        # If the loop completes all 10 sets, print the final total
        print(f"Congratulations! You completed a total of {total_jumping_jacks} jumping jacks.")

# Call the function to start the workout
workout_routine()

