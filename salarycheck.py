salary = float(input("Enter your salary: "))

if salary < 30000:
    tax_rate = 5

elif salary <= 70000:
    tax_rate = 15

else:
    tax_rate = 25


final_tax = (salary * tax_rate) / 100


print("Salary =", salary)
print("Tax Rate =", tax_rate, "%")
print("Final Tax =", final_tax)