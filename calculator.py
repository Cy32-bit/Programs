import math

def basic_calculator():
    print("\n=== Calculator ===")
    print("1. Basic Operations (+, -, *, /)")
    print("2. Power and Root")
    print("3. Trigonometric Functions")
    print("4. Logarithmic Functions")
    print("5. Area Calculations")
    print("0. Exit")

    while True:
        choice = input("\nEnter your choice (0-5): ")

        if choice == '0':
            print("Thank you for using the calculator!")
            break

        elif choice == '1':
            print("\n=== Basic Operations ===")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("\nSelect operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            
            op = input("Enter operation (1-4): ")
            if op == '1':
                print(f"Result: {num1 + num2}")
            elif op == '2':
                print(f"Result: {num1 - num2}")
            elif op == '3':
                print(f"Result: {num1 * num2}")
            elif op == '4':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero!")

        elif choice == '2':
            print("\n=== Power and Root ===")
            num = float(input("Enter the number: "))
            print("\n1. Square")
            print("2. Cube")
            print("3. Custom power")
            print("4. Square root")
            print("5. Cube root")
            
            op = input("Enter operation (1-5): ")
            if op == '1':
                print(f"Result: {num ** 2}")
            elif op == '2':
                print(f"Result: {num ** 3}")
            elif op == '3':
                power = float(input("Enter the power: "))
                print(f"Result: {num ** power}")
            elif op == '4':
                if num >= 0:
                    print(f"Result: {math.sqrt(num)}")
                else:
                    print("Error: Cannot calculate square root of negative number!")
            elif op == '5':
                print(f"Result: {num ** (1/3)}")

        elif choice == '3':
            print("\n=== Trigonometric Functions ===")
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print(f"Sine: {math.sin(rad)}")
            print(f"Cosine: {math.cos(rad)}")
            print(f"Tangent: {math.tan(rad)}")

        elif choice == '4':
            print("\n=== Logarithmic Functions ===")
            num = float(input("Enter the number: "))
            if num > 0:
                print(f"Natural logarithm (ln): {math.log(num)}")
                print(f"Base-10 logarithm: {math.log10(num)}")
            else:
                print("Error: Cannot calculate logarithm of non-positive number!")

        elif choice == '5':
            print("\n=== Area Calculations ===")
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")
            
            shape = input("Select shape (1-3): ")
            if shape == '1':
                radius = float(input("Enter radius: "))
                print(f"Area: {math.pi * radius ** 2}")
            elif shape == '2':
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                print(f"Area: {length * width}")
            elif shape == '3':
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                print(f"Area: {0.5 * base * height}")

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    basic_calculator()