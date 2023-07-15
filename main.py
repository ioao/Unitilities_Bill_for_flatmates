from appartment import Bill, Flatmate
from reports import PdfReport

amount = float(input("Please enter the amount of the Monthly Utilities Bill: ")) # amount of the bill
period = input("What is the bill period? E.g. November 2022: ")
currency = " czk"

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the Bill Period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the Bill Period? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2), currency)
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1), currency)

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)