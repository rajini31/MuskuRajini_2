
print("      BMI CALCULATOR")


name = input("Enter your name: ")

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than 0.")

    else:
        bmi = weight / (height ** 2)

        print("\n----- RESULT -----")
        print("Name:", name)
        print("BMI:", round(bmi, 2))

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("Category:", category)

        file = open("records.txt", "a")
        file.write(
            f"{name}, {weight}, {height}, {round(bmi,2)}, {category}\n"
        )
        file.close()

        print("\nData saved successfully!")

except ValueError:
    print("Please enter valid numbers.")