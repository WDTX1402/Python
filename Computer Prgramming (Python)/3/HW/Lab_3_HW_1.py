a1 = (input("Enter employee's name: "))
a2 = float(input("Enter number of hours worked in a week: "))
a3 = float(input("Enter hourly pay rate: "))
a4 = float(input("Enter federal tax withholding rate: "))
a5 = float(input("Enter state tax withholding rate: "))




c1 = a2 * a3
c2 = c1 * a4
c3 = c1 * a5
c4 = c2 + c3
c5 = c1 - c4



print("Employee Name: ", a1)
print("Hours Worked: ", a2)
print("Pay Rate: $", a3)
print("Gross Pay: $", c1)
print("Deductions:")
print("\tFederal Withholding", "(", format(a4, "4.1%"), "\b)", ": $", round(c2, 2))
print("\tState Withholding", "(", format(a5, "4.1%"), "\b)" ": $", round(c3, 2))
print("\tTotal Deduction: $", round(c4, 2))
print("Net Pay: $", round(c5, 2))






