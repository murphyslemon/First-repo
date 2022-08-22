print("hello everyone")

print("good")
print("morning")

first_number = 3
print(first_number)

fahrenheit_str = input("Temperature in fahrenheit:")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit - 32)*5/9
print(f"Temperature in celsius:{celsius:6.2f}")

height_str = input("Your height in metres:")
weight_str = input("Your weight in kilograms:")
height = float(height_str)
weight = float(weight_str)
BMI = weight/(height*height)
print(f"This is your BMI:{BMI:6.1f}")