import sys
if len(sys.argv)==2:
  script_name=sys.argv[0]
  emp_salary=float(sys.argv[1])
else:
  emp_salary=50000

bonus=emp_salary*0.10
total=bonus+emp_salary
print("salary before bonus:",emp_salary)
print(" bonus given:",bonus)
print("salary after bonus:",total)
