age = int(input("Enter your age: "))  # Ask for age first
is_finnish = input("Are you Finnish? (yes/no): ").strip().lower()  # Then ask nationality

if is_finnish == "yes":
    if age >= 18:
        print("You are eligible for the Finnish voting process.")
    else:
        print("You are not eligible for the Finnish voting process because you are a minor.")
else:
    print("You are not a citizen of the country.")