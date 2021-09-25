#wage = (((33000/12)/4)/40)
eur = (3.30)





wage = int(input("Hourly pay in Germany is €"))
xcd = wage * eur
print("Converted to XCD, this is equal to $", xcd)
salary = (((wage * 40)*4)*12)
totalxcd = salary * eur
print("Average Gross Salary of an entry level IT help Desk employee is €", salary,". Converted to XCD, this is $", totalxcd)
parttime = (wage * 17) * 4
ptxcd = parttime * eur
print("If I were to work a part-time job at this wage, I would make €", parttime ,". In XCD, this is $", ptxcd)
salary_parttime = parttime * 12
sptxcd = salary_parttime * eur
print("Yearly salary would be €15", salary_parttime," and $", sptxcd," in xcd.")