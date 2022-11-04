




def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetHours():
    hours = float(input("Enter hours worked: "))
    return hours

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate


def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
    print(empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Number of Hours: {TotHours:,.2f}")
    print(f"Total Gross Pay: {TotGrossPay:,.2f}")
    print(f"Total Tax: {TotTax:,.2f}")
    print(f"Total Net Pay: {TotNetPay:,.2f}")
 

if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break

        hours = GetHours()
        
        hourlyrate = GetHourlyRate()
       
        taxrate = GetTaxRate()
        
             
        # write the code to assign to hours the return value from GetHoursWorked

        # write the code to assign to hourlyrate the return value from GetHourlyRate

        # write the code to assign to taxrate the return value from GetTaxRate
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

        # write the code to increment the other total variables with the appropriate values


    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)



