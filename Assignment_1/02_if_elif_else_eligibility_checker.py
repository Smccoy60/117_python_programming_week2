employee_name = input("Enter employee name: ")
employee_years_of_service = int(input("Enter employee years of service: "))

print("Congratulations, " + employee_name)
print("You are elgible for the following award")

if employee_years_of_service >= 25:
    print("250.00")
elif employee_years_of_service >= 20:
    print("200.00")
elif employee_years_of_service >= 15:
    print("150.00")
elif employee_years_of_service >= 10:
    print("100.00")
elif employee_years_of_service >= 5:
    print("50.00")
else: 
    print("You are not eligible for a service award at this time.")
