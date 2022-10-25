print("I convert talents, pounds and lots to kilograms.")
talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: "))
lot = float(input("Enter lots: "))
P = talent * 20 * 32 * 13.3
L = pound * 32 * 13.3
G = lot * 13.3
K = (P + L + G) / 1000
g = (K * 1000) - (K * 1000)
print(f"The total weight in kilograms is: {K}Kg and:{g:6.0f}g")
