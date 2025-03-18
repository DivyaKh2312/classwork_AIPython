nationality = input("Enter your nationality: ")
age = int(input("Enter your age: "))

# Convert nationality to lowercase to allow "Finnish" or "finnish"
if nationality.lower() == "finnish" and age >= 18:
    print(f"You are eligible for the {nationality} voting process.")

elif nationality.lower() == "finnish" and age < 18:
    print(f"You are not eligible for the {nationality} voting process because you are a minor.")

else:
    print("You are not a citizen of the country.")